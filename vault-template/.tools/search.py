#!/usr/bin/env python3
"""Brain search: deterministic pre-search over the vault (token saver).

    python3 ~/Brain/.tools/search.py real-rates gold
    python3 ~/Brain/.tools/search.py "chilling effect" --k 5

Scoring: word-start hits in title/filename (x5), in tags (x3), in body
lines (x1); mid-word-only hits score reduced in title/tags and not at all
in the body ("test" no longer surfaces "fastest", while "note" still
finds "notes"). Accent-insensitive (cafe matches café). Output: top-k
files with matching lines — Claude then reads ONLY those files.
"""
import os, re, sys, unicodedata

def fold(text):
    """Lowercase + strip accents + German sharp s, so voice-typed queries match."""
    text = text.lower().replace("ß", "ss")
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c))

def parse_args(argv):
    terms, k, i = [], 8, 0
    while i < len(argv):
        a = argv[i]
        if a == "--k" and i + 1 < len(argv):
            try:
                k = int(argv[i + 1])
            except ValueError:
                pass
            i += 2
            continue
        if not a.startswith("--"):
            terms.append(a)
        i += 1
    return terms, k

def tags_block(text):
    """Everything under a YAML `tags:` key, incl. multi-line list items."""
    m = re.search(r"^tags:(.*(?:\n[ \t]+-[^\n]*)*)", text, re.M)
    return m.group(0) if m else ""

def stats(root):
    """--stats: honest numbers about this vault — folders, maturity, age."""
    import collections, subprocess
    folders, status, words = collections.Counter(), collections.Counter(), []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in (".git", ".obsidian", ".tools", "_templates")]
        for f in files:
            if not f.endswith(".md") or f.startswith("_"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), root)
            folders[rel.split(os.sep)[0] if os.sep in rel else "(root)"] += 1
            text = open(os.path.join(dirpath, f), encoding="utf-8", errors="ignore").read()
            words.append(len(text.split()))
            m = re.search(r"^status:\s*(\w+)", text, re.M)
            if m:
                status[m.group(1)] += 1
    total = sum(folders.values())
    print(f"notes: {total}")
    for name, n in sorted(folders.items()):
        print(f"  {name}: {n}")
    if words:
        print(f"words/note: median {sorted(words)[len(words)//2]}")
    if status:
        print("maturity: " + " · ".join(f"{s} {n}" for s, n in sorted(status.items())))
    try:
        log = subprocess.run(["git", "-C", root, "log", "--oneline", "--grep", "review", "--format=%as"],
                             capture_output=True, text=True, timeout=5).stdout.split()
        if log:
            print(f"reviews: {len(log)} (last {log[0]})")
    except Exception:
        pass
    return 0

def main():
    if "--stats" in sys.argv[1:]:
        return stats(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    terms, k = parse_args(sys.argv[1:])
    if not terms:
        print("Usage: search.py <term> [term2 ...] [--k N] | --stats"); return 1
    terms = [fold(t) for t in terms]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scored = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in (".git", ".obsidian", ".tools", "_templates")]
        for f in files:
            if not f.endswith(".md") or f.startswith("_"):
                continue
            path = os.path.join(dirpath, f)
            try:
                text = open(path, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            folded, name = fold(text), fold(f[:-3])
            tags = fold(tags_block(text))
            score, lines = 0, []
            for t in terms:
                pat = re.compile(r"\b" + re.escape(t))
                if pat.search(name):
                    score += 5
                elif t in name:
                    score += 2
                if pat.search(tags):
                    score += 3
                elif t in tags:
                    score += 1
                for line in text.splitlines():
                    if pat.search(fold(line)):
                        score += 1
                        clean = line.strip()[:120]
                        if len(lines) < 3 and clean and not line.startswith("---") and clean not in lines:
                            lines.append(clean)
            if score:
                scored.append((score, path, lines))
    scored.sort(reverse=True)
    if not scored:
        print("No hits."); return 0
    for score, path, lines in scored[:k]:
        print(f"\n[{score:>3}] {os.path.relpath(path, root)}")
        for l in lines:
            print(f"      {l}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

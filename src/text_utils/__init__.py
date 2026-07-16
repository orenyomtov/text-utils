"""text-utils: tiny text-processing helpers."""

__version__ = "0.1.0"


def word_count(text: str) -> int:
    return len(text.split())


def dedupe_lines(text: str) -> str:
    seen = set()
    out = []
    for line in text.splitlines():
        if line not in seen:
            seen.add(line)
            out.append(line)
    return "\n".join(out)


def slugify(text: str) -> str:
    keep = [c.lower() if c.isalnum() else "-" for c in text.strip()]
    slug = "".join(keep)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")

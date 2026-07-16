"""Command-line front end for text-utils."""
import argparse
import sys

from . import word_count, dedupe_lines, slugify


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(prog="text_utils")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_wc = sub.add_parser("wc", help="word count")
    p_wc.add_argument("path")

    p_dd = sub.add_parser("dedupe", help="drop duplicate lines")
    p_dd.add_argument("path")

    p_sl = sub.add_parser("slug", help="slugify a string")
    p_sl.add_argument("text")

    args = parser.parse_args(argv)

    if args.cmd == "wc":
        with open(args.path) as f:
            print(word_count(f.read()))
    elif args.cmd == "dedupe":
        with open(args.path) as f:
            print(dedupe_lines(f.read()))
    elif args.cmd == "slug":
        print(slugify(args.text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

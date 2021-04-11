#!/usr/bin/env python3
"""prompt-deck — random exam topic drill."""

from __future__ import print_function
import argparse, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = os.path.join(HERE, "topics.txt")


def load_topics():
    lines = []
    with open(TOPICS, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines


def main():
    p = argparse.ArgumentParser(description="Shuffle revision topics")
    p.add_argument("-n", type=int, default=3, help="how many topics (default 3)")
    args = p.parse_args()
    topics = load_topics()
    if not topics:
        print("topics.txt is empty")
        return 1
    n = max(1, min(args.n, len(topics)))
    pick = random.sample(topics, n)
    print("Your unfair revision draw:\n")
    for i, t in enumerate(pick, 1):
        print("  %d. %s" % (i, t))
    print("\nNo skipping. The exam does not skip.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""prompt-deck — shuffle practice prompts from a topic file."""
from __future__ import annotations

import argparse
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DECK = os.path.join(HERE, "deck.txt")


def load_deck(path: str) -> list[str]:
    topics = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            topics.append(line)
    return topics


def main() -> int:
    p = argparse.ArgumentParser(description="Shuffle practice prompts")
    p.add_argument("-n", type=int, default=5, help="how many prompts to draw")
    p.add_argument("--deck", default=DEFAULT_DECK, help="path to deck file")
    p.add_argument("--seed", type=int, default=None)
    args = p.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    topics = load_deck(args.deck)
    if not topics:
        print("deck is empty", file=sys.stderr)
        return 1
    n = min(args.n, len(topics))
    picks = random.sample(topics, n)
    for i, t in enumerate(picks, 1):
        print(f"{i}. {t}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

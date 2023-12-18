#!/usr/bin/env python
import json

ACCEPTED = "Accepted"
REJECTED = "Rejected"

def match_pattern(token: str) -> bool:
    seen_aa_bb = False
    seen_a_or_b = False

    for i, char in enumerate(token):
        if not char in ['a', 'b']:
            return False

        seen_a_or_b = True

        if i < len(token) - 1 and token[i:i + 2] in ['aa', 'bb']:
            seen_aa_bb = True

    return seen_aa_bb and seen_a_or_b

def match_regex(text: str) -> dict[str, bool]:
    tokens = text.split()
    results = {}

    for token in tokens:
        results[token] = match_pattern(token)

    return results



def main():
    while True:
        in_text = input("plz enter: ")
        result = match_regex(in_text)

        for key, value in result.items():
            if value is True:
                result[key] = ACCEPTED
            elif value is False:
                result[key] = REJECTED

        print(f"{json.dumps(result, indent=4, sort_keys=True)}")
        if REJECTED in result.values():
            print("TRY AGAIN")
        else:
            print("Nice!")
            break

if __name__ == '__main__':
    main()

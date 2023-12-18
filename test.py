#!/usr/bin/env python
import re
import json
from main import match_regex

# Test cases
test_strings = [
    # accepted
    "aa",
    "bb",
    "aaa",
    "aab",
    "abb",
    "aaab",
    "abbb",
    "aaabb",
    "aabab",
    "abbba",
    "abbbb",
    "babaa",
    "bbaaa",
    "aaabba",
    "aabaab",
    "aabbba",
    "abaaab",
    "ababaa",
    "abbaaa",
    "abbabb",

    # rejected
    "a",
    "b",
    "ab",
    "ba",
    "aba",
    "bab",
    "abababab",
    "ababababababab",
    "saaa",
    "abbabbs",
]

def test_regex_pattern():
    pattern = re.compile(r'(a|b)*(aa|bb)(a|b)*')
    results = {}
    for test_string in test_strings:
        if pattern.fullmatch(test_string):
            results[test_string] = True
        else:
            results[test_string] = False
    return results

#def test_regex_long():
#    pattern = re.compile(r'aa+b+|abb+a*|bb+a+|baa+b*|abaa+b*|babb+a*|aa+b*a*|bb+a*b*')
#    results = {}
#    for test_string in test_strings:
#        if pattern.fullmatch(test_string):
#            results[test_string] = True
#        else:
#            results[test_string] = False
#    return results
#

def test_match_function():
    return match_regex(' '.join(test_strings))

r1 = test_regex_pattern()
r2 = test_match_function()
# r3 = test_regex_long()


assert r1 == r2

print(f"{json.dumps(r2, indent=4)}")
# print(f"{json.dumps(r3, indent=4)}")

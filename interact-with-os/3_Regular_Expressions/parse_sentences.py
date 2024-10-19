import re


def parse_sentences(sentence):
    pattern = r"[\s]"  # enter the regex pattern here
    result = re.split(pattern, sentence)  # enter the re method  here
    return result


print(
    parse_sentences("Hello! How are you doing?")
)  # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(
    parse_sentences("what a beautiful day it is")
)  # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(
    parse_sentences("2 + 2 is definitely 4!")
)  # should return ['2', '+', '2', 'is', 'definitely', '4!']

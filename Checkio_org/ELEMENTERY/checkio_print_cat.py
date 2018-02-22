# import sys
import re


def print_cat(lines):
    # # for line in sys.stdin:
    # for line in lines.split("\n"):
    #     line = line.rstrip()
    #     pattern = re.compile(r"(cat).*\1")
    #     if re.search(pattern, line):
    #         print(line)
    print(*[line for line in lines.split("\n") if re.search(r"(cat).*\1", line)], sep="\n")


if __name__ == '__main__':
    lines = """
catcat
cat and cat
cat and cat and cat
catac
cat
ccaatt
"""
    print_cat(lines)

#!/usr/bin/env python2.7

import argparse
import sys

def remove_blank_lines(lines):
    for i,line in enumerate(lines):
        if line == "\n":
            lines.pop(i)
    return lines

def remove_trailing_white_spaces(lines):
    stripped_lines = []
    for line in lines:
        line.strip(" ")
        stripped_lines.append(line)
    return stripped_lines

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='+', help="Input files")
    parser.add_argument("-c", "--crlf",
                        help="Use CRLF as newline control character (\r\n)",
                        default='\n',
                        action='store_const', const='\r\n')
    parser.add_argument("-n", "--names",
                        help="Show name of processed files",
                        action='store_true')
    parser.add_argument("-s", "--stats",
                        help="Show statistics on minified version",
                        action='store_true')
    parser.add_argument("-m", "--keep-multiline",
                        help="Don't strip multiline comments (/* ... */)",
                        action='store_true')
    parser.add_argument("-i", "--keep-inline",
                        help="Do not strip inline comments (// ...)",
                        action='store_true')
    parser.add_argument("-w", "--keep-newline",
                        help="Keep newline control characters",
                        action='store_true')
    args = parser.parse_args()
    return args


def minify(filename):
    with open(filename, 'r') as source:
        lines = source.readlines()

        lines = remove_blank_lines(lines)

        lines = remove_trailing_white_spaces(lines)
        print lines
        for line in lines:
           print line



def main():
    filename = ""
    filename = raw_input("Enter the file to minify : ")
    minify(filename)
    

if __name__ == "__main__":
    main()

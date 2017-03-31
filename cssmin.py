#!/usr/bin/env python2.7

import argparse
import sys

def remove_blank_lines(lines):
    for i,line in enumerate(lines):
        if line == "\n":
            lines.pop(i)
    return lines

def replace_tabs(lines):
    for line in lines:
        line.replace('\t', ' ')
    return lines

def remove_trailing_white_spaces(lines):
    stripped_lines = []
    for line in lines:
        line.strip(' ')
        stripped_lines.append(line)
    return stripped_lines



def minify(filename):
    with open(filename, 'r') as source:
        lines = source.readlines()

        lines = remove_blank_lines(lines)
        lines = replace_tabs(lines)
        lines = remove_trailing_white_spaces(lines)
        print lines
        for line in lines:
           print line
        destination = filename.strip(".c")+"_min.c"
        dest = open(destination, "w")
        dest.writelines(lines)




def main():
    filename = ""
    filename = raw_input("Enter the file to minify : ")
    minify(filename)
    

if __name__ == "__main__":
    main()

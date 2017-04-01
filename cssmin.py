#!/usr/bin/env python2.7

import argparse
import sys
import re


def remove_everything_between(subs1, subs2, line):
    regex = re.compile(subs1 + r'.*' + subs2)
    return regex.sub('', line)


def remove_everything_before(subs, line):
    regex = re.compile(r'.*' + subs)
    return regex.sub('', line)


def remove_everything_past(subs, line):
    regex = re.compile(subs + r'.*')
    return regex.sub('', line)



def remove_blank_lines(lines):
    replacedLines = []
    for i,line in enumerate(lines):
        if line != '\n':
            replacedLines.append(line)
    return replacedLines

def replace_tabs(lines):
    for line in lines:
        line.replace("\t", "da tab")
    return lines

def replace_tabs2(lines):
    replacedLines = []
    for line in lines:
        result = str()
        for c in line:
            if c == '\t':
                result += ' ';
            else:
                result += c
        replacedLines.append(result)
    return replacedLines

def remove_trailing_white_spaces(lines):
    stripped_lines = []
    for line in lines:
        line.strip(' ')
        stripped_lines.append(line)
    return stripped_lines


def remove_comments(lines):
    start, end = '/*', '*/'
    escaped_start, escaped_end = '/\*', '\*/'
    in_comment = False
    newlines = []
    for line in lines:
        if not in_comment:
            start_pos = line.find(start)
            if start_pos != -1:
                in_comment = True
                end_pos = line.find(end)
                # inline multiline comment
                if start_pos < end_pos:
                    line = remove_everything_between(escaped_start, escaped_end, line)
                    in_comment = False
                else:
                    line = remove_everything_past(escaped_start, line)
        else:
            end_pos = line.find(end)
            if end_pos != -1:
                line = remove_everything_before(escaped_end, line)
                in_comment = False
                start_pos = line.find(start)
                # start of another comment on the same line
                if start_pos != -1:
                    line = remove_everything_past(escaped_start, line)
                    in_comment = True
            else:
                line = ''
        newlines.append(line)
    return newlines



def minify(filename):
    with open(filename, 'r') as source:
        lines = source.readlines()
    print lines

    lines = remove_comments(lines)
    lines = remove_blank_lines(lines)
    lines = replace_tabs2(lines)
    lines = remove_trailing_white_spaces(lines)
    #lines = remove_blank_lines(lines)

    print lines

    destination = filename.replace(".css","_min.css")
    dest = open(destination, "w")
    dest.writelines(lines)




def main():
    filename = ""
    filename = raw_input("Enter the file to minify : ")
    minify(filename)
    

if __name__ == "__main__":
    main()

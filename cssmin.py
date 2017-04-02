#!/usr/bin/env python2.7

import Core





def minify(filename):
    with open(filename, 'r') as source:
        lines = source.readlines()
    print lines

    lines = Core.replace_tabs2(lines)
    lines = Core.remove_trailing_white_spaces(lines)
    lines = Core.remove_blank_lines(lines)
    lines = Core.remove_comments(lines)
    lines = Core.remove_blank_lines(lines)
    lines = Core.optimize_lines(lines)
    lines = Core.condense_lines(lines)
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

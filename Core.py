import re


in_property_set = False
has_data = False

def remove_everything_between(subs1, subs2, line):
    regex = re.compile(subs1 + r'.*' + subs2)
    return regex.sub('', line)


def remove_everything_before(subs, line):
    regex = re.compile(r'.*' + subs)
    return regex.sub('', line)


def remove_everything_past(subs, line):
    regex = re.compile(subs + r'.*')
    return regex.sub('', line)

def is_in_property_set():
    return in_property_set

def enter_property_set():
    global in_property_set
    in_property_set = True
    return

def exit_property_set():
    global in_property_set
    in_property_set = False
    return


def has_data():
    return has_data


def remove_blank_lines(lines):
    replacedLines = []
    for i,line in enumerate(lines):
        if line != '\n':
            replacedLines.append(line)
    return replacedLines

def replace_tabs(lines):
    for line in lines:
        line.replace("\t", " ")
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
    in_line = False
    for line in lines:
        result = str()
        in_line = False
        for c in line:
            if c == ' ' and in_line == True:
                result+=c
            if c != ' ':
                in_line = True
                result+=c
        stripped_lines.append(result)
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


def optimize_lines(lines):
    result = []

    for line in lines:
        line = re.sub(r'[ ]*[{]', "{", line)
        line = re.sub(r'[ ]*[}]', "}", line)
        line = re.sub(r'[ ]*[:]', ":", line)
        line = re.sub(r'[:][ ]*', ":", line)
        line = re.sub(r'[ ]*[;]$]', ";", line)
        line = re.sub(r'[ ]*[\n]$]', "\n", line)

        result.append(line)

    return result


def condense_lines(lines):
    final = []
    for line in lines:
        result = str()
        for c in line:
            if c != '\n':
                result+= c
        final.append(result)
    return final
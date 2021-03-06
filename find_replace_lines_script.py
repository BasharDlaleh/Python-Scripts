#! /usr/bin/env python3
import re
import sys
import os

if sys.platform == "win32":
    os.system('color')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
file = sys.argv[2]

if sys.argv[1] == "find":

    with open(file,'r') as ofile:
        content = ofile.read()
        pattern = re.compile(sys.argv[3], re.DOTALL)
        newline = re.compile(r'\n')

        iter = pattern.finditer(content)
        count = 0
        matches = list()

        for i in iter:
            count += 1
            start_line = len(newline.findall(content, 0, i.start()))+1
            matches.append({"line_number" : start_line, "instance" : count})
        
    with open(file,'r') as ofile:
        lines=ofile.readlines()
        for match in matches:
            x = match["line_number"]
            print(bcolors.WARNING + lines[x - 1] + bcolors.ENDC + bcolors.OKCYAN + "........ line " + str(match["line_number"]) + bcolors.ENDC)

elif sys.argv[1] == "replace":

    with open(file, 'r') as ofile:
        # read a list of lines into data
        data = ofile.readlines()

    # now change line
    newline = "\n"
    data[int(sys.argv[3]) - 1] = f"{sys.argv[4]}" + f"{ (newline if sys.argv[4] != '' else '') }"
    # and write everything back
    with open(file, 'w') as ofile:
        ofile.writelines( data )
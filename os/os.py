import os

# pwd
os.getcwd()

# cd
os.chdir('path')

# get output of any shell command:
import commands
commands.getstatusoutput('command')
# eg:
commands.getstatusoutput('ls -l')


#suboprocess module allows-
#run shell commands with python
#capture outputs/errors
#pipe data between processed
#run process in parallel

import subprocess

#runs list of all items in pwd
result = subprocess.run(['ls'], shell = True)
#returns returncode
print(result.returncode)

#systeminfo- get system informantion
result = subprocess.run(['uname -a'], shell = True)
print(result)


ping_result = subprocess.run(['ping www.google.com'], shell = True, stdout = subprocess.PIPE, text = True)
print(ping_result.stdout)

folder_result = subprocess.run(['mkdir hello'], shell = True)
print(folder_result.stdout)

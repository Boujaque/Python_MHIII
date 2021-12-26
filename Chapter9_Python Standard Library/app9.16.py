# 16 - Command-line Arguments
import sys



print(sys.argv) # return ['app9.16.py', '-a', '-b', '-c']
if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]    
    print("password", password)
#17-Running External Programs
import subprocess


# subprocess.call("dir", shell =True)
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen # old, legacy

completed = subprocess.run("dir",     #running a child process
                           shell=True,
                           capture_output =True,
                           text = True)                        
print("Type: ",type(completed))
print("args:", completed.args)
print("returncode:", completed.returncode)
print("stderr: ", completed.stderr)
print("stdout: ", completed.stdout)

completed = subprocess.run(["python","other.py"],
                       capture_output =True,
                       text = True)
print("Type: ",type(completed))
print("args:", completed.args)
print("returncode:", completed.returncode)
print("stderr: ", completed.stderr)
print("stdout: ", completed.stdout)

# for erro casses and handling errors

try:
    completed = subprocess.run(["ls", "-l"],
                        capture_output =True,
                        text = True,
                        check = True) #Throw asception of type CalledProces Error
    # print("args:", completed.args)
    # print("returncode:", completed.returncode)
    # print("stderr: ", completed.stderr)
    # print("stdout: ", completed.stdout)
except (subprocess.CalledProcessError, FileNotFoundError) as ex:
    print("Error: ", ex)    
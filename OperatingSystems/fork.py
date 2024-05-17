import os

x = 100
print(f"Before fork, x = {x}")

pid = os.fork()

if pid == 0:  # This is executed in the child process
    print(f"Child process, initail x = {x}")
    x = 200  # Modify the variable in the child process
    print(f"Child process, modified x = {x}")
else:  
    os.wait()  # Wait for the child process to finish
    print(f"Parent process, inital x = {x}")
    x = 300
    print(f"Parent process, modified x = {x}")
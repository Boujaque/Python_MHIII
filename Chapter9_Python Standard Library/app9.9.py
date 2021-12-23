# 9 - Working with Timestamps
import time

print(time.time())  # UNIX epoch time 1 January 1970


def send_emails():
    for i in range(10000000):
        pass


start = time.time()
print("Start:", start)
send_emails()
end = time.time()
print("End: ", end)
duration = end - start
print("duration: ", duration)

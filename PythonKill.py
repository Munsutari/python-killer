import signal
import psutil
import time
import sys
import os


# Fixes color issue in terminal
if sys.platform.lower() == "win32":
    os.system('color')

    # Set windows size if you want to just double click the file
    # os.system('mode 20,15')


PROCNAME = "python"

# Loop through all python processes
for proc in psutil.process_iter():
    if PROCNAME in proc.name() and proc.pid != os.getpid():
        print("\x1b[31m" + "Killing..." + "\x1b[37m", proc.pid)
        proc.terminate()


print("\x1b[32mDone\x1b[37m")

time.sleep(0.5)

quit()

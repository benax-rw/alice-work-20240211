import os
import time

timestamp = time.time()
cmd = "raspistill -o Desktop/taken_"+str(timestamp)+".jpg -rot 180"
while  True:
    out = os.system(cmd)
    time.sleep(10)

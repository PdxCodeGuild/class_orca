import time
time_start = time.time()
time.sleep(5)
if round(time.time()-time_start) >= 5:
    print(':)')
elif round(time.time()-time_start) < 5:
    print(':(')
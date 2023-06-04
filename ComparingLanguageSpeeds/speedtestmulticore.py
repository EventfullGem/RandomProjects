import multiprocessing
import time

def worker():
    # worker function
    # function that prints a message and a
    print('Worker')
    x = 0
    while x < 1000:
        print(x)
        x += 1
    return
# Create 50 processes and start them
if __name__ == '__main__':
    start_time = time.time()
    jobs = []
    for i in range(50):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
# Wait for all processes to finish
    for job in jobs:
        job.join()

    end_time = time.time()
# Calculate the time taken and outputs to console window
    print("Time taken:", end_time - start_time, "seconds")

# End Data:
# Raspberry Pi 4B 8GB: 0.000000000
# My computer (i7-10750H @ 2.60GHz): 0.000000000
# My Server (Xeon E5-645 v5 @ 2.40GHz): 0.000000000

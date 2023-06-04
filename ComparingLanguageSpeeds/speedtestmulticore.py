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
# Raspberry Pi 4B 8GB (Ubuntu 22.04): 1.0884602069854736 seconds
# My computer with i7-10750H @ 2.60GHz (Windows 10 Home): 12.872420072555542 seconds
# My Server with Xeon E5-645 v5 @ 2.40GHz (Ubuntu 22.04): 0.22396469116210938 seconds

# Conclusion: Must be something with Windows that makes it slower.

# Second test: My computer with IntelliJ Ultimate: 3.63745379447937 seconds
# Second test: My computer but with WSL2 (Ubuntu 22.04): 0.1212620735168457 seconds

# Second conclusion: Ubuntu 22.04 is better at handling multi core code than Windows 10 home
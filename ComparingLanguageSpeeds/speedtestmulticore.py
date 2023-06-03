import multiprocessing
import time

start_time = time.time()

def worker():
    # worker function
    print('Worker')
    x = 0
    while x < 1000:
        print(x)
        x += 1
    return

if __name__ == '__main__':
    jobs = []
    for i in range(50):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()


end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")
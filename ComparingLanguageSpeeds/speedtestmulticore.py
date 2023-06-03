import multiprocessing

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
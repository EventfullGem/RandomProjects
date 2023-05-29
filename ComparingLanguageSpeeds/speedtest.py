import time

start_time = time.time()

for i in range(1000000):
    print(i)

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")

#Time taken: 48.79 seconds
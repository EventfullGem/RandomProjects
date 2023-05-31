import time

start_time = time.time()

for i in range(1000000):
    print(i)

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")

# Time taken: 48.79 seconds
# So when I run it in Visual Studio IDE and not Visual studio Code I get 7 seconds???
# When I run it in Intellij IDEA I get 21.91 seconds
# I don't know what im doing anymore

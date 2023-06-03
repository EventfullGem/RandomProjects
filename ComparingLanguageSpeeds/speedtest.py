import time

start_time = time.time()

for i in range(1000000000):
    print(i)

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")

# Time taken: 48.79 seconds
# So when I run it in Visual Studio IDE and not Visual studio Code I get 7 seconds???
# When I run it in JetBrains IDE I get 4.48 seconds?
# ran on my server I get ... 4.49 seconds
# I don't know what im doing anymore


# My server can count to one billion in about ... didnt finish, I'm trying to test multi core support for python now
#  Prompts user for input 
userinput = input("Input: ")
# Check if there is anything but a number in the input
if userinput.isnumeric() == False:
    # If there is, remove the letters and symbols and keep only the numbers
    userinput = userinput.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{};:"|,./<>?`~'})
# Translates string to integer
userinput = int(userinput)

# Prints the user input as just numbers
print("Output:", userinput)

# Why is this useful?
# Some people mistype and its annoying when the entire command fails because of that, so you could either make them reinput the numbers or just strip the text of all non-numbers
# Ex: Instead of pressing enter they also press "\" at the same time 
# Like 12\ [enter]
# Instead of crashing or giving an error, the program will just use "12"
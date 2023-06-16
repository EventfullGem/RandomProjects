
# Farenheit from Celsius
# f=c*1.8+32
# Celsius from Farenheit
# c=(f-32)/1.8

# create a prompt to input a celcius degree 
celcius = input("Enter a degree in Celcius: ")
# Check if there is anything but a number in the input
if celcius.isnumeric() == False:
    # If there is, remove the letters and symbols and keep only the numbers
    celcius = celcius.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{};:"|,./<>?`~'})
celcius = int(celcius)

farenheit = celcius*1.8+32

print("The temperature in Ferenheit is: ", farenheit)
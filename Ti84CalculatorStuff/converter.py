
#Only works on Linux I think, I still need to test this



#This code converts Ti-Basic to Python
#This code is not perfect, but it works
from ti842py import transpile

transpile("clock.txt", "tiprogram.py")
#clock.txt is the Ti-Basic (input) program
#tiprogram.py is the Python (output) program



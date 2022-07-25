import os
import time
 
if os.name == "posix":
   var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"
 
os.system(var)
 
print("")
print(" Ö ")
 
time.sleep(0.5)
os.system(var)
 
print("")
print(" OÖ ")
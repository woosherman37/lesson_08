#these are build-in libraries
import platform
import sys


#these libraries need to be downloaded
import pandas as pd
import matplotlib.pyplot as plt




python_version = platform.python_version()

if python_version == "3.10.6" :
	print(f"I am using Python Version {python_version}")

else:
	print(f"I am using another Python Version {python_version}")
	sys.exit()

dictionary = {"tom":[3,13], "sher":[3, 7], "bobo":[7, 8]}

print(pd.DataFrame(dictionary))




plt.plot([1,2,3,4])
plt.ylabel("sherman")
plt.show()

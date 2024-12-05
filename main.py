import platform
import pandas as pd





python_version = platform.python_version()

if python_version == "3.10.6" :
	print(f"I am using Python Version {python_version}")

else:
	print(f"I am using another Python Version {python_version}")


dictionary = {"tom":[3,13], "sher":[3, 7], "bobo":[7, 8]}

print(pd.DataFrame(dictionary))








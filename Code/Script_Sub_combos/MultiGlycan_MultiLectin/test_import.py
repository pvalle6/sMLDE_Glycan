from numpy import loadtxt

filepath = R"C:\Users\valle\Downloads\import.csv"
lines = loadtxt(filepath, dtype=str)

for i in lines:
	
	print(i)
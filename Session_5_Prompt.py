import numpy as np
from tabulate import tabulate

def main():
	two_pi = np.pi*2
	x = np.linspace(0.0,two_pi,1000)

	y = np.sin(x)

	table_data = [(a,b) for a,b in zip(x,y)]
	table_headers = ['x', 'sin(x)']
	print(tabulate(table_data,tablefmt="grid",headers=table_headers,floatfmt=".3f"))

if __name__=="__main__":
	main()
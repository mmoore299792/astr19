import numpy as np 
from tabulate import tabulate
from astropy.table import Table

pi_value = np.pi
x = np.linspace(0.0,2.0*pi_value,1000)
y = np.sin(x)

table_data = [(a,b) for a,b in zip(x,y)]
table_headers = ["x","sin(x)"]
python_table = tabulate(table_data, tablefmt="grid", headers=table_headers,
        floatfmt=".3f")

astropy_table = Table()
astropy_table["x"] = x
astropy_table["y"] = y

astropy_table["x"].format = "{:.3f}"
astropy_table["y"].format = "{:.3f}"

def main():
    print(python_table)
    print(astropy_table)

if __name__=='__main__':
    main()
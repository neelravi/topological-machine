from ase.io import read


data, atoms = read("mp-1000.cif", index=0, format="cif", parallel=False)
print (data) 



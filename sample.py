from pymatgen.ext.matproj import MPRester

with MPRester("IOa0xKupz6Ev2lHs") as m:

    # Get all energies of materials with formula "*2O".
#    results = m.query("SnSb", ['energy'], ['spacegroup.symbol'])

    results=m.query(criteria={"elements":  {"$all": ["Sb", "Sn"]}} , properties=["spacegroup.symbol"])
    
    print(results)
    # Get the formulas and energies of materials with materials_id mp-1234
#    # or with formula FeO.
#    results = m.query("FeO mp-1234", ['pretty_formula', 'energy'])
#    print(results)
#    # Get all compounds of the form ABO3
#    results = m.query("**O3", ['pretty_formula', 'energy'])

from pymatgen.ext.matproj import MPRester
from pymatgen.io.cif import CifWriter as cifwriter

basic_properties = ['task_id','pretty_formula','reduced_cell_formula','unit_cell_formula','spacegroup.number','energy','formation_energy_per_atom','density']
electronic_properties = ['band_gap','efermi','total_magnetization']
all_properties = basic_properties + electronic_properties
triclinic     = [2]
monoclinic    = list(range(10, 16))
orthorhombic  = list(range(47, 75))	
tetragonal    = list(range(83, 89))   + list(range(123, 143))		
triagonal     = list(range(147, 149)) + list(range(162, 168))			
hexagonal     = list(range(175, 177)) + list(range(191, 195))				
cubic         = list(range(200, 207)) + list(range(221, 231))					
spacegroup_with_inversion = triclinic + monoclinic + orthorhombic + tetragonal + triagonal + hexagonal + cubic
#criteria = { "spacegroup.number":  {"$in" : spacegroup_with_inversion}, "band_gap": {"$gte": 0.3}, 'nelements': {"$lte": 2}}

with MPRester("IOa0xKupz6Ev2lHs") as m:
	results = m.query({"spacegroup.number": {"$in": spacegroup_with_inversion}, "band_gap": {"$gte": 0.3}, 'nelements': {"$lte": 2}}, properties=['task_id'])
	
#for i in range(len(results)):
for i in range(10):	
	filename = (results[i]['task_id']) + ".cif"
	print (filename)
	structure = m.get_structure_by_material_id(results[i]['task_id'])
	cifwriter.write_file(structure, filename)

from mkutils.gromacs_writer import FFWriter
import json, os

ff_file = 'cc_parameters.json'
outfile = 'ffnonbonded.itp'

if not os.path.isfile(ff_file):
    with open(ff_file, 'w') as f:
        _dict = {'atomtypes': {}, 'crossints': {}}       
        json.dump(_dict, f)

ff = FFWriter(ff_file)

# Write atomtypes
# at_name, l_r, l_a, eps(K), sig(nm), MW(g/mol), proton_nr(unused)
ff.add_cgw_ift(298.15)
ff.add_atomtype('W2', 8., 6., 400., 0.37467, 36.03056, 20)
ff.add_atomtype('CT', 15.947, 6., 358.37, 0.45012, 43.08698, 25)
ff.add_atomtype('CM', 16.433, 6., 377.14, 0.4184, 42.07914, 24)


# Write crossinteractions
# Crossints can be specified with k_ij and directly specifiying in
# Kelving
ff.add_crossint('W', 'CT', k=0.31)
ff.add_crossint('W', 'CM', k=0.34)
ff.add_crossint('CT', 'CM', eps_mix=345.72)

ff.add_crossint('W2', 'CT', k=0.32)
ff.add_crossint('W2', 'CM', k=0.33)

ff.write_tables(shift=True, cutoff=2.0)
ff.write_forcefield(outfile='ffnonbonded.itp')

ff.add_cgw_ift(303.15, update=True)
ff.write_forcefield(outfile='ffnonbonded_30C.itp')


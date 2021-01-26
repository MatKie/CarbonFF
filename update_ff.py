# +
from mkutils.gromacs_writer import FFWriter
import json, os

ff_file = 'cc_parameters.json'
# -

ff = FFWriter(ff_file)

# Update Crossints
ff.add_crossint('Wift25', 'CT', k=0.25, update=True)
ff.add_crossint('Wift25', 'CM', k=0.25, update=True)

# No need to write tables again, because l_r, l_a did not change
#ff.write_tables(shift=True, cutoff=2.0)
ff.write_forcefield(outfile='ffnonbonded_v1.itp')

# Further update crossints
ff.add_crossint('Wift25', 'CT', k=0.4, update=True)
ff.add_crossint('Wift25', 'CM', k=0.4, update=True)

# No need to write tables again, because l_r, l_a did not change
#ff.write_tables(shift=True, cutoff=2.0)
ff.write_forcefield(outfile='ffnonbonded_v2.itp')


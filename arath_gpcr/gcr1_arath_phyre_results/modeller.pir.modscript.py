from modeller import * 
from modeller.automodel import * 
log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in
env.io.atom_files_directory = './:../atom_files'
a = automodel(env,
              alnfile  = 'modeller.pir',
              knowns   = ('c2rh1A_', 'c3pdsA_', 'c3emlA_', 'c3rzeA_', 'c3uonA_', 'c4djhA_', 'PoingAA', ),
              sequence = 'query')
a.starting_model= 1
a.ending_model  = 1
a.make()

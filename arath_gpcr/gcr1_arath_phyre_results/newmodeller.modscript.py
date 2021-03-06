from modeller import * 
from modeller.automodel import * 
log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in
env.io.atom_files_directory = './:../atom_files'
a = automodel(env,
              alnfile  = 'newmodeller.pir',
              knowns   = ('c3rzeA_','c2rh1A_','c3emlA_','c4djhA_','c3uonA_','c3pdsA_','PoingAA', ),
              sequence = 'query')
a.starting_model= 1
a.ending_model  = 1
a.make()

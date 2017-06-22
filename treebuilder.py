# This is the notebook where you can customize data path and the treemakers you want to use
# If you want to use custom treemakers, do not forget to import them. 
# In this case the .py-files of the custom treemakers are situated in /home/wittweg/treemakers

import sys
import hax

sys.path.append('/home/wittweg/treemakers/')
from s2_top_bottom_new import S2TopBottom # PAX 6.4.2 correction
from s2_correct_in_hax import S2CorrectInHax # PAX 6.6.4 correction


run = int(sys.argv[1])

hax.__version__
hax.init(main_data_paths=['/project/lgrandi/xenon1t/processed/pax_v6.6.5', '/project2/lgrandi/xenon1t/processed/pax_v6.6.5'],
         minitree_paths = ['./'],
         pax_version_policy = '6.6.5') # only use for version problems

#hax.minitrees.load(run, [S2TopBottom, S2CorrectInHax, 'Basics', 'Extended'])
hax.minitrees.load(run, ['Fundamentals','Basics','Extended'])

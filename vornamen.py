# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:50:52 2020

@author: netzer
"""

import csv
from pathlib import Path
from pprint import pprint


############## source path to csv files ##########################

year = '2012'

############## source path to csv files ##########################

# p = Path(sourcepath)

# dirs = [x for x in p.iterdir() if x.is_dir()]

# files = []   
# for d in dirs:
#     for f in d.iterdir():
#         if f.name.endswith(('csv')):
#             files.append(f.name)

# pprint(sorted(files))

import os
import glob
import pandas as pd
import gc

sourcepath = "D:\Tableau\VornamenBerlin\data\cleaned"
sourceyear = os.path.join(sourcepath,year)

os.chdir(sourceyear)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv(year + ".csv",
                    index=False,
                    encoding='utf-8-sig')
gc.collect()



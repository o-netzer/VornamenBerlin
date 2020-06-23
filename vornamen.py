# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:50:52 2020

@author: netzer
"""


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
os.chdir(sourcepath)
combined_years = 'union_2012-2019'
if not os.path.exists(os.path.join(sourcepath,combined_years)):
    os.mkdir(os.path.join(sourcepath,combined_years))


sourceyear = os.path.join(sourcepath,year)


os.chdir(sourceyear)


extension = 'csv'
combined_csv = pd.DataFrame()
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
for file in all_filenames:
    df = pd.read_csv(file,
                header=0,
                names = ['Vorname', 'Anzahl', 'Geschlecht']) # + Position ab 2017
    df['Jahr']=year
    df['Bezirk']=file
    
    combined_csv = combined_csv.append(df)
    
os.chdir(os.path.join(sourcepath,combined_years))

combined_csv.to_csv(year + ".csv",
                index=False,
                encoding='utf-8-sig')





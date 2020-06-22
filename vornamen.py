# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:50:52 2020

@author: netzer
"""

import csv
from pathlib import Path
from pprint import pprint


sourcepath = r"D:\PythonScripts20\haeufige-vornamen-berlin\haeufige-vornamen-berlin\data\source"

p = Path(sourcepath)

dirs = [x for x in p.iterdir() if x.is_dir()]

files = []   
for d in dirs:
    for f in d.iterdir():
        if f.name.endswith(('csv')):
            files.append(f.name)

pprint(sorted(files))
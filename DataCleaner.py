#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:34:22 2020

@author: sameenahmedashraf
"""

import GlassdoorScraper as gs
import pandas as pd
path= "/Users/sameenahmedashraf/OneDrive - The University of Texas at Dallas/Projects/GlassdoorSeliumScraper/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15 )

df.to_csv('glassdoor_dsjobs.csv', index=False)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe                          

data_files=["db_def.csv"]
includes = ["wx","cairo","encodings", "encodings.*"]
options = {"py2exe":{"includes":includes,"bundle_files": 1}}


setup(     
    version = "1.0", 
    description = "Scada Tool", 
    name = "Scada  Tool", 
    options = options, 
    zipfile=None,
    
    windows=["scada_tool.py"]
    )

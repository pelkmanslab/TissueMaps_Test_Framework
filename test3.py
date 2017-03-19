# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:55:56 2017

@author: saadiaiftikhar
"""

'''
Integration testing framework of the tissuemaps on sample datasets.
Images are provided by the different users in Pelkmans lab. Results are
compared versus expected outcome.
'''

import os
from flask import jsonify
import glob
import time
#import re
from scripttest import TestFileEnvironment
import shutil
#from tmclient.api import tmclient
from tmclient.api import TmClient
import unittest
import yaml

host = '172.23.102.218'
#host='localhost'
port='80'
#port = 8002
username = 'test'
password = '123456'

ROOT = '/home/ubuntu/'
MOCK_PATH = os.path.join(ROOT, 'mock')
test_data_path = "/home/ubuntu/testData/20170307_NUPReplicate_C22/"
test_data_main = "/home/ubuntu/testData/"
project_name = 'testData'
workflow_filename = "/home/ubuntu/testData/workflow_description.yml"
actual_experiment_data = "tissuemaps@172.23.102.218:home/ubuntu/storage/tissuemaps/data/experiment_3/workflow/"
ImageAnalysis_pipeline = os.path.join(MOCK_PATH, 'pipeline.yaml')
project_path = os.path.join(ROOT, project_name)
TIFF_FILES = test_data_path
handles_path = os.path.join(project_path, 'handles')
handles = glob.glob(os.path.join(handles_path, '*.*'))

client = TmClient

workflow_type = 'canonical'
microscope_type = 'cellvoyager'
plate_format = 384
plate_acquisition_mode = 'basic'
description = "test plate"
experiment_name = '2D'
-- INSERT --                                                                                                                                                                              1,1           Top

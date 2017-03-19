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
#actual_experiment_data = "tissuemaps@172.23.102.218:home/ubuntu/storage/tissuemaps/data/experiment_3/workflow/"
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
plate_name = 'plate1'
acq_name = 'acq1'
data_directory = 'test_data_path'

def test_workflow():

    client = TmClient(host,port,experiment_name,username,password)
    time.sleep(5) # delays for 5 seconds
    client.create_experiment(workflow_type, microscope_type,
                                    plate_format, plate_acquisition_mode)
    time.sleep(120) # delays for 120 seconds

    client.create_plate(plate_name, description='')
    time.sleep(120) # delays for 120 seconds

    client.create_acquisition(plate_name, acq_name, description='')
    time.sleep(120) # delays for 120 seconds

    client.get_microscope_files(plate_name, acq_name)
    time.sleep(60) # delays for 60 seconds

    for i in range(10):
        client.upload_microscope_files(plate_name, acq_name, test_data_path)

    time.sleep(30) # delays for 30 seconds

    client.upload_workflow_description_file(workflow_filename)
    
    time.sleep(60) # delays for 60 seconds

    client.upload_jterator_project_description_files(test_data_main)
    time.sleep(60) # delays for 60 seconds

    client.submit_workflow(description=None)

    time.sleep(1200) # delays for 1200 seconds

    client.download_object_feature_values('Cells',
            plate_name=None, well_name=None, well_pos_y=None, well_pos_x=None,
            tpoint=None)



test_workflow()

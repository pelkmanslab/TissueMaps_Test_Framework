# -*- coding: utf-8 -*-
"""
Created on Tues Mar 28 18:55:56 2017

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

host = '172.23.103.166'
port='80'
username = 'test'
password = '123456'

ROOT = '/home/ubuntu/'
MOCK_PATH = os.path.join(ROOT, 'mock')
test_data_path1 = "/home/ubuntu/Andy_Multiplex_Test_Data/cycle02/"
test_data_path2 = "/home/ubuntu/Andy_Multiplex_Test_Data/cycle03/"
test_data_path3 = "/home/ubuntu/Andy_Multiplex_Test_Data/cycle04/"
test_data_main = "/home/ubuntu/Andy_Multiplex_Test_Data/"
project_name = 'Andy_Multiplex_Test_Data'
workflow_filename = "/home/ubuntu/Andy_Multiplex_Test_Data/workflow_description.yml"
ImageAnalysis_pipeline = os.path.join(MOCK_PATH, 'pipeline.yaml')
project_path = os.path.join(ROOT, project_name)
TIFF_FILES = test_data_path1
handles_path = os.path.join(project_path, 'handles')
handles = glob.glob(os.path.join(handles_path, '*.*'))

client = TmClient

workflow_type = 'multiplexing'
microscope_type = 'cellvoyager'
plate_format = 384
plate_acquisition_mode = 'multiplexing'
description = "test multiplexing plate"
experiment_name = 'Andy_Multiplexing_Test_Automated1'
plate_name = 'plate1'
acq_name1 = 'cycle2'
acq_name2 = 'cycle3'
acq_name3 = 'cycle4'
data_directory1 = 'test_data_path1'
data_directory2 = 'test_data_path2'
data_directory3 = 'test_data_path3'

def test_workflow():

    client = TmClient(host,port,experiment_name,username,password)
    time.sleep(5) # delays for 5 seconds
    client.create_experiment(workflow_type, microscope_type,
                                    plate_format, plate_acquisition_mode)
    time.sleep(120) # delays for 120 seconds

    client.create_plate(plate_name, description='')
    time.sleep(120) # delays for 120 seconds

    client.create_acquisition(plate_name, acq_name1, description='')
    time.sleep(120) # delays for 120 seconds

    client.get_microscope_files(plate_name, acq_name1)
    time.sleep(60) # delays for 60 seconds

    for i in range(5):
        client.upload_microscope_files(plate_name, acq_name1, test_data_path1)

    time.sleep(30) # delays for 30 seconds
    
    client.create_acquisition(plate_name, acq_name2, description='')
    time.sleep(120) # delays for 120 seconds

    client.get_microscope_files(plate_name, acq_name2)
    time.sleep(60) # delays for 60 seconds

    for i in range(5):
        client.upload_microscope_files(plate_name, acq_name2, test_data_path2)

    time.sleep(60) # delays for 30 seconds
    
    client.create_acquisition(plate_name, acq_name3, description='')
    time.sleep(120) # delays for 120 seconds

    client.get_microscope_files(plate_name, acq_name3)
    time.sleep(60) # delays for 60 seconds

    for i in range(5):
        client.upload_microscope_files(plate_name, acq_name3, test_data_path3)

    time.sleep(60) # delays for 30 seconds

    client.upload_workflow_description_file(workflow_filename)
    
    time.sleep(60) # delays for 60 seconds

    client.upload_jterator_project_description_files(test_data_main)
    time.sleep(60) # delays for 60 seconds

    client.submit_workflow(description=None)

    time.sleep(1200) # delays for 1200 seconds

    client.download_object_feature_values('cells',
            plate_name=None, well_name=None, well_pos_y=None, well_pos_x=None,
            tpoint=None)



test_workflow()


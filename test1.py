# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:14:14 2017

@author: saadiaiftikhar
"""


'''
Integration testing framework of the tissuemaps on sample datasets.
Images are provided by the different users in Pelkmans lab. Results are
compared versus expected outcome.
'''

import os
import glob
import time
#import re
from scripttest import TestFileEnvironment
import shutil
#from tmclient.api import tmclient
from tmclient.api import TmClient
import unittest

#host = '172.23.102.218'
host='localhost'
port=1111
#port = 8002
username = 'test'
password = 123456

ROOT = '/home/ubuntu/'
MOCK_PATH = os.path.join(ROOT, 'mock')
test_data_path = "/home/ubuntu/testData/20170307_NUPReplicate_C22/"
project_name = 'testData'
workflow_filename = "/home/ubuntu/testData/workflow_description.yml"
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
experiment_name = 'experiment_test_2D'
plate_name = 'plate1'
acq_name = 'acq1'
data_directory = 'test_data_path'

client = TmClient(host,port,experiment_name,username,password)
client.creat_experiment(workflow_type, microscope_type, 
                                   plate_format, plate_acquisition_mode)
    
#def main():
#        
#        '''
#        Initialize the tm test framework with experiment description.
#        '''
#        
#        # super(TMsTestFramework,self).__init__(self)
#        
#        workflow_type = 'canonical'
#        microscope_type = 'cellvoyager'
#        plate_format = 384
#        plate_acquisition_mode = 'basic'
#        description = "test plate"
#        experiment_name = 'experiment_test_2D'
#        plate_name = 'plate1'
#        acq_name = 'acq1'
#        data_directory = 'test_data_path'
#        
#
#        TmClient.create_experiment(workflow_type, microscope_type, 
#                                    plate_format, plate_acquisition_mode)
#
#
#client = TmClient
#if __name__ == "__main__":
#    main()

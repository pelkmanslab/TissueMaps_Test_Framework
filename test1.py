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

host = '172.23.102.218'
port = 8002
username = 'test'
password = 123456

ROOT = os.path.dirname(__file__)
MOCK_PATH = os.path.join(ROOT, 'mock')
test_data_path = "/home/ubuntu/testData/20170307_NUPReplicate_C22/"
project_name = 'testData'
workflow_filename = "/home/ubuntu/testData/workflow_description.yml"
ImageAnalysis_pipeline = os.path.join(MOCK_PATH, 'pipeline.yaml')
project_path = os.path.join(ROOT, project_name)
TIFF_FILES = list(glob.glob(test_data_path/'*.tif'))
handles_path = os.path.join(project_path, 'handles')
handles = list(glob.glob(handles_path/'*.*'))

client = TmClient

#workflow_type = 'canonical'
#microscope_type = 'cellvoyager'
#plate_format = 384
#plate_acquisition_mode = 'basic'
#description = "test plate"
#experiment_name = 'experiment_test_2D'
#plate_name = 'plate1'
#acq_name = 'acq1'
#data_directory = 'test_data_path'

def main(self,host,port,username,password):
        
        '''
        Initialize the tm test framework with experiment description.
        '''
        
        # super(TMsTestFramework,self).__init__(self)
        
        self.workflow_type = 'canonical'
        self.microscope_type = 'cellvoyager'
        self.plate_format = 384
        self.plate_acquisition_mode = 'basic'
        self.description = "test plate"
        self.experiment_name = 'experiment_test_2D'
        self.plate_name = 'plate1'
        self.acq_name = 'acq1'
        self.data_directory = 'test_data_path'
        

        TmClient.create_experiment(self.workflow_type, self.microscope_type, 
                                    self.plate_format, self.plate_acquisition_mode)


main()

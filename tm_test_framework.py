#!/usr/bin/env python

"""
Created on Tue Mar 14 16:30:36 2017

@author: Saadia Iftikhar, saadia.iftikhar@fmi.ch

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
from tmclient import api

import unittest

host = '172.23.102.218'
port = 8002
username = 'test'
password = 123456

ROOT = os.path.dirname(__file__)
MOCK_PATH = os.path.join(ROOT, 'mock')
test_data_path = "/home/ubuntu/testData"
project_name = 'testData'
workflow_filename = "/home/ubuntu/testData/workflow_description.yml"
ImageAnalysis_pipeline = os.path.join(MOCK_PATH, 'pipeline.yaml')
project_path = os.path.join(ROOT, project_name)
TIFF_FILES = list(glob.glob(test_data_path/'*.tif'))
handles_path = os.path.join(project_path, 'handles')
handles = list(glob.glob(handles_path/'*.*'))

client = api.TmCleint()

class TMsTestFramework(unittest.TestCase):
    
    def __init__(self,host,port,username,password):
        
        '''
        Initialize the tm test framework with experiment description.
        '''
        
        super(TMsTestFramework,self).__init__(host,port,username,password)
        
        self.workflow_type = 'canonical'
        self.microscope_type = 'cellvoyager'
        self.plate_format = 384
        self.plate_acquisition_mode = 'basic'
        self.description = "test plate"
        self.experiment_name = 'experiment_test_2D'
        self.plate_name = 'plate1'
        self.acq_name = 'acq1'
        self.data_directory = 'test_data_path'
        
    
    def age_file(self,filepath, aging=600):
        
        '''Make last modification and access time of the file look older.
        '''
        
        aging = int(aging)
        current_time = int(time.time())
        new_time = current_time - aging
        os.utime(filepath, (new_time, new_time))
        assert current_time - os.path.getmtime(filepath) >= aging
        
    def copy_config_files(self):
        
        '''Copy yaml files into the project folder, eg. expectation.yml.
        '''
        
        shutil.copy(workflow_filename, project_path)
        shutil.copy(ImageAnalysis_pipeline, project_path)
        shutil.copy(handles, handles_path)    
    
    
    def main(self):
        
        '''Test the different stages of tissuemaps framework.
        '''
        
        # create a test environment 
        
        self.age_file(self,TIFF_FILES)
        
        basepath = '/tmp/test'
        t = TestFileEnvironment(basepath, start_clear=False)
        
        # create an experiment in tissuemaps 
        
        result = t.run(
                    client.create_experiment(self, self.workflow_type,
                                             self.microscope_type, 
                                             self.plate_format,
                                             self.plate_acquisition_mode)
                    .format(p=project_path),expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        # create a plate in experiment
            
        result = t.run(
                    client.create_plate(self, self.plate_name, description='')
                    .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        # create an acquisition in plate
        
        result = t.run(
            client.create_acquisition(self,self.plate_name,
                                      self.acq_name,description='')
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        # get the list of microscope files
        
        result = t.run(
            client.get_microscope_files(self, self.plate_name, self.acq_name)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        # upload the microscope files in the experiment  
        
        result = t.run(
            client.upload_microscope_files(self,self.plate_name, 
                                            self.acq_name,self.data_directory)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
#        result = t.run(
#            self.copy_config_files(self)
#            .format(p=project_path),
#                    expect_stderr=True)
#        self.assertEqual(result.returncode, 0)
        
        # copy workflow description file into the experiment
        
        result = t.run(
            client.upload_workflow_description(self,workflow_filename)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        # submit the workflow
        
        result = t.run(
            client.submit_workflow(self, description=None)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        # get the status of the workflow 
        
        result = t.run(
            client.get_workflow_status(self, depth=2)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)

        # download the feature values
        
#        result = t.run(
#            client.download_feature_values(self, mapobject_type_name)
#            .format(p=project_path),
#                    expect_stderr=True)
#        self.assertEqual(result.returncode, 0)
        
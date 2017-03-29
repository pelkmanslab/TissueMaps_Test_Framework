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
from scripttest import TestFileEnvironment
import shutil
import unittest
from scripttest import TestFileEnvironment
from tmclient.api import TmClient
import unittest


host = '172.23.102.218'
port='80'
username = 'test'
password = '123456'

ROOT = '/home/ubuntu/'
MOCK_PATH = os.path.join(ROOT, 'mock')
test_data_path = "/home/ubuntu/testData/20170307_NUPReplicate_C22/"
test_data_main = "/home/ubuntu/testData/"
project_name = 'testData'
workflow_filename = "/home/ubuntu/testData/workflow_description.yml"
ImageAnalysis_pipeline = os.path.join(MOCK_PATH, 'pipeline.yaml')
project_path = os.path.join(ROOT, project_name)
TIFF_FILES = test_data_path
handles_path = os.path.join(project_path, 'handles')
handles = glob.glob(os.path.join(handles_path, '*.*'))

workflow_type = 'canonical'
microscope_type = 'cellvoyager'
plate_format = 384
plate_acquisition_mode = 'basic'
description = "test plate"
experiment_name = '2D'
plate_name = 'plate1'
acq_name = 'acq1'
data_directory = 'test_data_path'


class TMsTestFramework(unittest.TestCase):
    
    def __init__(self):
        
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
                
    
    
    def test_workflow(self):
        
        '''Test the different stages of tissuemaps framework.
        '''
        
        # create a test environment     
        
        basepath = '/tmp/test'
        t = TestFileEnvironment(basepath, start_clear=False)
        
        client = TmClient(host,port,experiment_name,username,password)
        time.sleep(5) # delays for 5 seconds
        
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        
        
        # create an experiment in tissuemaps 
        
        client.create_experiment(workflow_type, microscope_type,
                                        plate_format, plate_acquisition_mode)
        time.sleep(120) # delays for 120 seconds
        
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        
        # create a plate in experiment
            
        client.create_plate(plate_name, description='')
        time.sleep(120) # delays for 120 seconds
        
         # get the status of the workflow 
        
        result = t.run(client.get_workflow_status(self, depth=2))        
        self.assertEqual(result.returncode, 0)
        
        # create an acquisition in plate
        
        client.create_acquisition(plate_name, acq_name, description='')
        time.sleep(120) # delays for 120 seconds
        
         # get the status of the workflow  
        
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        
        # get the list of microscope files
        
        client.get_microscope_files(plate_name, acq_name)
        time.sleep(60) # delays for 60 seconds
        
         # get the status of the workflow  
        
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        
        # upload the microscope files in the experiment  
        
        for i in range(10):
            client.upload_microscope_files(plate_name, acq_name, test_data_path)
    
        time.sleep(30) # delays for 30 seconds
        
         # get the status of the workflow 
        
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        
        # upload workflow description file into the experiment
        
        client.upload_workflow_description_file(workflow_filename)
        time.sleep(60) # delays for 60 seconds

         # get the status of the workflow   
      
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        
        # upload the jterator pipeline 
        
        client.upload_jterator_project_description_files(test_data_main)
        time.sleep(60) # delays for 60 seconds

         # get the status of the workflow  
       
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        
        # submit the workflow
        
        client.submit_workflow(description=None)
        time.sleep(1200) # delays for 1200 seconds
        
        # get the status of the workflow 
        
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        

        # download the feature values
        
        client.download_object_feature_values('Cells',
                plate_name=None, well_name=None, well_pos_y=None
                , well_pos_x=None, tpoint=None)
        
         # get the status of the workflow 
        
        result = t.run(client.get_workflow_status(self, depth=2))
        self.assertEqual(result.returncode, 0)
        

if __name__=='__main__':
    
    
    tm_test_framwork = TMsTestFramework()
    
   # client = TmClient(host,port,experiment_name,username,password)
   # client.creat_experiment(workflow_type, microscope_type, 
    #                               plate_format, plate_acquisition_mode)
    
#    tm_test = TMsTestFramework()
#    init_test = tm_test.__init__
#    
#    TMsTestFramework.__init__
#    TMsTestFramework.test_workflow()
    
    
#TM_Test = TMsTestFramework(host,port,username,password)
#TMsTestFramework.__init__
#TMsTestFramework.main(TM_Test)
   
#

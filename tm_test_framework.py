#!/usr/bin/env python

"""
Created on Tue Mar 14 16:30:36 2017

@author: saadiaiftikhar
"""


'''
Integration testing framework of the tissuemaps on sample datasets.
Images are provided by the different users in Pelkmans lab. Results are
compared versus expected outcome.
'''

import os
import time
import re
from scripttest import TestFileEnvironment
import shutil
from tmclient.api import tmclient
import unittest

ROOT = os.path.dirname(__file__)
MOCK_PATH = os.path.join(ROOT, 'mock')
Project_Description_pipeline = 'expectation.yaml'
ImageAnalysis_pipeline = os.path.join(MOCK_PATH, 'pipeline.yaml')
project_path = ''
TIFF_FILES = 'http://testdata.tissuemaps.org/storage/' \
           'experiment1/'

class TMsTestFramework(unittest.TestCase):
    
    def age_file(self,filepath, aging=600):
        '''Make last modification and access time of the file look older.'''
        aging = int(aging)
        current_time = int(time.time())
        new_time = current_time - aging
        os.utime(filepath, (new_time, new_time))
        assert current_time - os.path.getmtime(filepath) >= aging

#    def install_tmset(self):
#        '''Run the installation scipt.'''
#    
#    def build_container(self):
#        '''Run the scipt to create the virtual machine or docker.'''
#    
#    def strat_container(self):
#        '''Start the created container.'''
#        
#    def stop_container(self):
#        '''Stop the created container after the jobs are finished.'''
#    
#    def mount_shares(self):
#        '''Mount the data shares.'''
    
    def read_experiment_description(self):
        '''Read the contents of experiment provided by the user in  
        expectation.yaml.'''
        
        lines2 = tuple(open(os.path.join(project_path,'expectation.yml'), 'r'))
        array12 = list()
        list22 = ['n_microscpe_files', 'n_channels', 'n_object_types' \
                'workflow_type', 'microscope_type', 'plate_format',  \
                'plate_acquisition_mode', 'plate_name', \
                'description', 'acq_name', 'directory']
        
        # workflow_type, microscope_type, plate_format, plate_acquisition_mode
        # project_path, plate_name, description, acq_name, directory
        array12.append(list22)
        i1 = 0
        for line2 in range(1,len(lines2)):
            a1 = re.findall(list22[i1], lines2[line2])
            i1 += 1            
        
        
#    def init_experiment_details(self):
#        '''Create experiment, plate, acquisition etc. using an expectation.yaml 
#        file provided by the user in the project folder'''
#        
#        client = tmclient()
        
    def copy_config_files(self):
        '''Copy yaml files into the project folder, eg. expectation.yml'''
        
        shutil.copy(Project_Description_pipeline, project_path)
        shutil.copy(ImageAnalysis_pipeline, project_path)
        
        
    def test_workflow(self):
        '''Test the different stages of tissuemaps framework '''
        
        age_file(self,TIFF_FILES)
        
        client = tmclient()
        
        basepath = '/tmp/test'
        t = TestFileEnvironment(basepath, start_clear=False)
        project_path = os.path.join(basepath, 'tiny_canonical')
        
        result = t.run(
                    client.create_experiment(self, workflow_type,
                                             microscope_type, plate_format,
                                             plate_acquisition_mode)
                    .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
            
        
        result = t.run(
                    client.create_plate(self, plate_name, description)
                    .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        result = t.run(
            client.create_acquisition(self,plate_name,acq_name,description='')
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        result = t.run(
            client.get_microscope_files(self, plate_name, acq_name)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        result = t.run(
            client.upload_microscope_files(self,plate_name, acq_name,directory)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        result = t.run(
            copy_config_files(self)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
            
        
        result = t.run(
            client.submit_workflow(self, description=None)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)
        
        result = t.run(
            client.get_workflow_status(self, depth=2)
            .format(p=project_path),
                    expect_stderr=True)
        self.assertEqual(result.returncode, 0)

                

# set all necessary variables
export VM_IP=172.23.102.218
export experimentName=testExperiment2
export plateName=plate1
export acquisitionName=acquisition1
export testDataPath=~/testData/20170307_NUPReplicate_C22/

# Create the experiment
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName data experiment create

# Create a plate called “plate1” and check whether it was correctly created
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName data plate create -n plate1
sleep 10s
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName data plate ls

# Create an acquisition called “acquisition1” for plate “plate1" and check whether it was correctly created
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName data acquisition create -p $plateName -n $acquisitionName
sleep 10s
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName data acquisition ls

# Upload microscope files for acquisition “acquisition1” of plate “plate1” and check whether they were correctly uploaded
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName data microscope-file upload -p $plateName -a $acquisitionName --directory $testDataPath

# Check whether all the statuses returned by the following command are Complete
# tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName data microscope-file ls -p plate1 -a acquisition1

# Download a workflow description template
# tm_client -H $VM_IP -u test -p 123456 -e $experimentName workflow description download --file /tmp/workflow_description.yml
# Adapt the template: change “value” key (similar to what you would do in the UI)

# Upload the adapted workflow description
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName workflow description upload --file ~/testData/workflow_description.yml


# Upload a jterator project description (there must be a /tmp/pipeline.yaml file and several /tmp/handles/*.handles.yaml files)
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName workflow jtproject upload --directory ~/testData

# Submit the workflow
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName workflow job submit

sleep 10m

# Monitor the workflow
# tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName workflow job status
# watch -n 10 tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName workflow job status
# prepend command with "watch -n 10” to run query every 5 seconds

# Get log output of a particular job
# tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName workflow job log -s metaconfig -n metaconfig_run_000001

# Download feature values
tm_client -vv -H $VM_IP -u test -p 123456 -e $experimentName data feature-values download -o Cells --directory /tmp


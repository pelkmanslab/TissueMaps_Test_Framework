
#############################################################
# installing dependencies
#############################################################

sudo apt-get install git
sudo apt-get update
sudo apt-get install python-pip

git clone https://github.com/ansible/ansible-container
pip install .
git clone https://github.com/tissuemaps/elasticluster
pip install .
sudo apt-get install libpq-dev
sudo apt-get install libffi-dev

#############################################################
# install tm setup
#############################################################

git clone https://github.com/pelkmanslab/TmSetup
sudo pip install .

#############################################################
# install tm client
#############################################################

sudo apt-get update
git clone https://github.com/pelkmanslab/TmClient

#############################################################
# launch vm in sciencecloud
#############################################################

source .openstack.rc
mkdir .tmaps/setup/
cp tmsetup/etc/singlenode_setup_os.yml ~/.tmaps/setup/setup.yml

tm_setup -vv vm launch

tm_setup -vv vm deploy

# tm_setup -vv container build ( for launching a docker )

#############################################################
# execute python script for testing framework
#############################################################

git clone tm_framework_tests
cd /tm_framework_tests
chmod +x tm_test_framework.py
python TMsTestFramework.py

#############################################################

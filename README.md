# TissueMaps_Test_Framework

The test framework scripts can be run within a <a href="https://jenkins.io/" target="_blank"> Jekins server </a>.

Jenkins server need a proper  <a href="http://www.tutorialspoint.com/jenkins/" target="_blank"> configuration </a> especially to set up triggers related to a Github repository and a target email.

### Compatibility with Dockers and accessibility
If the test scripts requires  <a href="https://www.docker.com/" target="_blank"> Dockers </a>, it is critical to associate the Jenkins account ot it as and to give rights to the Jenkins user.
Jenkins will run scripts as "jenkins" user not "ubuntu" or other users. 

```
sudo usermod -aG docker jenkins
chmod 777 $YOUR_SCRIPT
```

### Mail notification
Jenkins needs to have set a target mail which will receive notification if something went wrong with the build but also an SMTP server which will send such a mail.
This can be done with these steps:

1. Login in Jenkins server

2. Select Configuration under manage Jenkins

3. Go to E-mail Notification option.

4. In SMTP server option enter "localhost" without quotes.

5. In Default user e-mail suffix enter your email suffix.

6. check Test configuration by sending test e-mail option.

7.  Enter your email-id.

8. click on test configuration.

9. check your email for confirmation

10. Now go to the project and select E-mail Notification under the Jenkins configuration project

11. enter E-mail id of the Recipients (separated by space for multiple recipients)

12. click on save.

### Tox
If the test scripts uses virtual environments and <a href="http://flask.pocoo.org/" target="_blank"> Flask </a> using different versions of Python and related libraries, 
it is convenient to install  <a href="https://tox.readthedocs.io/en/latest/" target="_blank"> Tox  </a> as an environment manager.
```
pip install tox
tox-quickstart   
``` 
Be aware that tox might install an old version of pip, which could not be able to find dependencies or other.
It is advised to perform this hack:
```
pip install pip==8.1.1
``` 

### Adding Build Step.
Now we are ready to tell Jenkins how to perform the tests, adding directly the command line steps or the scripts which perfom the testing. In this picture, two scripts are listed one which download the updated Tissuemaps and one which is actually running a test. Go to the project and select "Configure"
![alt tag](https://image.ibb.co/cYzvOv/build.png)

In get_TM.sh, it is possible to deploy TM using Dockers or Ansible scripts:
```
#!/bin/bash

#Clean previous versions
rm -rf ~/tissuemaps

#Download teh compose file
wget https://raw.githubusercontent.com/tissuemaps/tissuemaps/master/docker-compose.yml -q -P ~/tissuemaps

#Create and start containers
cd ~/tissuemaps
tm_deploy container build
```

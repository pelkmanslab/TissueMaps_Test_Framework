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

### 
he trigger and the 
 

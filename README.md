Steps to create ec2 instance and deploy web server and test whether its up and running or not

Make sure you install python and boto modules before executing the below steps

pre tasks:
=========

update boto file as below

vi .boto
[Credentials]
AWS_ACCESS_KEY_ID = *****************
AWS_SECRET_ACCESS_KEY = ****************


1). Clone the  repository
=========================

ubuntu@ip-172-31-91-102:~$ git clone https://github.com/kovelamudi/MADHAVA-RAO_Challenge.git


2). Run ansible playbook using the below command
=================================================


ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ ansible-playbook -i hosts ec2.yml


3). Test it by running the script verifying-webserver.sh
=========================================================



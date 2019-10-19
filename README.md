Steps to create ec2 instance and deploy web server and test whether its up and running or not

1). Clone the  repository

ubuntu@ip-172-31-91-102:~$ git clone https://github.com/kovelamudi/MADHAVA-RAO_Challenge.git


2). Run ansible playbook using the below command

ansible-playbook -i hosts --vault-password-file=vault-passwd.txt ec2.yml


ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ ansible-playbook -i hosts --vault-password-file=vault-passwd.txt ec2.yml


3). Test it by running the script verifying-webserver.sh

ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ ./verifying-webserver.sh
Webserver is up
ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$


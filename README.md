Steps to create ec2 instance and deploy web server and test whether its up and running or not

1). Clone the infrastructure challenge repository

2). Run ansible playbook using the below command

ansible-playbook -i hosts --vault-password-file=vault-passwd.txt ec2.yml

3). Test it by running the script verifying-webserver.sh

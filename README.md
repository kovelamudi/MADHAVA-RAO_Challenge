Steps to create ec2 instance and deploy web server and test whether its up and running or not

1). Clone the  repository

ubuntu@ip-172-31-91-102:~$ git clone https://github.com/kovelamudi/MADHAVA-RAO_Challenge.git
Cloning into 'MADHAVA-RAO_Challenge'...
remote: Enumerating objects: 36, done.
remote: Counting objects: 100% (36/36), done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 36 (delta 9), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (36/36), done.
ubuntu@ip-172-31-91-102:~$ pwd
/home/ubuntu
ubuntu@ip-172-31-91-102:~$ ls -ltr
total 8
drwxrwxrwx 2 ubuntu ubuntu 4096 Oct 19 00:47 backup
drwxrwxr-x 3 ubuntu ubuntu 4096 Oct 19 00:51 MADHAVA-RAO_Challenge
ubuntu@ip-172-31-91-102:~$ cd MADHAVA-RAO_Challenge/
ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ pwd
/home/ubuntu/MADHAVA-RAO_Challenge
ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ ls -ltr
total 32
-rw-rw-r-- 1 ubuntu ubuntu  236 Oct 19 00:51 verifying-webserver.sh
-rw-rw-r-- 1 ubuntu ubuntu    8 Oct 19 00:51 vault-passwd.txt
-rw-rw-r-- 1 ubuntu ubuntu   61 Oct 19 00:51 hosts
-rw-rw-r-- 1 ubuntu ubuntu 2540 Oct 19 00:51 ec2.yml
-rw-rw-r-- 1 ubuntu ubuntu  679 Oct 19 00:51 aws_keys.yml
-rw-rw-r-- 1 ubuntu ubuntu 1675 Oct 19 00:51 asgdemo.pem
-rw-rw-r-- 1 ubuntu ubuntu   87 Oct 19 00:51 ansible.cfg
-rw-rw-r-- 1 ubuntu ubuntu  327 Oct 19 00:51 README.md
ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$



2). Run ansible playbook using the below command

ansible-playbook -i hosts --vault-password-file=vault-passwd.txt ec2.yml


ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ ansible-playbook -i hosts --vault-password-file=vault-passwd.txt ec2.yml

PLAY [local] ***************************************************************************************************************************************************************

TASK [Create a security group] *********************************************************************************************************************************************
[DEPRECATION WARNING]: Distribution Ubuntu 18.04 on host localhost should use /usr/bin/python3, but is using /usr/bin/python for backward compatibility with prior Ansible
releases. A future Ansible release will default to using the discovered platform python for this host. See
https://docs.ansible.com/ansible/2.8/reference_appendices/interpreter_discovery.html for more information. This feature will be removed in version 2.12. Deprecation
warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
ok: [localhost]

TASK [Launch the new EC2 Instance] *****************************************************************************************************************************************
changed: [localhost]

TASK [Add the newly created host so that we can further contact it] ********************************************************************************************************
changed: [localhost -> localhost] => (item={u'ramdisk': None, u'kernel': None, u'root_device_type': u'ebs', u'private_dns_name': u'ip-172-31-86-4.ec2.internal', u'block_device_mapping': {u'/dev/sda1': {u'status': u'attached', u'delete_on_termination': True, u'volume_id': u'vol-0363e74c11d145d22'}}, u'key_name': u'asgdemo', u'public_ip': u'3.92.2.234', u'image_id': u'ami-04b9e92b5572fa0d1', u'tenancy': u'default', u'private_ip': u'172.31.86.4', u'groups': {u'sg-0e533baa3e5fec160': u'webservers_sg'}, u'public_dns_name': u'ec2-3-92-2-234.compute-1.amazonaws.com', u'state_code': 16, u'id': u'i-011c88bd603cc8146', u'tags': {}, u'placement': u'us-east-1a', u'ami_launch_index': u'0', u'dns_name': u'ec2-3-92-2-234.compute-1.amazonaws.com', u'region': u'us-east-1', u'ebs_optimized': False, u'launch_time': u'2019-10-19T00:52:26.000Z', u'instance_type': u't2.micro', u'state': u'running', u'architecture': u'x86_64', u'hypervisor': u'xen', u'virtualization_type': u'hvm', u'root_device_name': u'/dev/sda1'})

TASK [Add tag to Instance(s)] **********************************************************************************************************************************************
changed: [localhost] => (item={u'ramdisk': None, u'kernel': None, u'root_device_type': u'ebs', u'private_dns_name': u'ip-172-31-86-4.ec2.internal', u'block_device_mapping': {u'/dev/sda1': {u'status': u'attached', u'delete_on_termination': True, u'volume_id': u'vol-0363e74c11d145d22'}}, u'key_name': u'asgdemo', u'public_ip': u'3.92.2.234', u'image_id': u'ami-04b9e92b5572fa0d1', u'tenancy': u'default', u'private_ip': u'172.31.86.4', u'groups': {u'sg-0e533baa3e5fec160': u'webservers_sg'}, u'public_dns_name': u'ec2-3-92-2-234.compute-1.amazonaws.com', u'state_code': 16, u'id': u'i-011c88bd603cc8146', u'tags': {}, u'placement': u'us-east-1a', u'ami_launch_index': u'0', u'dns_name': u'ec2-3-92-2-234.compute-1.amazonaws.com', u'region': u'us-east-1', u'ebs_optimized': False, u'launch_time': u'2019-10-19T00:52:26.000Z', u'instance_type': u't2.micro', u'state': u'running', u'architecture': u'x86_64', u'hypervisor': u'xen', u'virtualization_type': u'hvm', u'root_device_name': u'/dev/sda1'})

TASK [Wait for SSH to come up] *********************************************************************************************************************************************
ok: [localhost] => (item={u'ramdisk': None, u'kernel': None, u'root_device_type': u'ebs', u'private_dns_name': u'ip-172-31-86-4.ec2.internal', u'block_device_mapping': {u'/dev/sda1': {u'status': u'attached', u'delete_on_termination': True, u'volume_id': u'vol-0363e74c11d145d22'}}, u'key_name': u'asgdemo', u'public_ip': u'3.92.2.234', u'image_id': u'ami-04b9e92b5572fa0d1', u'tenancy': u'default', u'private_ip': u'172.31.86.4', u'groups': {u'sg-0e533baa3e5fec160': u'webservers_sg'}, u'public_dns_name': u'ec2-3-92-2-234.compute-1.amazonaws.com', u'state_code': 16, u'id': u'i-011c88bd603cc8146', u'tags': {}, u'placement': u'us-east-1a', u'ami_launch_index': u'0', u'dns_name': u'ec2-3-92-2-234.compute-1.amazonaws.com', u'region': u'us-east-1', u'ebs_optimized': False, u'launch_time': u'2019-10-19T00:52:26.000Z', u'instance_type': u't2.micro', u'state': u'running', u'architecture': u'x86_64', u'hypervisor': u'xen', u'virtualization_type': u'hvm', u'root_device_name': u'/dev/sda1'})

PLAY RECAP *****************************************************************************************************************************************************************
localhost                  : ok=5    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ 





3). Test it by running the script verifying-webserver.sh


ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ curl 3.92.2.234
<html><h1>Hello World</h1></html>
ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ vi verifying-webserver.sh
ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ chmod 777 verifying-webserver.sh
ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$ ./verifying-webserver.sh
Webserver is up
ubuntu@ip-172-31-91-102:~/MADHAVA-RAO_Challenge$


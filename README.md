# MADHAVA-RAO_Challenge
Challenge to create ec2 instance and deploy web server securely


1). Infrastructure:
==================

Here I used Ansible as configuration management tool.

Created security group, ec2 instance and deployed webserver using ec2.yml file.

ubuntu@ip-172-31-91-102:~$ ansible-playbook -i hosts ec2.yml --ask-vault-pass
Vault password:

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
changed: [localhost] => (item={u'ramdisk': None, u'kernel': None, u'root_device_type': u'ebs', u'private_dns_name': u'ip-172-31-95-189.ec2.internal', u'block_device_mapping': {u'/dev/sda1': {u'status': u'attached', u'delete_on_termination': True, u'volume_id': u'vol-0202ba9e4d1ac0510'}}, u'key_name': u'asgdemo', u'public_ip': u'3.86.95.234', u'image_id': u'ami-04b9e92b5572fa0d1', u'tenancy': u'default', u'private_ip': u'172.31.95.189', u'groups': {u'sg-0e533baa3e5fec160': u'webservers_sg'}, u'public_dns_name': u'ec2-3-86-95-234.compute-1.amazonaws.com', u'state_code': 16, u'id': u'i-0c956af6db845ed8d', u'tags': {}, u'placement': u'us-east-1a', u'ami_launch_index': u'0', u'dns_name': u'ec2-3-86-95-234.compute-1.amazonaws.com', u'region': u'us-east-1', u'ebs_optimized': False, u'launch_time': u'2019-10-13T14:49:33.000Z', u'instance_type': u't2.micro', u'state': u'running', u'architecture': u'x86_64', u'hypervisor': u'xen', u'virtualization_type': u'hvm', u'root_device_name': u'/dev/sda1'})

TASK [Add tag to Instance(s)] **********************************************************************************************************************************************
changed: [localhost] => (item={u'ramdisk': None, u'kernel': None, u'root_device_type': u'ebs', u'private_dns_name': u'ip-172-31-95-189.ec2.internal', u'block_device_mapping': {u'/dev/sda1': {u'status': u'attached', u'delete_on_termination': True, u'volume_id': u'vol-0202ba9e4d1ac0510'}}, u'key_name': u'asgdemo', u'public_ip': u'3.86.95.234', u'image_id': u'ami-04b9e92b5572fa0d1', u'tenancy': u'default', u'private_ip': u'172.31.95.189', u'groups': {u'sg-0e533baa3e5fec160': u'webservers_sg'}, u'public_dns_name': u'ec2-3-86-95-234.compute-1.amazonaws.com', u'state_code': 16, u'id': u'i-0c956af6db845ed8d', u'tags': {}, u'placement': u'us-east-1a', u'ami_launch_index': u'0', u'dns_name': u'ec2-3-86-95-234.compute-1.amazonaws.com', u'region': u'us-east-1', u'ebs_optimized': False, u'launch_time': u'2019-10-13T14:49:33.000Z', u'instance_type': u't2.micro', u'state': u'running', u'architecture': u'x86_64', u'hypervisor': u'xen', u'virtualization_type': u'hvm', u'root_device_name': u'/dev/sda1'})

TASK [Wait for SSH to come up] *********************************************************************************************************************************************
ok: [localhost] => (item={u'ramdisk': None, u'kernel': None, u'root_device_type': u'ebs', u'private_dns_name': u'ip-172-31-95-189.ec2.internal', u'block_device_mapping': {u'/dev/sda1': {u'status': u'attached', u'delete_on_termination': True, u'volume_id': u'vol-0202ba9e4d1ac0510'}}, u'key_name': u'asgdemo', u'public_ip': u'3.86.95.234', u'image_id': u'ami-04b9e92b5572fa0d1', u'tenancy': u'default', u'private_ip': u'172.31.95.189', u'groups': {u'sg-0e533baa3e5fec160': u'webservers_sg'}, u'public_dns_name': u'ec2-3-86-95-234.compute-1.amazonaws.com', u'state_code': 16, u'id': u'i-0c956af6db845ed8d', u'tags': {}, u'placement': u'us-east-1a', u'ami_launch_index': u'0', u'dns_name': u'ec2-3-86-95-234.compute-1.amazonaws.com', u'region': u'us-east-1', u'ebs_optimized': False, u'launch_time': u'2019-10-13T14:49:33.000Z', u'instance_type': u't2.micro', u'state': u'running', u'architecture': u'x86_64', u'hypervisor': u'xen', u'virtualization_type': u'hvm', u'root_device_name': u'/dev/sda1'})

PLAY RECAP *****************************************************************************************************************************************************************
localhost                  : ok=5    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

ubuntu@ip-172-31-91-102:~$


For security created Security group and opened required ports to connect to the instance and route the traffic to http and https

Configred https by installing self signed certificates an redirecting the traffic from http to https by configuration changes in https.conf file 

Tested all the code by running the yml file and accessing the website and verified it by giving https URL



2). Coding
==========

Added the code in the repository as re.py

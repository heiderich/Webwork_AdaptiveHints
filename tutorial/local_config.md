## Download
- Download Vagrant for your platform -> [Vagrant Download](https://www.vagrantup.com/downloads.html)
	- Vagrant is a tool for setting development environments as Virtual Machines
	```
	pip install ansible
	```
	- Ansible is a tool for provisioning/configuring development environments

## Pull from Github
- Clone Webwork_AdaptiveHints [Github URL](https://github.com/cse103/Webwork_AdaptiveHints)
- Clone Administrative_Code [Github URL](https://github.com/cse103/Administrative_Code)

## Download database:
	scp username@webwork.cse.ucsd.edu:../zzhai/webwork.sql Webwork_AdaptiveHints/local_server`

## Start Vagrant
	- This will download a base VM image, install all the necessary dependencies for Webwork and Python stuff,
	  and configure (almost) everything you need for a development environment for the adaptive hints infrastructure
	- Email Zhen the error
	- Re-run the provisioning `	vagrant provision`

## Config Development Environment
	- src/servers/rest_server/webwork_config.py
	- username: webworkWrite
	- password: webwork
	- cd into directory /vagrant/src/servers/init-scripts
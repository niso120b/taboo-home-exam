Role - Jenkins
==============

Install Jenkins on CentOS / RedHat servers

Requirements
------------

None.

Role Variables
--------------

vars:

include in defaults/main.yml

Dependencies
------------

roles:
- java
- tools

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - tools
         - java
	 - jenkins

License
-------

BSD

Author Information
------------------

Nissim Bitan - niso120b@gmail.com

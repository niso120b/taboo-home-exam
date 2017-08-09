# Python 

## Usage Guide

the script use pip package python-jenkins, you should install this package by running 
the following command : 

``pip install python-jenkins``

the python script receives job name and build number

``python main.py job_name build_number``

if you wrong in the parameters, you get one of the following error messages

``
ERROR: you should pass two parameters job name and build number
 Example: python main.py job_name 1
 job_name - the jenkins job name
 1 - build number
``

``
ERROR: one of your parameters could not be found
 Example: python main.py job_name 1
     job_name - the jenkins job name
     1 - build number
``

### Success Output example

``
Taboola - Python & Jenkins API Exam!
Started by: admin
Status: success
Duration: 00:02:34
Slave: None, Jenkins not in master/slave mode, only master server
``





#
#
# By Nissim Bitan (niso120b@gmail.com)

import os
import jenkins
import datetime
import datetime
from sys import argv

'''
    -------------------------
        print_job_details 
    -------------------------
    
    print details about the build in specific job
    
    input - 
        job     - jenkins job name
        build   - build number in the job
    
    output - None 
'''
def print_job_details(job, build):
    server = jenkins.Jenkins('http://localhost:8080',
                             username='admin',
                             password='admin')

    try:
        build_info = server.get_build_info(name=job,
                                           number=build)

        user = build_info['actions'][0]['causes'][0]['userName']
        result = build_info['result'].lower()
        duration = datetime.datetime.utcfromtimestamp(int(build_info['duration']) / 1000).strftime('%H:%M:%S')

        print("Taboola - Python & Jenkins API Exam!")
        print("Started by: {}".format(user))
        print("Status: {}".format(result))
        print("Duration: {}".format(duration))
        print("Slave: None, Jenkins not in master/slave mode, only master server")

    except:
        print_error(type=1)

def print_error(type=0):
    if type == 0:
        print("ERROR: you should pass two parameters job name and build number")
    else:
        print("ERROR: one of your parameters could not be found")
    print(" Example: python main.py job_name 1")
    print("     job_name - the jenkins job name")
    print("     1 - build number")

if __name__ == "__main__":
    if len(argv) != 3:
        print_error(type=0)
        exit(0)

    job_name = str(argv[1])
    build_number = int(argv[2])
    print_job_details(job=job_name, build=build_number)

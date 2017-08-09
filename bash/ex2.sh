#!/bin/bash
# Taboola Home Exam - DevOps/Automation
# By Nissim Bitan (niso120b@gmail.com)

if [ "$#" -ne 1 ]; then
   echo "ERROR: The script requires one ftp url parameter"
   exit 1
fi

url_path=$1

log_file_name=access.log

if [ -f $log_file_name ]; then
    echo "Delete the access log file - Bye Bye log :)"
    rm -f  $log_file_name
fi

echo "Download the access log via wget"
wget --output-document=${log_file_name}.gz $url_path
echo "Unarchive log file from the .gz"
gzip -d $log_file_name

ls -lh $log_file_name

echo "List of broken and/or relocated urls"
cat $log_file_name | grep -v ' 200 ' | sed \$d | cut -d "\"" -f 2 | sed -e 's/HTTP\/1.0//g' | cut -d " " -f 2

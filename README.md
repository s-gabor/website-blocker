# website-blocker
WARNING!!!
This program modifies the content of the hosts file on your computer.

On MacOS the path for hosts file is: /private/etc/hosts. For windows it's a different one.

The constants.py file contains a "blocked_websites" list which will be added in the hosts file.
Each added row will be "127.0.0.1 + blocked_website".
Basically each website from the list is routed to this IP Address.

In order to run main.py administrator privileges are required. 
On MacOS, from the terminal run: "sudo python3 main.py" and enter the password.
For windows, again, it's different. 
Once started the script will run indefinitely. 
Must be manually force stopped.


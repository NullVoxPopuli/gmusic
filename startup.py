from gmusic.core.Core import Core
import os, json, subprocess, sys


pip_command = 'pip install -r requirements.txt'
gstreamer_command = 'apt-get install python-gst-1.0'

if not os.path.isfile('data/unlocked/credentials.json'):
    try:
        output = subprocess.check_output(['bash', '-c', pip_command])
        output = subprocess.check_output(['bash', '-c', gstreamer_command])
    except:
        print('Dependencies not installed, please run as sudo.')
        sys.exit(1)

    print('Installed dependencies.')

    print('Welcome to GMusic, a Bash Terminal implementation of Google All-Access Music.')
    print('Please enter an application password for Google Music. This will be stored')
    print('locally on your device. WE WILL NEVER ACCESS THIS FILE OUTSIDE OF USE IN')
    print('GMUSIC ON THIS MACHINE. If you delete the file, you will be required to')
    print('rerun this script to generate a keyfile.\n')

    email = raw_input('Please enter your Google email:  ')
    password = raw_input('Please enter an application specific password:  ')
    with open('data/unlocked/credentials.json','w') as credentials:
    	json.dump({"username": email, "password": password}, credentials)

print('Welcome to GMusic. Logging in and loading your library.')

gm = Core()
gm.start()

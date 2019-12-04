import paramiko
import sys
import subprocess
import os



def hardware_install():
       print "Trying to connect VM "
       try:
           ssh=paramiko.SSHClient()
           ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           ssh.connect('10.120.21.98',username='ppelli',password='Inf0bl0x123')
           print ("Connected \n")
           if os.path.exists('/mnt/home/ppelli/resmgr'):
                  ssh.exec_command('rm -rf /mnt/home/ppelli/resmgr')
           else:
                  print ("File Check Passed \n")
           command1='cd '+ PATH + " ; ls -ltr %s/nios*_x86_64.bin | awk '{print $9}' | cut -d '/' -f 8 | xargs config_grid -h " + MACHINE_TYPE + " -f "
           stdin, stdout, stderr = ssh.exec_command(command1)
           for line in stdout.readlines():
               print line
           for line in stderr.readlines():
                  print line
       except paramiko.AuthenticationException:
           print ("failed to connect \n")
           sys.exit(1)
           ssh.close()


def virtual_type1():
       print "Trying to connect VM "
       try:
           ssh=paramiko.SSHClient()
           ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           ssh.connect('10.120.21.98',username='ppelli',password='Inf0bl0x123')
           print ("Connected \n")
           if os.path.exists('/mnt/home/ppelli/resmgr'):
                  ssh.exec_command('rm -rf /mnt/home/ppelli/resmgr')
           else:
                  print ("File Check Passed \n")
           command1='cd '+ PATH + " ; ls -ltr nios*"+ IMAGE_TYPE +".ova | awk '{print $9}' | cut -d '/' -f 8 | xargs config_grid -h " + MACHINE_TYPE + " -f "
           print command1
           stdin, stdout, stderr=ssh.exec_command(command1)
           for line in stdout.readlines():
               print line
           for line in stderr.readlines():
                  print line
       except paramiko.AuthenticationException:
           print ("failed to connect \n")
           sys.exit(1)
           ssh.close()




MACHINE_TYPE=raw_input("Enter your type of Machine : eg : HARDWARE_IB_810 for hardware Machine or VIRTUAL for Vnios \n")
print MACHINE_TYPE
PATH=raw_input("Please enter the PATH of the BUILD to be installed on specified machine  \n")
print PATH
IMAGE_TYPE=raw_input("Please enter version of NIOS Image Installation . eg : 160G-1410, 160G-820,500G-1400,300G-800 \n")
print IMAGE_TYPE
if (MACHINE_TYPE=='HARDWARE'):
       hardware_install()
elif (MACHINE_TYPE =='VIRTUAL'and IMAGE_TYPE=='160G-1410'):
       virtual_type1()
elif (MACHINE_TYPE =='VIRTUAL'and IMAGE_TYPE=='160G-820'):
    virtual_type2()
elif (MACHINE_TYPE =='VIRTUAL'and IMAGE_TYPE=='500G-1400'):
    virtual_type3()
elif (MACHINE_TYPE =='VIRTUAL'and IMAGE_TYPE=='300G-800'):
    virtual_type4()
else:
    print ("Better luck next time with correct options \n")


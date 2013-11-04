from fabric.api import *


def hosts():
   ''' uses the hosts list '''
   env.user = 'root' 
   env.hosts = open('hosts', 'r').readlines()
   
def setup_java():  
   ''' Setup Java '''
   sudo('yum install java7')

def setup_user():
   ''' Setup User '''
   with settings(warn_only=True): 
      sudo('groupadd hadoop')
      sudo('useradd -g hadoop hduser')
      puts('Switched to `hduser`')
      sudo('ssh-keygen -f $HOME/.ssh/id_rsa -t rsa -N "" -q', user='hduser') 
      sudo('cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys', user='hduser')
    
def disable_ipv6():
   ''' Disable IPV6 '''
   sudo('sysctl -w net.ipv6.conf.all.disable_ipv6=1')
   sudo('sysctl -w net.ipv6.conf.default.disable_ipv6=1')
   puts('Verify IP6 is disabled') 
   sudo('cat /proc/sys/net/ipv6/conf/all/disable_ipv6')



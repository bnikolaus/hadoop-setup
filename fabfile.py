from fabric.api import *
from fabric.contrib.files import append
from fabric.contrib.files import exists

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

def setup_hadoop():
   sudo('rm -rf /home/hduser/hadoop-1.2.1/hadoop-1.2.1') 
   sudo('yum install wget') 
   # sudo('wget -P /users/hduser/ http://mirror.nexcess.net/apache/hadoop/common/hadoop-1.2.1/hadoop-1.2.1.tar.gz', user='hduser')
   put('./dist/hadoop-1.2.1.tar.gz', '/home/hduser/') 
   sudo('chown hduser:hadoop /home/hduser/hadoop-1.2.1.tar.gz')
   sudo('tar -xvf /home/hduser/hadoop-1.2.1.tar.gz')
   sudo('mv -f hadoop-1.2.1 /home/hduser/hadoop-1.2.1')
   sudo('chown -R hduser:hadoop /home/hduser/*')
   with settings(sudo_user="hduser"):
      sudo('ln -s hadoop-1.2.1 hadoop')
   #append("/users/hduser/.bashrc", 'export HADOOP_PREFIX=/home/hduser/hadoop', user='hduser')  

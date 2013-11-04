# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

#
export DISPLAY='10.16.142.227:0:0'
export HADOOP_PREFIX=/home/hduser/hadoop
export JAVA_HOME=/usr/lib/jvm/jre-openjdk/
export PATH=$PATH:$HADOOP_PREFIX/bin

# User specific aliases and functions

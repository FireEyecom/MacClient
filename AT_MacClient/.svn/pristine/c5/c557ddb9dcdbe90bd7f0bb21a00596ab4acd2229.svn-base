
#coding:utf-8
import re
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

filename = "/Users/elvis/desktop/macClient/variable.txt"
def replaceVariable(filename,ip,robotPath,macAccount):

	f=open(filename,"rb")
	content = f.read()
	f.close()
	f=open(filename,"rb")
	while 1:
	    line = f.readline()
	    if not line:
	        break
	    ipflag = re.search("\$\{ip\}",line)
	    robotPathflag = re.search("\$\{robotPath\}",line)
	    macAccountflag = re.search("\$\{macAccount\}",line)
	    if ipflag is not None:
	    	line = line.replace('$','\$')
	    	line = line.replace('{',"\{")
	    	line = line.replace('}',"\}")
	    	string = "${ip}             " + ip + "\n"
	    	content = re.sub(line,string,content)
	    if robotPathflag is not None:
	    	line = line.replace('$','\$')
	    	line = line.replace('{',"\{")
	    	line = line.replace('}',"\}")
	    	string = "${robotPath}      " + robotPath + "\n"
	    	content = re.sub(line,string,content)
	    if macAccountflag is not None:
	    	line = line.replace('$','\$')
	    	line = line.replace('{',"\{")
	    	line = line.replace('}',"\}")
	    	string = "${macAccount}     " + macAccount +"\n"
	    	content = re.sub(line,string,content)

	f=open(filename,"wb")
	f.write(content)
	f.close()

if __name__ == '__main__':
	filename = sys.argv[1]
	ip = sys.argv[2]
	robotPath = sys.argv[3]
	macAccount = sys.argv[4]
	replaceVariable(filename,ip,robotPath,macAccount)


'''  
=================================================================
	@version  1.3
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Testset parse module.
=================================================================
'''
import subprocess
import sys

def parse(pname,location):
	
	'''
	Initializations
	'''
	testset={}
	uni=open(location+"/universe.txt")
	i=0
	
	'''
	Clean up and Folder initialization.
	'''
	subprocess.call("rm -r outputs/State_outputs",shell=True)
	subprocess.call("mkdir outputs/State_outputs",shell=True)
	subprocess.call("rm -r outputs/Branch_outputs",shell=True)
	subprocess.call("mkdir outputs/Branch_outputs",shell=True)

	
	'''
	Parsing of statement coverage info
	'''

	subprocess.call(["rm",pname+".c.gcov"])
	subprocess.call(["rm",pname+".gcda"])
	subprocess.call("gcc -fprofile-arcs -ftest-coverage -g -o "+pname+" "+location+"/"+pname+".c",shell=True)


	for line in uni:
		i=i+1
		testset[i]=str(line)
		subprocess.call("./"+pname+" "+str(line),shell=True)
		temp_out=subprocess.check_output("gcov "+pname,shell=True)
		print temp_out,"\n"
		try:
			check=subprocess.check_output("mv "+pname+".c.gcov"+" Outputs/State_outputs/"+str(i),shell=True)
			print check
			subprocess.call(["rm",pname+".gcda"])
		except Exception as e:
			logging.error(traceback.format_exc())
			print "\n Abrupt exit"
			sys.exit(0)


	'''
	Clean up
	'''
	uni.close()
	subprocess.call(["rm",pname+".gcno"])
	subprocess.call(["rm","-r",pname+".dsYM"])
	subprocess.call(["rm",pname])
	

	return testset

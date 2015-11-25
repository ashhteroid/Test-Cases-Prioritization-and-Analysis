'''  =================================================================
  @version  1.1
  @author   Ashwin Ramadevanahalli
  @title    Testing.
 	 =================================================================

Testset_parse module.
######################################################################
'''
import subprocess
import sys

def parse():
	
	location="/Users/Ashwin/Downloads/benchmarks/tcas"
	testset={}
	uni=open(location+"/universe.txt")
	subprocess.call("rm -r outputs/State_outputs",shell=True)
	subprocess.call("mkdir outputs/State_outputs",shell=True)
	subprocess.call("rm -r outputs/Branch_outputs",shell=True)
	subprocess.call("mkdir outputs/Branch_outputs",shell=True)

	
	'''Clean up'''
	
	subprocess.call(["rm","tcas.c.gcov"])
	subprocess.call(["rm","tcas.gcda"])
	subprocess.call("gcc -fprofile-arcs -ftest-coverage -g -o tcas "+location+"/tcas.c",shell=True)

	i=0
	for line in uni:
		i=i+1
		testset[i]=str(line)
		subprocess.call("./tcas "+str(line),shell=True)
		temp_out=subprocess.check_output("gcov tcas",shell=True)
		print temp_out,"\n"
		try:
			check=subprocess.check_output("mv tcas.c.gcov Outputs/State_outputs/"+str(i),shell=True)
			print check
			subprocess.call(["rm","tcas.gcda"])
		except Exception as e:
			logging.error(traceback.format_exc())
			print "\n Abrupt exit"
			sys.exit(0)



	subprocess.call(["rm","tcas.gcno"])
	subprocess.call(["rm","-r","tcas.dSYM"])
	subprocess.call(["rm","tcas"])
	return testset

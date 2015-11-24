'''  =================================================================
  @version  1.1
  @author   Ashwin Ramadevanahalli
  @title    Testing.
 	 =================================================================


######################################################################
'''
import os
import sys
import subprocess


location="/Users/Ashwin/Downloads/benchmarks/tcas"

uni=open(location+"/universe.txt")


'''Clean up'''
subprocess.call(["rm","tcas.c.gcov"])
subprocess.call(["rm","tcas.gcda"])

subprocess.call("gcc -fprofile-arcs -ftest-coverage -g -o tcas "+location+"/tcas.c",shell=True)


for line in uni:
	print line
	subprocess.call("./tcas "+str(line),shell=True)
	temp_out=subprocess.check_output("gcov tcas",shell=True)
	print temp_out
	subprocess.call(["rm","tcas.c.gcov"])
	subprocess.call(["rm","tcas.gcda"])




subprocess.call(["rm","tcas.gcno"])
subprocess.call(["rm","-r","tcas.dSYM"])
subprocess.call(["rm","tcas"])
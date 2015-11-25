'''  
=================================================================
	@version  1.4
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Main module.
=================================================================
'''

import os
import sys
import subprocess
import testset_parse
import gcov_parse

'''
Initializations
'''
exclu=[]
pname="tcas"
location="/Users/Ashwin/Downloads/benchmarks/"+pname

'''
Cleaning
'''
subprocess.call("rm -r outputs",shell=True)
subprocess.call("mkdir outputs",shell=True)


'''
Testset parse module 
returns: 	A dictionary with Key in range '1 to No_of_tests' and value as the testcases and total number of statements in program.
input: 		program name, location of program.
'''
testset,tot_statements=testset_parse.parse(pname,location)

'''
Gcov parse module 
returns:	state_testset=list of <testcase,No of statements it covers> and Brances_testset=list of <testcase,No of brances it covers>
input:		testset and Exclution set
'''

state_testset,branch_testset,sb_testset=gcov_parse.parse(testset,exclu,tot_statements)
print state_testset
print branch_testset
print sb_testset









'''  
=================================================================
	@version  1.3
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
Helper Functions
'''


'''
Testset parse module 

returns:
A dictionary with Key in range '1 to No_of_tests' and value as the testcases.

input:
program name, location of program.
'''
testset=testset_parse.parse(pname,location)

'''
Gcov parse module 

returns:
state_testset=list of <testcase,No of statements it didnt cover>
Brances_testset=list of <testcase,No of brances it covers>

input:
testset and Exclution set()
'''

state_testset,branch_testset=gcov_parse.parse(testset,exclu)
print state_testset


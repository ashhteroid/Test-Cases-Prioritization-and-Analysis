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

'''
Cleaning
'''
subprocess.call("rm -r outputs",shell=True)
subprocess.call("mkdir outputs",shell=True)

'''
Helper Functions
'''


'''
Testset parse module returns a dictionary with Key in range '1 to No_of_tests' and value as the testcases.
'''
testset=testset_parse.parse()

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


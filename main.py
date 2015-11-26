'''  
=================================================================
	@version  1.7
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
import rand_pri
import tot_pri
import add_pri

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
returns:	state_testset=list of <No of statements it covers,testcase> and Brances_testset=list of <No of brances it covers,testcase> and both.
input:		testset and Exclution set
'''

state_testset,branch_testset,sb_testset=gcov_parse.parse(testset,exclu,tot_statements)



'''
Random prioritization
returns:	Random prioritizated testsets for statement, branch and both coverage.
input:		testset, program name and location of program
'''
#Ran_S,Ran_B,Ran_SB=rand_pri.pri(testset.values(),pname,location)

'''
Total coverage prioritization
returns:	Total coverage prioritizated testsets for statement, branch and both coverage.
input:		testsets with coverage information, program name and location of program.
'''
#Tot_S,Tot_B,Tot_SB=tot_pri.pri(state_testset,branch_testset,sb_testset,pname,location)


'''
Additional coverage prioritization
returns:	Additional coverage prioritizated testsets for statement, branch and both coverage.
input:		testsets with coverage information, program name and location of program.
'''

Add_S,Add_B,Add_SB=add_pri.pri(state_testset,branch_testset,sb_testset,pname,location)






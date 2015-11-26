'''  
=================================================================
	@version  1.8
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
pname=str(str(subprocess.check_output("pwd",shell=True)).split('/')[-1].strip())
location=""
maxlimit={'tcas':96.67,'totinfo':97.04,'printtokens':95.34,'printokens2':99.50,'replace':95.02,'schedule':98.67,'schedule2':99.23}
#location="/Users/Ashwin/Downloads/benchmarks/"+pname+"/"


'''
Cleaning
'''
print "################################\nEntered CLeanig\n################################\n"
subprocess.call("rm -r outputs",shell=True)
subprocess.call("mkdir outputs",shell=True)


'''
Testset parse module 
returns: 	A dictionary with Key in range '1 to No_of_tests' and value as the testcases and total number of statements in program.
input: 		program name, location of program.
'''
print "################################\nEntered Testset parse module\n################################\n"
testset,tot_statements,No_of_tests=testset_parse.parse(pname,location)
print testset
print tot_statements

'''
Gcov parse module 
returns:	state_testset=list of <No of statements it covers,testcase> and Brances_testset=list of <No of brances it covers,testcase> and both.
input:		testset and total number of statements
'''
print "################################\nEntered Gcov parse module\n################################\n"
state_testset,branch_testset,sb_testset=gcov_parse.parse(testset,tot_statements)
print state_testset



'''
Random prioritization
returns:	Random prioritizated testsets for statement, branch and both coverage.
input:		testset, program name and location of program, max coverage
'''
print "################################\nEntered Random prioritization\n################################\n"
Ran_S,Ran_B,Ran_SB=rand_pri.pri(testset.values(),pname,location,maxlimit)

'''
Total coverage prioritization
returns:	Total coverage prioritizated testsets for statement, branch and both coverage.
input:		testsets with coverage information, program name and location of program, max coverage
'''
Tot_S,Tot_B,Tot_SB=tot_pri.pri(state_testset,branch_testset,sb_testset,pname,location,maxlimit)


'''
Additional coverage prioritization
returns:	Additional coverage prioritizated testsets for statement, branch and both coverage.
input:		testsets with coverage information, program name and location of program, max coverage
'''

Add_S,Add_B,Add_SB=add_pri.pri(state_testset,branch_testset,sb_testset,pname,location,maxlimit)

print "################################\nResult Section\n################################\n"

print len(Ran_S)
print len(Ran_B)
print len(Ran_SB)
print len(Tot_S)
print len(Tot_B)
print len(Tot_SB)
print len(Add_S)
print len(Add_B)
print len(Add_SB)

print "Total number of test cases=",No_of_tests




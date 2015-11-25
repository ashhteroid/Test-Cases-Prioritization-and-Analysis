'''  
=================================================================
	@version  1.6
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Random Priorization module.
=================================================================
'''
import random
import subprocess
import sys

'''Intializations'''


def pri(tests,pname,location):
	s_adeq_suite=[]
	b_adeq_suite=[]
	sb_adeq_suite=[]
	sflag=True
	bflag=True
	random.shuffle(tests)
	subprocess.call(["rm",pname+".gcno"])
	subprocess.call(["rm","-r",pname+".dsYM"])
	subprocess.call(["rm",pname])
	subprocess.call(["rm",pname+".c.gcov"])
	subprocess.call(["rm",pname+".gcda"])
	subprocess.call("gcc -fprofile-arcs -ftest-coverage -g -o "+pname+" "+location+"/"+pname+".c",shell=True)
	for test in tests:

		if sflag==True:
			s_adeq_suite.append(test)
		if bflag==True:
			b_adeq_suite.append(test)
		sb_adeq_suite.append(test)

		subprocess.call("./"+pname+" "+test,shell=True)
		temp_out=subprocess.check_output("gcov -b -c "+pname,shell=True)
		
		if 80==float(temp_out.split('\n')[1].split(':')[-1].split()[0].strip('%')):
			sflag=False

		if 76==float(temp_out.split('\n')[2].split(':')[-1].split()[0].strip('%')):
			bflag=False

		if not(sflag) and not(bflag):
			break
		else:
			sys.exit("Adequate test not found")









	return s_adeq_suite,b_adeq_suite,sb_adeq_suite



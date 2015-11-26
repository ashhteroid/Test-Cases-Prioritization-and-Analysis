'''  
=================================================================
	@version  1.6
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Total Prioritiztion module.
=================================================================
'''
import subprocess
import sys

def pri(state,branch,sb,pname,location):
	
	state.sort(key=lambda tup:tup[0],reverse=True)
	branch.sort(key=lambda tup:tup[0],reverse=True)
	sb.sort(key=lambda tup:tup[0],reverse=True)

	return helper(state,pname,location,1),helper(state,pname,location,2),helper(state,pname,location,3)

'''
	Helper function to select test cases prifix set which satisfy adequacy
	returns:	adequant set
	input: 		test cases, program name and location and option(1-list,2-branch,3-both)
'''

def helper(tlist,pname,location,option):
	
	ade=[]
	subprocess.call(["rm",pname+".gcno"])
	subprocess.call(["rm","-r",pname+".dsYM"])
	subprocess.call(["rm",pname])
	subprocess.call(["rm",pname+".c.gcov"])
	subprocess.call(["rm",pname+".gcda"])
	subprocess.call("gcc -fprofile-arcs -ftest-coverage -g -o "+pname+" "+location+"/"+pname+".c",shell=True)

	for test in tlist:
		ade.append(test[1])
		subprocess.call("./"+pname+" "+test[1],shell=True)
		temp_out=subprocess.check_output("gcov -b -c "+pname,shell=True)

		if (option==1 or option==2) and 100==float(temp_out.split('\n')[option].split(':')[-1].split()[0].strip('%')):
			return ade
		elif (option==3) and (100==float(temp_out.split('\n')[1].split(':')[-1].split()[0].strip('%'))) and (100==float(temp_out.split('\n')[2].split(':')[-1].split()[0].strip('%'))):
			return ade
			
	sys.exit("Adequate test not found(Total)")


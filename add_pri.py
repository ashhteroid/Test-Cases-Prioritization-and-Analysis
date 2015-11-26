'''  
=================================================================
	@version  1.7
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Additional Prioritiztion module.
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


	selectedtes -> 	best choice at each step
	selected 	->	file to store and reset .gcda at each run.
'''

def helper(tlist,pname,location,option):
	
	'''Initialization and clean up'''
	ade=[]
	loopflag=True
	remflag=False
	subprocess.call(["rm",pname+".gcno"])
	subprocess.call(["rm","-r",pname+".dsYM"])
	subprocess.call(["rm",pname])
	subprocess.call(["rm",pname+".c.gcov"])
	subprocess.call(["rm",pname+".gcda"])
	subprocess.call("gcc -fprofile-arcs -ftest-coverage -g -o "+pname+" "+location+"/"+pname+".c",shell=True)

	'''Adding fisrt test set'''
	ade.append(tlist.pop(0)[1])
	subprocess.call("./"+pname+" "+ade[0],shell=True)
	temp_out=subprocess.check_output("gcov -b -c "+pname,shell=True)
	coverage=float(temp_out.split('\n')[option].split(':')[-1].split()[0].strip('%'))
	if option==3:
		coverage=float(temp_out.split('\n')[1].split(':')[-1].split()[0].strip('%'))+float(temp_out.split('\n')[2].split(':')[-1].split()[0].strip('%'))

	subprocess.call("cp "+pname+".gcda tempfile",shell=True)
	


	'''Addition of subsequent best test cases'''
	while(True):
		
		'''Exit condition'''
		if (option==1 or option==2) and 100==coverage:
				return ade
		elif (option==3) and (100==float(temp_out.split('\n')[1].split(':')[-1].split()[0].strip('%'))) and (100==float(temp_out.split('\n')[2].split(':')[-1].split()[0].strip('%'))):
				return ade
		oldcoverage=coverage

		
		'''Selection of best testcase'''
		for test in tlist:
			subprocess.call("./"+pname+" "+test[1],shell=True)
			temp_out=subprocess.check_output("gcov -b -c "+pname,shell=True)

			newcoverage=float(temp_out.split('\n')[option].split(':')[-1].split()[0].strip('%'))
			if option==3:
				newcoverage=float(temp_out.split('\n')[1].split(':')[-1].split()[0].strip('%'))+float(temp_out.split('\n')[2].split(':')[-1].split()[0].strip('%'))

			if coverage<newcoverage:
				coverage=newcoverage
				subprocess.call("rm selected",shell=True)
				subprocess.call("cp "+pname+".gcda selected",shell=True)
				selectedtest=test
				remflag=True

			subprocess.call(["rm",pname+".c.gcov"])
			subprocess.call(["rm",pname+".gcda"])
			subprocess.call("cp tempfile "+pname+".gcda",shell=True)

		'''Restoring environment'''
		subprocess.call("rm tempfile",shell=True)
		subprocess.call("cp selected tempfile",shell=True)
		subprocess.call("cp selected "+pname+".gcda",shell=True)

		'''addition of best set'''
		if remflag==True:
			tlist.remove(selectedtest)
			ade.append(selectedtest[1])
			remflag=False

		'''Fault tolerance'''
		if len(tlist)==0 or oldcoverage==coverage:
			sys.exit("Adequate test not found(Additional)")
	

	


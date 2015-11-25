'''  
=================================================================
	@version  1.3
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Gcov output file parse module.
=================================================================
		Bout=open("/outputs/State_outputs")
'''


def parse(testset,exclu):
	state_testset=[]
	for key in testset:
		count=0
		Sout=open("outputs/State_outputs/"+str(key))
		for line in Sout.readlines():
			if line.split(':')[0]=="    #####":
				count+=1
		Sout.close()
		tu=(count,testset[key].strip('\n'))
		state_testset.append(tu)


	return state_testset,0
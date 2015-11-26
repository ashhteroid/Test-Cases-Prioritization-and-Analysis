'''  
=================================================================
	@version  2.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Gcov output file parse module.
=================================================================
		Bout=open("/outputs/State_outputs")
'''


def parse(testset,total):
	state_testset=[]
	branch_testset=[]
	sb_testset=[]
	flag=True
	for key in testset:
		scount=0
		bcount=0
		Sout=open("outputs/"+str(key))
		for line in Sout.readlines():
			if line.split(':')[0]=="    #####":
				scount+=1

			ls=line.split()
			if ls[0]=="branch" and ls[2]=="taken" and int(ls[3])>0:
				bcount+=1

		Sout.close()

		Stu=(total-scount,testset[key])
		state_testset.append(Stu)

		Btu=(bcount,testset[key])
		branch_testset.append(Btu)

		SBtu=(bcount+total-scount,testset[key])
		sb_testset.append(SBtu)



	return state_testset,branch_testset,sb_testset
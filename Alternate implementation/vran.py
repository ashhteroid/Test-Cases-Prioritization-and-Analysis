'''  
=================================================================
	@version  2.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Random Priorization module.
=================================================================
'''


import random
import vec_manipulation
import sys


def pri(rrlist,location,pname,option):
	
	rlist=rrlist
	random.shuffle(rlist)
	


	f=open(location+"bit/"+pname+"/out"+str(option)+".txt")
	
	pmax=int(str(f.readlines()[0]).strip('\n'))
	print "Ran Max coverage:",pmax
	f.close()
	
	cov=rlist[0][1]
	vec=vec_manipulation.vfetch(rlist[0][0],location,pname,option)
	suite=[]
	suite.append(rlist[0][2])
	rlist.remove(rlist[0])


	for tup in rlist:
		
		if cov==pmax:
			print cov								##########
			return suite

		
		cov,vec=vec_manipulation.vmerge(vec,vec_manipulation.vfetch(tup[0],location,pname,option))
		suite.append(tup[2])
	if cov==pmax:
			print cov								##########
			return suite
	
	print "Max:",pmax," coverage:",cov
	sys.exit("Ran:Adequate testset not found")





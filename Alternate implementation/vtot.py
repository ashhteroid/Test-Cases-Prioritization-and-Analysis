'''  
=================================================================
	@version  3.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Total Prioritiztion module.
=================================================================
'''

import vec_manipulation
import sys

def pri(tlist,location,pname,option):
	tlist.sort(key=lambda tup:tup[1],reverse=True)


	f=open(location+"bit/"+pname+"/out"+str(option)+".txt")
	
	pmax=int(str(f.readlines()[0]).strip('\n'))
	print "Tot Max coverage:",pmax
	f.close()
	
	cov=tlist[0][1]
	vec=vec_manipulation.vfetch(tlist[0][0],location,pname,option)
	suite=[]
	suite.append(tlist[0][2])
	tlist.remove(tlist[0])
	flag=True



	for tup in tlist:
		if cov==pmax:
			print cov								##########
			return suite

		suite.append(tup[2])

		cov,vec=vec_manipulation.vmerge(vec,vec_manipulation.vfetch(tup[0],location,pname,option))

	if cov==pmax:
		print cov								##########
		return suite
	print suite
	print "Max:",pmax," coverage:",cov
	sys.exit("TOT:Adequate testset not found")



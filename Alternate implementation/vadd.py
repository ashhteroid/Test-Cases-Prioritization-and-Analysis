'''  
=================================================================
	@version  3.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Additional Prioritiztion module.
=================================================================
'''


import vec_manipulation
import sys

def pri(alist,location,pname,option):
	alist.sort(key=lambda tup:tup[1],reverse=True)


	f=open(location+"bit/"+pname+"/out"+str(option)+".txt")
	
	pmax=int(str(f.readlines()[0]).strip('\n'))
	print "Add Max coverage:",pmax
	f.close()
	
	cov=alist[0][1]
	vec=vec_manipulation.vfetch(alist[0][0],location,pname,option)
	suite=[]
	suite.append(alist[0][2])
	print alist[0][2]
	alist.remove(alist[0])
	end=len(alist)+1
	i=0
	notfirst=False
	
	while(i<end):
		flag=False

		for tup in alist:
			if cov==pmax:
				print cov							#######
				if notfirst:
					suite.append(selected[2])
				return suite
			value,mvec=vec_manipulation.vmerge(vec,vec_manipulation.vfetch(tup[0],location,pname,option))
			if value>cov:			
				cov=value
				selected=tup
				smvec=mvec
				flag=True
		notfirst=True
		if flag:
			vec=smvec
			suite.append(selected[2])
			alist.remove(selected)	
		else:
			print "Add coverage: ",suite
			print "Max:",pmax," coverage:",cov
			sys.exit("ADD:Adequate testset not found "+str(option))


		i+=1
	print "Max:",pmax," coverage:",cov
	sys.exit("Alternate ADD:Adequate testset not found "+str(option))

	
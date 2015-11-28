'''  
=================================================================
	@version  3.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Main module.
=================================================================
'''

import os
import sys
import subprocess
import pickle
import bitvector
import vran
import vtot
import vadd


'''
Bit vector data
input: 		location,pname,option
returns:	vlist<index,coverage number,testcase>
'''
svlist=bitvector.reader(location,pname,1)
bvlist=bitvector.reader(location,pname,2)
sbvlist=bitvector.reader(location,pname,3)

print svlist
print bvlist
print sbvlist

'''
Random prioritization

returns: Random prioritizated testsets
'''


a=list(svlist)
b=list(bvlist)
c=list(sbvlist)
Ran_S=vran.pri(a,location,pname,1)
Ran_B=vran.pri(b,location,pname,2)
Ran_SB=vran.pri(c,location,pname,3)
'''
print Ran_S
print Ran_B
print Ran_SB
'''

'''
Total prioritization

returns: Total prioritizated testsets
'''
d=list(svlist)
e=list(bvlist)
f=list(sbvlist)

Tot_S=vtot.pri(d,location,pname,1)
Tot_B=vtot.pri(e,location,pname,2)
Tot_SB=vtot.pri(f,location,pname,3)

'''
print "Total coverage\n",Tot_S
print Tot_B
print Tot_SB
'''
'''
Additional Total prioritization

returns: Additional Total prioritizated testsets

'''

Add_S=vadd.pri(svlist,location,pname,1)
Add_B=vadd.pri(bvlist,location,pname,2)
Add_SB=vadd.pri(sbvlist,location,pname,3)
'''
print Add_S
print Add_B
print Add_SB
'''



print "################################\n","Result Section of ",pname,"\n################################\n"

print "Number of test cases from Random prioritization(Statement coverage)=",len(Ran_S)
print "Number of test cases from Random prioritization(Branch coverage)=",len(Ran_B)
print "Number of test cases from Random prioritization(Both )=",len(Ran_SB)
print "Number of test cases from Total prioritization(Statement coverage)=",len(Tot_S)
print "Number of test cases from Total prioritization(Branch coverage)=",len(Tot_B)
print "Number of test cases from Total prioritization(Both coverage)=",len(Tot_SB)
print "Number of test cases from Additional prioritization(Statement coverage)=",len(Add_S)
print "Number of test cases from Additional prioritization(Branch coverage)=",len(Add_B)
print "Number of test cases from Additional prioritization(Both coverage)=",len(Add_SB)





'''Storing Results'''

subprocess.call("rm -r results",shell=True)

subprocess.call("mkdir results",shell=True)

test=open("results/sran","w")
pickle.dump(Ran_S, test)
test.close()

test=open("results/bran","w")
pickle.dump(Ran_B, test)
test.close()

test=open("results/sbran","w")
pickle.dump(Ran_SB, test)
test.close()

test=open("results/stot","w")
pickle.dump(Tot_S, test)
test.close()

test=open("results/btot","w")
pickle.dump(Tot_B, test)
test.close()

test=open("results/sbtot","w")
pickle.dump(Tot_SB, test)
test.close()

test=open("results/sadd","w")
pickle.dump(Add_S, test)
test.close()

test=open("results/badd","w")
pickle.dump(Add_B, test)
test.close()

test=open("results/sbadd","w")
pickle.dump(Add_SB, test)
test.close()

print "Task Complete.Thank you."




'''  
=================================================================
	@version  1.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Main module.
=================================================================
'''

import pickle 
import subprocess
import time
import sys

meganame=sys.argv[1]

pname=str(str(subprocess.check_output("pwd",shell=True)).split('/')[-1].rstrip('\\n\''))
print (pname)
num_faults=int(subprocess.check_output("ls | grep -c ^v",shell=True))

subprocess.call("rm -r safe",shell=True)
subprocess.call("rm -r V0outouts",shell=True)
subprocess.call("rm FResults_"+pname+"_"+meganame,shell=True)



subprocess.call("mkdir safe",shell=True)
subprocess.call("mkdir V0outouts",shell=True)

subprocess.call("cp *.c safe/",shell=True)
subprocess.call("cp *.h safe/",shell=True)

real_outputs=[]


res=open("FResults_"+pname+"_"+meganame,"w")
res.write("0 Fault analysis of "+pname+"\n0 Total number of faults: "+str(num_faults)+"\n")


print("####################")
print("Enetring loop Pass")
print("####################")

for suite in [meganame]:
	infile=open("results/"+suite,"rb")
	testcases=pickle.load(infile)
	print(testcases)
	print("####################")
	print("After Pickle")
	print("####################")

	out=open("V0outouts/Vmainoutputs_"+suite,"w")
	
	subprocess.call(["rm",pname])
	subprocess.call("gcc -o "+pname+" "+pname+".c",shell=True)

	print("####################")
	print("After Gcc")
	print("####################")

	for test in testcases:
		print(test)
		try:

			temp=subprocess.run("gtimeout 1 ./"+pname+" "+test,shell=True,stdout=subprocess.PIPE)
			pout=str(temp.stdout)
			
			#pout=str(subprocess.check_output(["./"+pname,test],timeout=5))
		except subprocess.CalledProcessError as e:
			print("Exception occured XXXXXXXXXXXXX",str(e))
			real_outputs.append(str(e))
			out.write(str(e))
		except subprocess.TimeoutExpired as e:
			print("Exception occured XXXXXXXXXXXXX",str(e))
			real_outputs.append(str(e))
			out.write(str(e))
		except Exception as e:
			print ("Doesnt Run.......")
			real_outputs.append(str(e))
			out.write(str(e))

		else:
			real_outputs.append(pout)
			print("Exception did not occured XXXXXXXXXXXXX")
			out.write(pout)

	out.close()

		
	print("####################")
	print("After load zone")
	print("####################")
	

	for i in range(num_faults):
		i+=1
		print("runnning version:",i)
		subprocess.call("cp v"+str(i)+"/* .",shell=True)
		subprocess.call("gcc -o "+pname+" "+pname+".c",shell=True)
		c=0
		fflag=False

		
		for test in testcases:
			
			try:
				temp=subprocess.run("gtimeout 1 ./"+pname+" "+test,shell=True,stdout=subprocess.PIPE)
				temp_out=str(temp.stdout)
			except subprocess.CalledProcessError as e:
				print("Exception occured XXXXXXXXXXXXX",str(e))
				temp_out=str(e)
			except subprocess.TimeoutExpired as e:
				print("Exception occured XXXXXXXXXXXXX",str(e))
				temp_out=str(e)
			except Exception as e:
				print ("Doesnt Run.......")
				real_outputs.append(str(e))
				out.write(str(e))
			print("####\nfisrt one:",real_outputs[c],"\nSecond one:",temp_out,"\n####")
			if not(real_outputs[c]==temp_out):
				res.write("1 "+suite+" reveals fault in v"+str(i)+"\n")
				fflag=True
				print("####\nfisrt one:",real_outputs[c],"\nSecond one:",temp_out,"\n####")
				print("####################")
				print(i,"\t",suite,"\tPass")
				print("####################")

				break
			c+=1
		
		if fflag==False:
				res.write("0 "+suite+" does not reveal fault in v"+str(i)+"\n")
				print("####################")
				print(i,"\t",suite,"\Fail")
				print("####################")

		
		subprocess.call("cp safe/* .",shell=True)
	infile.close()

res.close()

print("Total number of faults: ",num_faults,"\n")













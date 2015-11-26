'''  
=================================================================
	@version  2.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Testset parse module.
=================================================================
'''
import subprocess
import sys

def parse(pname,location):
	
	'''Initializations and clean up'''

	testset={}
	uni=open(location+"universe.txt")
	i=0
	subprocess.call(["rm",pname+".gcno"])
	subprocess.call(["rm","-r",pname+".dsYM"])
	subprocess.call(["rm",pname])
	subprocess.call("gcc -fprofile-arcs -ftest-coverage -g -o "+pname+" "+location+pname+".c",shell=True)

	
	'''
	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	Parsing of statement coverage info
	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	'''

	'''Clean up of files generated after ./ and gcov'''
	subprocess.call(["rm",pname+".c.gcov"])
	subprocess.call(["rm",pname+".gcda"])
	

	'''Runnning each case and storing output'''

	for line in uni:
		i=i+1
		testset[i]=str(line.strip('\n'))
		subprocess.call("./"+pname+" "+str(line),shell=True)

		temp_out=subprocess.check_output("gcov -b -c "+pname,shell=True)
		tot_statements=int(temp_out.split('\n')[1].split()[-1])
		try:
			check=subprocess.check_output("mv "+pname+".c.gcov"+" outputs/"+str(i),shell=True)
			subprocess.call(["rm",pname+".gcda"])
		except Exception as e:
			logging.error(traceback.format_exc())
			print "\n Abrupt exit"
			sys.exit(0)




	'''
	Clean up- Removing obj file, gcno and dsYM created after compiling.
	'''
	uni.close()
	subprocess.call(["rm",pname+".gcno"])
	subprocess.call(["rm","-r",pname+".dsYM"])
	subprocess.call(["rm",pname])
	

	return testset,tot_statements,i

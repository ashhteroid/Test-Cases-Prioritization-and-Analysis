# version  3.0
# author   Ashwin Ramadevanahalli
# title    Software Testing Project
# date	   Nov 27th 2015

This is a python script to select testsuite from a given set of tests for a program.(gcov is used to obtain branch coverage and statement coverage information)

It generates test suits for Branch coverage, Statement coverage and both-each using the following three types of prioritizations:

1.**Random prioritization**- Randomly order the tests in a test suite.


2.**Total branch coverage prioritization.** Prioritize test cases according to the total number of branches they cover simply by sorting them in order of total branch coverage achieved.


3.**Additional branch coverage prioritization.** Iteratively selects a test case that yields the greatest branch coverage, then adjusts the coverage information on subsequent test cases to indicate their coverage of branches not yet covered, and then repeats this process, until all branches covered by at least one test case have been covered.  

##How to run the script:
1. Place all the files in the folder containg your c program.
2. Make sure the folder containingg your program and your program are named same.(Example: 'test/test.c'.)
3. Execute main.py


Note- This is script considers 'Brance Excecuted' metric of gcov for branch coverage. Check out the alternate implementation for 'Branch taken'. 

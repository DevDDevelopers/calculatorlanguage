vthe program is compiled and tasted on linux and python 2.7.1
for other platform and version use at your own risk 
for compiling and running program :
  on linux terminal type: 				   python cl.py
	as an runtime input provide the name:     eg. input.txt
	important to keep inputfile in same directory as of program cl.py 
in the program there are following assuption made in input
* each operator ,number ,bracket are seperated by white space 
* it is assumed that there is no arithmetic error in the input 
   as program does not check for arithmetic error 	
* subtraction operator is seperated by whitespace while negivite sign is not 
*input is terminated my #
sample input :

A = B = 4
C = ( D + 2 ) * -2 
C = D = 2 * -2 
F = C - D
E = D * -10
Z = 10 / 3
#

sample output :

A = 4 B = 4  
C = -4.0  
D = -4.0  
no change
E = 40.0  
Z = 3.33333333333  
   
the zip file contain 4 files :
1 -- cl.py         : the implemetation of calculator language 
2 -- input1.txt  : input provided by HT 
3 -- input2.txt  : my sample input 
4 -- readme.txt  

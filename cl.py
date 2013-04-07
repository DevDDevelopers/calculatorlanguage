#  AUTHOR : MANJEET SINGH
# CALCULATOR LANGUAGE 
# compiled on python 2.7.1
# FOR MORE INFO. READ README.TXT
# the program calculate expressions right associative and all the opreators have same prcedence 

#!/usr/bin/python
   
# ------- variable list -------------------------
var =[]   #list of variables 
op=['+','-','*','/',"="] #list of operators 
rIn=[]  # input list 
v={}  # empty dictonary 

#-------class stack------
#---useful in postfix and postfix calculation ---- 
class stack:
      stk=[];
#default constructor ,push,pop,isempty,empty function wt ususl meaning    
      def __init__(self):
      		x=1
      def push(self,x):
      		self.stk.append(x)
      def pop(self):
      	   if(self.isempty()):
      	   	print "stack is empty cant be poped"
      	   	return False 
      	   else:		
           	return self.stk.pop()
      def isempty(self):
           if not self.stk:
           	return True
           else:
                return False	
      def prstk(self):
      	 	print self.stk
      def empty(self):
      	 	self.stk=[]
                       				

#*******************converting reverse expression into post fix expression******************************
def postfix(x):
    exp=[]
    st=stack()
    l=len(x)
    i=0
    r=""
    st.empty()
    while(i<l):
    	r=x[i]
	if(r in op):
	#checking wather stack is empty  
	    if(st.isempty()):	    	
	    	st.push(r)
	    	#st.prstk()	
	    else:
	        y=st.pop()
	        exp.append(y)
	        st.push(r)	
		#print "operator",r
	#if r is digit ,alphabet or negitive number append in expression 	
	elif(r.isalpha()|r.isdigit()|(r[0]=="-" and len(r)>1) ):
		exp.append(r)
	# if bracket is encountetred evaluate prefix for inside expression 
	elif(r==")"):        
		lst=[]
		while(r!="("):
			i=i+1
			r=x[i]
			if(r=="("):
				continue			
			lst.append(r)
		ls=postfix(lst)
		exp=exp+ls				
			
	i=i+1
# append the leftover operators 			
    while(st.isempty()==False):
	        exp.append(st.pop())	
    return exp	
 #-------------evaluating posfix expression -----------------------
def evaluate(x):
	lst=[]
	#creating a stack
	stk=stack()
	#verifing wather stack is empty 
	stk.empty()
	y = len(x)
	i=0
	# for loop for evaluation of postfix expression 
	for r in x:
		if(r.isalpha()|r.isdigit()|(r[0]=="-" and len(r)>1) ):
			stk.push(r)
		elif(r in op):
			if(stk.isempty()!=True):				
			#if stack is not empty and if we encounter operator we pop the two numbers for assignment 	
				a=str(stk.pop())
				b=str(stk.pop())
				
				if(r=="="):
					if(a.isalpha() and b.isalpha() ):
					#assigning values only to those whose values are changed 
						if(float(v[a])!=float(v[b])):
							v[a]=v[b]
							lst.append(a)
							#pussing assigned value back into stack 
							stk.push(v[a])
							
					elif(a.isalpha()):
						if(float(v[a])!=float(b)):
							v[a]=b
							lst.append(a)
							#pussing assigned value back into stack 
							stk.push(b)
							#print "b= ",b
					elif(b.isalpha()):
						if(float(v[b])!=float(a)):
							lst.append(b)
							#pussing assigned value back into stack 
							stk.push(a)	
										
					
							
					
				else:
					#print "its here"
					#evalusting + - * / operaion and pushing it back to stack 
					if(a.isalpha() and b.isalpha()):
						x=float(v[a])
						y=float(v[b])
						
					elif(a.isalpha()):
						x=float(v[a])
						y=float(b)
						
					elif(b.isalpha()):
						x=float(a)
						y=float(v[b])
					else:
						x=float(a)
						y=float(b)
					
						
					if(r=="+"):
						z=x+y
						#pussing  value back into stack 
						stk.push(z)
					if(r=="-"):
						z=x-y
						#pussing  value back into stack 
						stk.push(z)
					if(r=="*"):
						z=x*y
								
						stk.push(z)    #pussing  value back into stack
					if(r=="/"):
						z=x/y
						stk.push(z)    #pussing  value back into stack				
	return lst;	#returning the list of variables whose values have been changed 				
			
		
	 
     
# ------Open a file-------
r=raw_input("enter file name  :  ")	       
fo = open(r, "r+")
In = fo.read().splitlines();

for r in In:
        #print r
 	for  s in r:
		    if(s.isalpha()):
		    	    var.append(s)
	if(r=="#"):
		break    
	rIn.append(r.split() )	    	
fo.close()
#----------shorting a list in alphabetical order ------------

var=list(set(var))
var.sort()

#a dictonary containing variables and there default value 0
for r in var:
    v.update({r:0})
    

i=0
# reversing the expression operators are calculated right associative 
for r in rIn:
      r=r[::-1]
      rIn[i]=r
      i=i+1
      
# ------list containing postfix expression ----------------
pexp=[]
for r in rIn:
	pexp.append( postfix(r))
	
	
#-------------------- printing output ------------------------
for r in pexp:    
	#print r   
	y=evaluate(r)
	#print v
	if not y:
		print "no change"
		
	else:
		y.sort()
		for i in y:
			print i,"=",v[i] ,
			#print "=",v[i]	
		print " "	

        

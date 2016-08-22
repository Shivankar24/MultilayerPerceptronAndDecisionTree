'''
Created on Nov 15, 2015

@author: srnthknna
'''
import csv
import math
import random
from _random import Random
import copy
import matplotlib.pyplot as g1
import matplotlib.pyplot as g2
import matplotlib.pyplot as g3
import matplotlib.pyplot as g4
import matplotlib.pyplot as g5
list=[]
list0=[]
list10=[]
list100=[]
list1000=[]
list10000=[]
values01=[]
values0=[]
values10=[]
values100=[]
values1000=[]
values10000=[]
classifier0=[]
classifier10=[]
classifier100=[]
classifier1000=[]
classifier10000=[]

xyvals0=[]
xyvals10=[]
xyvals100=[]
xyvals1000=[]
xyvals10000=[]
values01_0=[]
values01_10=[]
values01_100=[]
values01_1000=[]
values01_10000=[]

weights0=[]
weights10=[]
weights100=[]
weights1000=[]
weights10000=[]
numinputs=3
numhidden=6
numoutput=4 

rates=[[20,-7,-7,-7],[-7,15,-7,-7],[-7,-7,5,-7],[-3,-3,-3,-3]]
cmatrix0=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cmatrix10=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cmatrix100=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cmatrix1000=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cmatrix10000=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def hwx(x):
    f=1/(1+math.e**(-x))
    return f


def readsamples():
    global list,list0,list10,list100,list1000,list10000
    with open('sd.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            elem=[]
            for x in row:
                elem.append(float(x))
            list.append(elem)
    list0=copy.deepcopy(list)
    list10=copy.deepcopy(list)	
    list100=copy.deepcopy(list)
    list1000=copy.deepcopy(list)
    list10000=copy.deepcopy(list)
	
class node():
    w=[]
    v=0
    d=0
    b=0
class network():
    input=[]
    hidden=[]
    output=[]
    layers=[]       
    def __init__(self):
        self.input=[]
        self.hidden=[]
        self.output=[]
        self.layers=[] 
        for i in range(numinputs):
            n=node()
            l=[]
            for w in range(numhidden):
                l.append(random.uniform(1,1))
            n.w=l
            self.input.append(n)
        self.input[numinputs-1].v=1
        self.input[numinputs-1].b=1        
        for i in range(numhidden):
            n=node()
            l=[]
            for w in range(numoutput):
                l.append(random.uniform(1,1))
            n.w=l
            self.hidden.append(n)
        self.hidden[numhidden-1].v=1
        self.hidden[numhidden-1].b=1        
        for i in range(numoutput):
            n=node()
            self.output.append(n)   
        self.layers.append(self.input)
        self.layers.append(self.hidden)
        self.layers.append(self.output) 
a0=network()
a10=network()
a100=network()
a1000=network()
a10000=network()  
def weightsread():
    global weights0,weights10,weights100,weights1000,weights10000
    with open('C:\\Users\\srnthknna\\Downloads\\Python3\\dt\\weights0.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            elem=[]
            for x in row:
                elem.append(float(x))
            weights0.append(elem)
    with open('C:\\Users\\srnthknna\\Downloads\\Python3\\dt\\weights10.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            elem=[]
            for x in row:
                elem.append(float(x))
            weights10.append(elem)        
    with open('C:\\Users\\srnthknna\\Downloads\\Python3\\dt\\weights100.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            elem=[]
            for x in row:
                elem.append(float(x))
            weights100.append(elem)        
    with open('C:\\Users\\srnthknna\\Downloads\\Python3\\dt\\weights1000.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            elem=[]
            for x in row:
                elem.append(float(x))
            weights1000.append(elem)        
    with open('C:\\Users\\srnthknna\\Downloads\\Python3\\dt\\weights10000.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            elem=[]
            for x in row:
                elem.append(float(x))
            weights10000.append(elem)


def assignnets():
    global weights0,weights10,weights100,weights1000,weights10000
    count=0
    for l in range(len(a0.layers)-1):
        for i in a0.layers[l]: 
            i.w=weights0[count]
            count=count+1
    count=0
    for l in range(len(a10.layers)-1):
        for i in a10.layers[l]: 
            i.w=weights10[count]
            count=count+1
    count=0
    for l in range(len(a100.layers)-1):
        for i in a100.layers[l]: 
            i.w=weights100[count]
            count=count+1
    count=0
    for l in range(len(a1000.layers)-1):
        for i in a1000.layers[l]: 
            i.w=weights1000[count]
            count=count+1
    count=0
    for l in range(len(a10000.layers)-1):
        for i in a10000.layers[l]: 
            i.w=weights10000[count]
            count=count+1
            


def forproc(a,values,list):    
    for example in list: 
        v=[]
        #print()
        for i in range(numinputs-1):
            a.layers[0][i].v=example[i]
            
        for h in range(1,len(a.layers)):    
            for j in range(len(a.layers[h])):
                sum=0
                for i in a.layers[h-1]:
                    sum=sum+(i.w[j]*i.v) 
                sum=hwx(sum) 
#                if(a.layers[h][j].b!=1):
#                   print("output ",sum)
                if(a.layers[h][j].b==0):    
                    a.layers[h][j].v=sum
                if(h==(len(a.layers)-1)):
                    v.append(a.layers[h][j].v)
        values.append(v)
		

def assignclassifier(values,classifier,classifiedlist):
    for i in values:
        a=max(i)
        b=i.index(a)+1
        classifier.append(b)
    for i in range(len(classifier)):
        classifiedlist[i][2]=classifier[i]

    
def recograte(classifier):
    global list
    correct=0
    for i in range(len(list)):
        if(list[i][2]==classifier[i]):
            correct=correct+1
    print("Total samples ",len(list))
    print("Percentage of correct classification ",(correct/len(list)*100))    

def profitcalc(classifier,cmatrix):
    global list  
    profit=0
    for k in range(len(list)):
        j=int(list[k][2]-1)
        i=int(classifier[k]-1)
        cmatrix[i][j]=cmatrix[i][j]+1
        profit=profit+rates[i][j]
    print("The profit obtained is ",profit)

def confusionmat(cmatrix):
    print("         Confusion Matrix")
    print("Assigned               Actual              ")
    print("            Bolt    Nut    Ring    Scrap ")
    print("Bolt        {0}        {1}       {2}       {3}   ".format(cmatrix[0][0],cmatrix[0][1],cmatrix[0][2],cmatrix[0][3]))
    print("Nut         {0}        {1}       {2}       {3}   ".format(cmatrix[1][0],cmatrix[1][1],cmatrix[1][2],cmatrix[1][3]))
    print("Ring        {0}        {1}       {2}       {3}   ".format(cmatrix[2][0],cmatrix[2][1],cmatrix[2][2],cmatrix[2][3]))
    print("Scrap       {0}        {1}       {2}       {3}   ".format(cmatrix[3][0],cmatrix[3][1],cmatrix[3][2],cmatrix[3][3]))



            
			


def datacreate():
	global xyvals0,xyvals10,xyvals100,xyvals1000,xyvals10000
	xyvals=[]
	for i in range(0,100,1):
		for j in range(0,100,1):
			list=[]
			list.append(i/100)
			list.append(j/100)
			list.append(1)
			xyvals.append(list)
	xyvals0=copy.deepcopy(xyvals)
	xyvals10=copy.deepcopy(xyvals)
	xyvals100=copy.deepcopy(xyvals)
	xyvals1000=copy.deepcopy(xyvals)
	xyvals10000=copy.deepcopy(xyvals)	
def assignclassclassifier(values,list):
    temp=[]
    #print("here",values)
    for i in values:
        a=max(i)
        b=i.index(a)+1
        temp.append(b)
    for i in range(len(temp)):
        list[i][2]=temp[i]

def graph2(region,g1,i):
	freq=[0,10,100,1000,10000]
	points1x=[]
	points1y=[]
	points2x=[]
	points2y=[]
	points3x=[]
	points3y=[]
	points4x=[]
	points4y=[]
	ppoints1x=[]
	ppoints1y=[]
	ppoints2x=[]
	ppoints2y=[]
	ppoints3x=[]
	ppoints3y=[]
	ppoints4x=[]
	ppoints4y=[]
	for elements in region:
		(x,y,z)=elements
		if(z==1):
			points1x.append(x)
			points1y.append(y)
		elif(z==2):
			points2x.append(x)
			points2y.append(y)
		elif(z==3):
			points3x.append(x)
			points3y.append(y)
		else:
			points4x.append(x)
			points4y.append(y)
	for elements in list:
		(x,y,z)=elements
		if(z==1):
			ppoints1x.append(x)
			ppoints1y.append(y)
		elif(z==2):
			ppoints2x.append(x)
			ppoints2y.append(y)
		elif(z==3):
			ppoints3x.append(x)
			ppoints3y.append(y)
		else:
			ppoints4x.append(x)
			ppoints4y.append(y)	
	g1.figure(i)
	g1.title('Region for '+str(freq[i-1]))
	g1.scatter(points1x,points1y,color='blue',label='Bolts')
	g1.scatter(points2x,points2y,color='orange',label='Nuts')
	g1.scatter(points3x,points3y,color='red',label='Rings')
	g1.scatter(points4x,points4y,color='cyan',label='Scrap')
	g1.scatter(ppoints1x,ppoints1y,color='white',label='-Bolts')
	g1.scatter(ppoints2x,ppoints2y,color='black',label='-Nuts')
	g1.scatter(ppoints3x,ppoints3y,color='yellow',label='-Rings')
	g1.scatter(ppoints4x,ppoints4y,color='green',label='-Scrap')
	g1.legend()
	#g1.show()			
			
#for all
weightsread()
assignnets()            
readsamples()
			
print()
print("For 0")
print()
#for 0 weights
forproc(a0,values0,list)	
assignclassifier(values0,classifier0,list0)
recograte(classifier0)
profitcalc(classifier0,cmatrix0)
confusionmat(cmatrix0)
print()
print("For 10")
print()
forproc(a10,values10,list)
assignclassifier(values10,classifier10,list10)	
recograte(classifier10)
profitcalc(classifier10,cmatrix10)
confusionmat(cmatrix10)
print()
print("For 100")
print()
forproc(a100,values100,list)
assignclassifier(values100,classifier100,list100)
recograte(classifier100)	
profitcalc(classifier100,cmatrix100)
confusionmat(cmatrix100)
print()
print("For 1000")
print()
forproc(a1000,values1000,list)
assignclassifier(values1000,classifier1000,list1000)
recograte(classifier1000)
profitcalc(classifier1000,cmatrix1000)
confusionmat(cmatrix1000)
print()
print("For 10000")
print()
forproc(a10000,values10000,list)	
assignclassifier(values10000,classifier10000,list10000)	
recograte(classifier10000)
profitcalc(classifier10000,cmatrix10000)
confusionmat(cmatrix10000)

#for region	

datacreate()
forproc(a0,values01_0,xyvals0)
forproc(a10,values01_10,xyvals10)
forproc(a100,values01_100,xyvals100)
forproc(a1000,values01_1000,xyvals1000)
forproc(a10000,values01_10000,xyvals10000)
#print(values01_0)
#print()
#input()
#print(values01_10)
#print()
#input()
#print(xyvals100)
#print(xyvals1000)
#print(xyvals10000)
assignclassclassifier(values01_0,xyvals0)
assignclassclassifier(values01_10,xyvals10)
assignclassclassifier(values01_100,xyvals100)
assignclassclassifier(values01_1000,xyvals1000)
assignclassclassifier(values01_10000,xyvals10000)
#print(xyvals0)
#print()
#input()
#print(xyvals10)
#print()
#input()
#print(xyvals100)
#print(xyvals1000)
#print(xyvals10000)
graph2(xyvals0,g1,1)
graph2(xyvals10,g1,2)
graph2(xyvals100,g1,3)
graph2(xyvals1000,g1,4)
graph2(xyvals10000,g1,5)
g1.show()

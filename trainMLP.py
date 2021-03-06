'''
Created on Nov 15, 2015

@author: srnthknna
'''
import csv
import math
import random
import copy
from _random import Random
import matplotlib.pyplot as g1
list=[]
values=[]
weights0=[]
weights10=[]
weights100=[]
weights1000=[]
weights10000=[]
def readsamples():
    global list
    with open('sas.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            elem=[]
            for x in row:
                elem.append(float(x))
            list.append(elem)
#print (list)

        
def hwx(x):
    f=1/(1+math.e**(-x))
    return f

class node():
    w=[]
    v=0
    d=0
    b=0
numinputs=3
numhidden=6
numoutput=4 
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
                l.append(random.uniform(-1,1))
            n.w=l
            self.input.append(n)
        self.input[numinputs-1].v=1
        self.input[numinputs-1].b=1        
        for i in range(numhidden):
            n=node()
            l=[]
            for w in range(numoutput):
                l.append(random.uniform(-1,1))
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
a=network()
b=network()
print(len(b.layers))
def findssd(network):
    global values
    temp=copy.deepcopy(network)
    sumsq=0
    for example in list: 
        for i in range(numinputs-1):
            a.layers[0][i].v=example[i]                   
        for h in range(1,len(a.layers)):    
            for j in range(len(a.layers[h])):
                sum=0
                count=0;
                for i in a.layers[h-1]:
                    sum=sum+(i.w[j]*i.v)                     
                    count=count+1
                sum=hwx(sum) 
                if(a.layers[h][j].b==0):    
                    a.layers[h][j].v=sum
                if(h==(len(a.layers)-1)):
                    if ((j)==(example[2]-1) ):
                        sumsq=sumsq+(a.layers[h][j].v-1)**2
                    else:
                        sumsq=sumsq+(a.layers[h][j].v-0)**2
    values.append(sumsq)

def backprop():

    for epoch in range(10001):
        eval=0
        print(epoch)
        if(eval==0 and (epoch==0 or epoch==10 or epoch==100 or epoch==1000 or epoch==10000 )):
                with open('weights'+str(epoch)+'.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    for l in range(len(a.layers)-1):
                        for i in a.layers[l]:
                            writer.writerow(i.w)
        findssd(a)         
        for example in list:
            
            #print(epoch) 
            for i in range(numinputs-1):
                a.layers[0][i].v=example[i]
                    
            for h in range(1,len(a.layers)):    
                for j in range(len(a.layers[h])):
                    sum=0
                    count=0;
                    for i in a.layers[h-1]:
                        sum=sum+(i.w[j]*i.v)                     
                        count=count+1
                    sum=hwx(sum) 
                    if(a.layers[h][j].b==0):    
                        a.layers[h][j].v=sum       

                
            for i in a.layers[len(a.layers)-1]:
                if (a.layers[len(a.layers)-1].index(i)==(example[2]-1) ):
                    i.d=(i.v-1)*(i.v)*(1-i.v)
                else:
                    i.d=(i.v-0)*(i.v)*(1-i.v)
    
            
            for i in range(len(a.layers)-2,0,-1):
                for k in a.layers[i]:
                    if(a.layers[i].index(k)!=(len(a.layers[i])-1)):
                        sum=0
                        count=0
                        for j in a.layers[i+1]:
                            indexj=a.layers[i+1].index(j)
                            indexi=a.layers[i].index(k)
                            sum=sum+(a.layers[i+1][indexj].d*a.layers[i][indexi].w[indexj])
                            count=count+1
                        sum=sum*k.v*(1-k.v)
                        k.d=sum
    
            for i in (0,len(a.layers)-2):
                for j in a.layers[i]:   
                    for k in range(len(j.w)):
                        j.w[k]=j.w[k]-(0.1*a.layers[i+1][k].d*j.v)

            
            eval=eval+1  
           
           
#print("here")
#print(len(values))
#for i in range(len(values)):
#    print(i)
#    print(values[i])
    
def graph1():
    num=[]
    for i in range(len(values)):
        num.append(i+1)
    g1.xlabel(' epoch count ')
    g1.ylabel(' sum of the squared error ')
    g1.scatter(num,values,color='orange')
    g1.plot(num,values)
    g1.show()
	
	
readsamples()               
backprop()    
graph1()
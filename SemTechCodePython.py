import math
import os
import random
import re
import sys
import csv
import itertools
import itertools
from collections import Counter
from itertools import  groupby
from functools import reduce

class PopObj:
    def __init__(self, indi):
        #print("INDI=",indi[0],indi[1],indi[2], indi[3])
        sdi =  ["", "", "", ""]
        #di = str(indi).split(';')
        #print(len(indi), indi)
        for i  in range(0,len(indi)):
            sdi[i] = indi[i]
        #print("SDI=",sdi[0],sdi[1],sdi[2], sdi[3])
        if (sdi[0] == None or sdi[0] == ""):
            self.k = ""
        else:
            self.k = sdi[0]
        if (sdi[3] == None or sdi[3] == ""):
            self.c = ""
        else:
            self.c = sdi[3]
        #print("SDI\t",type(sdi[2]),"\t",sdi[0],"\t",sdi[1],"\t",sdi[2],"\t",sdi[3])
        if (sdi[2] == None):
           self.p = -1 
        elif (sdi[2] == ""):
           self.p = 0  
        else:      
            if (isinstance(sdi[2], str)):
                x = re.findall("\\d+",sdi[2])
                if x:
                    self.p = int(x[0])
                else:
                    self.p = 0
            elif (isinstance(sdi[2], int)):
                self.p = sdi[2]                    
            else:
                self.p=0
    def pmax(x,y):
        #print("PMAX-X=", [x.k,'',x.p,x.c])
        #print("PMAX-Y=", [y.k,'',y.p,y.c])
        if  (x.p > y.p):
            return x
        else:
            return y;
      
    def pmin(x,y):
        #print("PMIN-X=", [x.k,'',x.p,x.c])
        #print("PMIN-Y=", [y.k,'',y.p,y.c])
        if  (x.p < y.p):
            return x
        else:
            #print("PSUM=", [y.k,'',x.p+y.p,x.c])
            return y;
    def psum(x,y):
        #print("PMIN-X=", [x.k,'',x.p,x.c])
        #print("PMIN-Y=", [y.k,'',y.p,y.c])
        #print("PSUM=", [x.k,'',x.p+y.p,x.c])
        return PopObj([x.k,'',x.p+y.p,x.c])
    def __str__(self):
        return str((self.k, self.p, self.c))
 
    def __repr__(self):
        return repr((self.k, self.p, self.c))


class LineStreamProc:
    def fileLines(self,file):
      
            self.polist = []
            objs = []  
            
            with open(file, newline = '') as csvfile :
                freader = csv.reader(csvfile, delimiter = ';',quoting=csv.QUOTE_NONE)
                #freader.read();
                for line in freader:
                    #print(type(line), line);
                    popobj = PopObj(line)
                    #print("PPP=",popobj.k, popobj.c, popobj.p);
                    #print(str(popobj));
                    objs.append(popobj)
                    sys.stderr.flush()
                    sys.stdout.flush()
            func=lambda x : x.c
            sobjs = sorted(objs,  key=func)
            # for xx in objs:
                # print("XX=",xx.k, xx.c, xx.p);
            return sobjs
            #return self.poslist;

      # Employubg Stream of lines from input file get Max Population for Each Department
    def getPopulationByDept(self,lines):
        groups = {}
        maxPop = {}
        minPop = {}
        sumPop = {}
        uniquekeys=[]
        #print(lines)
        print("NUM RECIRDS = ",len(lines)+1);
        sfunc=lambda x : x.c
        ##sorted(objs,  key=sfunc)
        for k, g in groupby(lines, key=sfunc):
            groups[k] = list(g)
            uniquekeys.append(k)
            #print("K, G=", k, groups[k], "\n")
            # for x in groups[k]:
                # print("KEY=",k,"GROUP=",x,"\n");
        for k in groups.keys():
            #print(str(groups[k]))
            sys.stderr.flush()
            sys.stdout.flush()
            maxPop[k] = reduce(lambda x, y: PopObj.pmax(x,y),  groups[k])
            sumPop[k] = reduce(lambda x, y: PopObj.psum(x,y),  groups[k])
            minPop[k] = reduce(lambda x, y: PopObj.pmin(x,y),  groups[k])
       
        #print("MINIPOP: ", minPop);
        popmin = {}
        for x in minPop.keys():
            #print(minPop[x])
            a = minPop[x].k
            b = minPop[x].c 
            c = minPop[x].p
           
            if c in popmin:
                popmin[c].append(b)
            else:
                popmin[c] = []
                popmin[c].append(b)
        popMini = min(sorted(popmin.keys()))
        for k in sorted(groups.keys()):
            print("Department " , k , "Sum Population " , sumPop[k].p , ", Max Population  " , maxPop[k].p)
        print(popMini, " is the Minimum Population for cities " , popmin[popMini], " " )
        return  groups, minPop, maxPop, sumPop

if __name__ == "__main__":
    lineproc = LineStreamProc();
    lines = lineproc.fileLines(sys.argv[1])
    lineproc.getPopulationByDept(lines[1:])
       




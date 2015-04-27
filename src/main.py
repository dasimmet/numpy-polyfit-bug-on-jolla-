import pyotherside


def helloWorld():
    print("hi this is Python")

def testPolyFit():
    import numpy as np
    import pdb
    x=np.array([1,2,3,4,5])
    y=np.array([100,50,20,30,0])
    fit=pdb.runcall(np.polyfit,x,y,1,w=y)
    print(x,y,fit)

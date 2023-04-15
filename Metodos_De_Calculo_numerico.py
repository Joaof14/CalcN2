import numpy as np
from sympy import  expand, Symbol
import warnings



np.seterr(all = 'warn')

warnings.filterwarnings('error')

xS = Symbol('x')



class LinearSystem():
    def __init__(self, Inpa,Inpb, pr = '0.0000000001'):
        self.MatrizA = np.array(Inpa)
        self.MatrizB = np.array(Inpb)
        da = np.shape(self.MatrizA)
        db = np.shape(self.MatrizB)
        if da[0] != db:
            IndexError
        x = np.zeros(self.MatrizB.size, dtype=float)
        p = float(pr)
        f = open("Resol.txt", 'w')
        f.write("Matriz A|B: \n") 
        f.close()
        self.outputMatrizesAB(mb = True)
    
    def outputMatrizesAB(self, mb):
        for i in range(len(self.MatrizA)):
            outputM = ''
            for j in range(len(self.MatrizA[i])):
                outputM += str(self.MatrizA[i][j]) + ' '
            if mb:
                outputM += '|' + str(self.MatrizB[i])
            outputM += '\n'
            with open('Resol.txt', 'a') as f:
                f.write(outputM)

    
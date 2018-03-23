'''
Created on Dec 3, 2017

@author: Radu
'''

import re 

class ObjReader:
    
    def __init__(self):
        self._vertices = []
        self._edges = []
        self._faces = []
        
        
    def read(self, fileName):
        
        f = open(fileName, 'r')
        
        for line in f:
            
            
            #processed line
            procLine = re.sub(' +',' ', line)
            
            if procLine[:1] == 'v ':
                
                sL = procLine.split(' ')
                
                print sL
                
                self._vertices.append((float(sL[1]), float(sL[2][2:]), float(sL[3][2:-1]))) 
            
            if procLine[:1] == 'f ':
                
                sL = procLine.split(' ')
                
                self._faces.append((int(sL[1]) - 1, int(sL[2][1:]) - 1,  int(sL[3][1:-1]) - 1))
                
                self._edges.append((int(sL[1]) - 1, int(sL[2][1:]) - 1))
                self._edges.append((int(sL[2][1:]) - 1, int(sL[3][1:-1]) - 1))
                self._edges.append((int(sL[1]) -1 , int(sL[3][1:-1]) - 1))
                
        
    def getVertices(self):
        return tuple(self._vertices)

    def getEdges(self):
        return tuple(self._edges)

    def getFaces(self):
        return tuple(self._faces)


'''
Created on Dec 8, 2017

@author: Radu
'''

from Shapes.Repo import Repo
from Shapes.Shape import ConnectorCube


class MapCreator:
    
    def __init__(self, fileName):
        f = open(fileName)
        
        self._mat = []    
        for row in f:
            
            matRow = []
            
            for i in row.split(' '):
                matRow.append(int(i))
            
            self._mat.append(matRow)
                        
    
    
    def createRepo(self):
        
        repo = Repo()
    
        for i in range(1, 9):
            for j in range(1, 9):
                
                a = None 
                missingFaces = []
                
                if self._mat[i][j] == 1:
                    
                    x = 2 * (j - 2)
                    z = 2 * (10 - i - 2)
                    
                    print self._mat[i][j], i, j
                    
                    if self._mat[i + 1][j] == 1:
                        missingFaces.append(0)
                        
                    if self._mat[i - 1][j] == 1:
                        missingFaces.append(1)
                       
                    if self._mat[i][j + 1] == 1:
                        missingFaces.append(4)
                        
                    if self._mat[i][j - 1] == 1:
                        missingFaces.append(5)
                    
                    a = ConnectorCube([missingFaces, 'Wall'])
                    a.addVector((x, 0, z))
                    repo.addGround(a)
                
        return repo


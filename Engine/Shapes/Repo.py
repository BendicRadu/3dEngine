'''
Created on Sep 7, 2017

@author: Radu
'''

from Shapes.Shape import BasicCube
from Shapes.Shape import Shape
from copy import deepcopy

from math import floor

class Repo:
    
    def __init__(self):
        self._objList = []
        self._groundList = []
    
    def __str__(self):
        return str(self._objList)
    
    def __repr__(self):
        for obj in self._objList:
            print str(obj) + "\n"
    
    def add(self, newObj):
        self._objList.append(newObj)
        
    def addGround(self, newObj):
        self._objList.append(newObj)
        self._groundList.append(newObj)
    
    
    def getGround(self, pos):

        pos = tuple(pos)
        
        for g in self._groundList: 
            
            if g.isInside(pos):
                return g
      
    def remove(self, Id):        
        for obj in self._objList:
            if obj._id == Id:
                del obj
    
    def removeByVerts(self, verts):        
        for obj in self._objList:
            if obj._verts == verts:
                del obj
    
    def createRowOfShapes(self, ShapeParams, nrOfShapes, dir = 0):
        '''
        Function to add a row of shapes to the repo
        @startPos@ Starting position
        @nrOfCubes@ explicit
        @dir@ direction of row:
                - 0 horizontal x
                - 1 vertical y 
                - 2 depth z
        '''
        vect = [0, 0, 0]
        a = Shape(ShapeParams)
        for i in range(nrOfShapes):
            
            other = deepcopy(a)
            
            
            k = a.getSize()[dir]
            vect[dir] += k 
            otherVect = tuple(vect) 
            
            other.addVector(otherVect)
            self.addGround(other)
            
            
        
        
        

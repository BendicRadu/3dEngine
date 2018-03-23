'''
Created on Sep 7, 2017

@author: Radu
'''
from decimal import _Infinity
from copy import deepcopy
import math
from Shapes.ObjReader import ObjReader



def addVectors(v1, v2):
    
    v1 = list(v1)
    v2 = list(v2)
    
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])
    

def distanceBetweenPoints(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[1] - p2[1]) ** 2 )


def scaleVector(vect, scale):
    
    aux = list(vect)
    
    for i in range(3):
        aux[i] *= scale
        
    return tuple(aux)

def colissionWithFace(faceVerts, pos, speed):
    
    xc = sum(x for (x, y, z) in faceVerts) / len(faceVerts)
    yc = sum(y for (x, y, z) in faceVerts) / len(faceVerts)
    zc = sum(z for (x, y, z) in faceVerts) / len(faceVerts)
    
    if ( pos[0] + speed >= xc):
        return True
    
    if ( pos[1] + speed >= yc):
        return True
    
    if ( pos[2] + speed >= zc):
        return True
    
    return False
    

class Shape:
    
    '''
    @argList
    [0] - verts
    [1] - faces
    [2] - edges
    [3] - id
    '''
    
    def __init__(self, argList):
        self._verts = argList[0] 
        self._faces = argList[1]
        self._edges = argList[2]
        try:
            self._id = str(argList[3]) 
        except IndexError:
            self._id = None
    
    def __str__(self):
        return str(self._verts) + "\n" + str(self._faces) + "\n" + str(self._edges) + "\n"
        
        
    def __repr__(self):
        return str(self._verts) + "\n" + str(self._faces) + "\n" + str(self._edges) + "\n"
        
        
    def __rmul__(self, factor):
        vect = list(self._verts)
        newList = []
        row = []
        for pos in vect:
            k = list(pos)
            for i in k:
                i *= factor
                row.append(i)
            newList.append(tuple(row))
            row = []
        
        newList = tuple(newList)
        self._verts = newList
        self._id += str(factor)
        
        return self
    
    def __radd__(self, factor):
        vect = list(self._verts)
        newList = []
        row = []
        for pos in vect:
            k = list(pos)
            for i in k:
                i += factor
                row.append(i)
            newList.append(tuple(row))
            row = []
        
        newList = tuple(newList)
        self._verts = newList
        
        return self
    

    
    def addVector(self, otherVect):
        vect = list(self._verts)
        otherList = list(otherVect)
        
        newList = []
        row = []
        for pos in vect:
            k1 = list(pos)
            for i in range(len(k1)):
                k1[i] += otherList[i]
                row.append(k1[i])
            newList.append(tuple(row))
            row = []
        
        newList = tuple(newList)
        self._verts = newList
       
    def scaleVector(self, scale):

        
        vect = list(self._verts)
        rez = []
        
        for i in range(len(vect)):
            
            vert = [0, 0, 0]
            
            for j in range(3):
                vert[j] = vect[i][j] * scale
                
            rez.append(vert)
            
        self._verts = tuple(rez)

    
    def removeVector(self, otherVect):
        vect = list(self._verts)
        otherList = list(otherVect)
        
        newList = []
        row = []
        for pos in vect:
            k1 = list(pos)
            for i in range(len(k1)):
                k1[i] -= otherList[i]
                row.append(k1[i])
            newList.append(tuple(row))
            row = []
        
        newList = tuple(newList)
        self._verts = newList
        
        
    def getSize(self):
                
        vect = list(self._verts)
        
        xMin = _Infinity
        xMax = -_Infinity
        
        yMin = _Infinity
        yMax = -_Infinity
        
        zMin = _Infinity
        zMax = -_Infinity
        
        
        for pos in vect:
            k1 = list(pos)
            if k1[0] < xMin: xMin = k1[0]
            if k1[0] > xMax: xMax = k1[0]
            if k1[1] < yMin: yMin = k1[1]
            if k1[1] > yMax: yMax = k1[1]
            if k1[2] < zMin: zMin = k1[2]
            if k1[2] > zMax: zMax = k1[2]
            
        return [xMax - xMin, yMax - yMin, zMax - zMin]
    
    def getMiddle(self):
        
        
        x, y, z = 0, 0, 0
        
        for vert in self._verts:
            x += vert[0]
            y += vert[1]
            z += vert[2]
        
        
        return [x / 8, y / 8, z / 8]
    
    def isInside(self, pos):
        
        vect = list(self._verts)
        
        xMin = _Infinity
        xMax = -_Infinity
        
        yMin = _Infinity
        yMax = -_Infinity
        
        zMin = _Infinity
        zMax = -_Infinity
        
        for point in vect:
            k1 = list(point)
            if k1[0] < xMin: xMin = k1[0]
            if k1[0] > xMax: xMax = k1[0]
            if k1[1] < yMin: yMin = k1[1]
            if k1[1] > yMax: yMax = k1[1]
            if k1[2] < zMin: zMin = k1[2]
            if k1[2] > zMax: zMax = k1[2]
        
        
        if (pos[0] > xMin and pos[0] < xMax) and (pos[1] > yMin and pos[1] < yMax) and (pos[2] > zMin and pos[2] < zMax):
            return True
        return False
        
         
        
    
    @staticmethod
    def distanceBetweenPoints(a1, b1):
        a = list(a1)
        b = list(b1)
         
        vSum = 0
         
        for i in range(len(a)):
            vSum += (a[i] + b[i]) ** (a[i] + b[i])
            
        return int(math.sqrt(vSum))
        
            
            
class BasicCube(Shape):
    '''
    @ArgList
    [0] - verts
    [1] - edges
    [2] - faces
    [3] - id 
    '''
    
    def __init__(self, argList = None):
        if argList == None:
         
            verts = ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
            edges = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))
            faces = ((0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6),  (1, 2, 6, 5) )
        
            Shape.__init__(self, [verts, edges, faces, None])        
        else:
            Shape.__init__(self, [argList[0], argList[1], argList[2]])
            
class BasicPyramid(Shape):
    
    def __init__(self, argList = None):
        if argList == None:
             
            verts = ((0, 1, 0), (-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1))
            edges = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4))
            faces = ((0, 1, 2), (0, 2, 3), (0, 3, 4), (1, 2, 3, 4))
            
            Shape.__init__(self, [verts, edges, faces, None])        
        else:
            Shape.__init__(self, [argList[0], argList[1], argList[2]])
            
class BasicSphere(Shape):
    
    
    def __init__(self, argList = None):
        if argList == None:                   
            oR = ObjReader()
            oR.read("C:\Users\Radu\workspace\RedI\Objects\Cheap Sphere.txt")
            
            Shape.__init__(self, [oR.getVertices(), oR.getEdges(), oR.getFaces()])
        else:
            Shape.__init__(self, [argList[0], argList[1], argList[2]])
         
    
class ImportShape(Shape):
    
    def __init__(self, fileName):
        
        oR = ObjReader()
        oR.read(fileName)
        
        Shape.__init__(self, [oR.getVertices(), oR.getEdges(), oR.getFaces()])
    

class Projectile(Shape):
    '''
    @argList
    [0] - pos
    [1] - velocity
    [2] - id
    '''
    
    def __init__(self, argList):
                
        self._pos = argList[0]
        self._moveVector = argList[0]
        self._velocity = argList[1]
                
        verts = ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
        edges = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))
        faces = ((0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6),  (1, 2, 6, 5) )
    
        Shape.__init__(self, [verts, edges, faces, argList[2]])

        self.addVector(argList[0])
    
    
    def hasPassedThrough(self, pos):
        
        midPos = self.getMiddle()
        initialPos = self._pos
        
        xMin = _Infinity
        xMax = -_Infinity
        
        yMin = _Infinity
        yMax = -_Infinity
        
        zMin = _Infinity
        zMax = -_Infinity
        
        for x, y, z in (midPos, initialPos):
            if x < xMin: xMin = x
            if x > xMax: xMax = x
            if y < yMin: yMin = y
            if y > yMax: yMax = y
            if z < zMin: zMin = z
            if z > zMax: zMax = z
        
        
        if (xMin < pos[0] and pos[0] < xMax) and (yMin < pos[1] and pos[1] < yMax) and (zMin < pos[2] and pos[2] < zMax):
            return True
        return False
        
        
        
    
    
    
class ConnectorCube(Shape):
    
    def __init__(self, argList):
        
        '''
        @argList
        [0] - missing faces (list)
            - 0 (0 1 2 3) ( front )
            - 1 (4 5 6 7) ( back )
            - 2 (0 1 5 4) ( floor ) 
            - 3 (2 3 7 6) ( ceiling )
            - 4 (1 2 6 5) ( right )
            - 5 (0 3 7 4) ( left )
        [1] - id
        '''
        
        verts = ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
        edges = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))
        faces = ((0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6),  (1, 2, 6, 5), (0, 3, 7, 4) )

    
        faces = list(faces)
    
        k = 0
           
        for i in argList[0]:    
            del faces[i - k]
            k += 1
            
        faces = tuple(faces) 
        
    
        Shape.__init__(self, [verts, faces, edges, argList[1]])
    
    

class PlayerCube(Shape):
    '''
    @argList
    [0] - pos
    [1] - id
    '''
    
    def __init__(self, argList):
        
        self._pos = argList[0]        
        
        verts = ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
        edges = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))
        faces = ((0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6),  (1, 2, 6, 5) )
    
        Shape.__init__(self, [verts, edges, faces, argList[1]])
        self.addVector(self._pos)
        
        
    def setPos(self, pos):
        
        self.scaleVector(2)
        
        auxVect = list(self._pos)
        
        auxVect[0] = - auxVect[0]
        auxVect[1] = - auxVect[1]
        auxVect[2] = - auxVect[2]
         
        self.addVector(tuple(auxVect))
        self.addVector(pos)
        
        self._pos = pos
    
    
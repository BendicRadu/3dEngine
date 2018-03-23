'''
Created on Sep 6, 2017

@author: Radu
'''


import pygame
from Camera import Camera
from Shapes.Shape import Shape, BasicCube, BasicPyramid, BasicSphere,\
    ImportShape, colissionWithFace, scaleVector, distanceBetweenPoints,\
    addVectors, Projectile, ConnectorCube, PlayerCube
from Shapes.Repo import Repo
from copy import deepcopy
from time import sleep
import math
from numpy.random.mtrand import randint

import thread
from Shapes.Utils import Location
from MapCreator import MapCreator
         
class Engine:
    
    def __init__(self, width = 800, height = 600, Repo = None):
        pygame.init()
        self._screen = pygame.display.set_mode((width, height))
        
        self._repo = Repo
        
        
        pygame.event.get()
        pygame.mouse.get_rel()
        pygame.mouse.set_visible(0)
        pygame.event.set_grab(1)
        
        
        #Screen height and width 
        self._sW = width
        self._sH = height 
        
        
        #Coords adjusted to center
        self._cX = self._sW // 2
        self._cY = self._sH // 2
        
        
        self._done = False
        self._clock = pygame.time.Clock()
        
        self._points = []
        
        self._radian = 0
            
        self.loop()
    
    
    def checkBullteCollision(self, obj):
    
        d = True
        
        for ground in self._repo._groundList:
            if ground.isInside(obj.getMiddle()):
                d = False
                
        if d:
            del self._repo._objList[self._repo._objList.index(obj)]
             
        
    
    def createBulet(self, event):
        
        if event.type == pygame.MOUSEBUTTONUP:
            
            scale = 0.01
            
            x = math.sin(cam._rot[0])
            z = math.cos(cam._rot[0])
            
            y = math.sin(cam._rot[1])
            z1 = math.cos(cam._rot[1])
            
            vect = (x + cam._pos[0] / scale, y + cam._pos[1] / scale ,  z + z1 + cam._pos[2]/ scale)
            
            aux = [0, 0, 0]
            
            if aux == [0, 0, 0]:
                aux[0] = - x
                aux[1] = - 1.5 * y
                aux[2] = - z
            
            b = Projectile([deepcopy(vect), deepcopy(tuple(aux)), "bullet"])
            b.scaleVector(scale)
            

            self._repo.add(b)
        
    
    def loop(self):
        
        
        
        p1 = PlayerCube([(0, 0, 0), 'player1'])
        p1.scaleVector(0.5)
        
        p2 = PlayerCube([(0, 0, 0), 'player2'])
        p2.addVector((12, 0, 14))
        p2.scaleVector(0.5)
        
        self._repo.add(p1)
        self._repo.add(p2)
        
        
        while not self._done:
            
            
            
            p1.setPos(cam._pos)
            
            self._screen.fill((0, 0, 0))
            
            dt = 0.001
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self._done = True
                    cam.event(event)
                    self.createBulet(event)
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self._done = True
            
            faceList = []; depth = []
            
            canMove = True
            
    
            pos = list(deepcopy(cam._pos))
            pos = tuple(pos)
            
            s = dt * 150
            
            x = s * math.sin(cam._rot[0])
            z = s * math.cos(cam._rot[0])
        
            groundCluster = Location()
            
            groundCluster._center = self._repo.getGround(pos)
            
            groundCluster._up = self._repo.getGround([pos[0] + x, pos[1], pos[2] + z])
            groundCluster._down = self._repo.getGround([pos[0] - x, pos[1], pos[2] - z])
            
            groundCluster._left = self._repo.getGround([pos[0] - z, pos[1], pos[2] + x])
            groundCluster._right = self._repo.getGround([pos[0] + z, pos[1], pos[2] - x])
            
            
            
            for obj in self._repo._objList:
                
                p1.addVector(cam._pos)
                
                if obj._id == 'bullet':
                    
                        
                    moveVect = scaleVector(obj._velocity, 0.2)
                    aux = list(moveVect)
                   
                    aux[0] = -aux[0]
                    aux[1] = -aux[1]
                    aux[2] = -aux[2]
                    
                    aux = tuple(aux)
                    obj.addVector(aux)
                                       
                    
                    if (distanceBetweenPoints(obj.getMiddle(), cam._pos) > 5):
                        del self._repo._objList[self._repo._objList.index(obj)]
                         
                    
                    try:
                        index = self._repo._objList.index(p1)                                   
                        if self._repo._objList[index].isInside(obj.getMiddle()):
                            del self._repo._objList[index]
                            
                        index = self._repo._objList.index(p2)                                   
                        if self._repo._objList[index].isInside(obj.getMiddle()):
                            del self._repo._objList[index]
                            
                    except Exception: pass
                    
                    self.checkBullteCollision(obj)
                
                vertList = []; screenCoords = [];
             
           
                for x, y, z in obj._verts:
                    
                    x, z = cam.rotate((x, z), (self._sW, self._sH), "y")   
                    y, z = cam.rotate((y, z), (self._sW, self._sH), "x")
                    
                    x -= cam._pos[0] 
                    y -= cam._pos[1]
                    z -= cam._pos[2]
                    
                    vertList += [(x, y, z)]
                    
                    if z <= 0 : z = 0.0000001
                    
                    f = 400 /  z
                    x *= f
                    y *= f
                    
                    if x > self._sW: x = self._sW  + self._cX
                    if x < -self._sW: x = -self._sW - self._cX
                    
                    if y > self._sH: y = self._sH  + self._cY
                    if y < -self._sH: y = -self._sH - self._cY
                    
                    
                    screenCoords += [(self._cX + int(x), self._cY + int(y))]
                
                for face in obj._faces:
                    
                    for i in face:
                        
                        
                        coords = [screenCoords[i] for i in list(face)]    
                        '''
                        if colissionWithFace(vertList, cam._pos, dt * 200):
                            canMove = False
                        else:
                            canMove = True
                        '''
                        
                        
                        if obj._id == 'bullet':
                            faceList += [(coords, [255, 0, 0])]
                        
                        elif obj._id == 'player1':
                            faceList += [(coords, [0, 0, 255])]
                            
                        elif obj._id == 'player2':
                            faceList += [(coords, [0, 255, 255])]    
                        
                        else:
                            faceList += [(coords, [255, 255, 255])]
                        
                        
                        depth += [sum(sum(vertList[j][i] for j in face) ** 2 for i in range(3))]
                        
                    
            
            order = sorted(range(len(faceList)), key = lambda i: depth[i], reverse = 1)
            
            k = 200
            
            for i in order:

                try:
                    
                    color = [255, 255, 255]
                    
                    pygame.draw.polygon(self._screen, tuple(color), faceList[i][0], 0)
                    
                    if k > 10:
                        k -= 1
    
                    
                       
                except Exception as e:
                    print e
                
            pygame.draw.line(self._screen, (255, 255, 255), (self._cX - 10, self._cY), (self._cX + 10, self._cY), 2)
            pygame.draw.line(self._screen, (255, 255, 255), (self._cX, self._cY - 10), (self._cX, self._cY + 10), 2)
                
                
            pygame.display.flip()  
            key = pygame.key.get_pressed() 
            
            if canMove:
                
                try:
                    cam.update(dt, key, 150, groundCluster)
                except AttributeError as e:
                    cam._pos[1] += 1
   
   

repo = MapCreator("C:\Users\Radu\workspace\RedI\Maps\Map1").createRepo()
#repo = Repo()

'''
b = ConnectorCube([[0, 1, 2, 3], 'left'])
repo.createRowOfShapes([b._verts, b._edges, b._faces], 9, 2)

c = ConnectorCube([[0, 4], 'Right'])
repo.createRowOfShapes([c._verts, c._edges, c._faces], 9, 0)

d = ConnectorCube([[0, 1, 2, 4], 'Right'])
d.addVector((2, 0, 0))
repo.createRowOfShapes([d._verts, d._edges, d._faces], 9, 2)
'''


cam = Camera(pos = (0, 0, 0))
a = Engine(Repo = repo)    

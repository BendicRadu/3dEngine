'''
Created on Sep 7, 2017

@author: Radu
'''




import pygame
import math
from copy import deepcopy



class Camera:

    def __init__(self, pos = (0, 0, 0), rot = (0, 0, 0)):
        self._pos = list(pos)
        self._rot = list(rot)
        
    def getCameraDir(self):
        
        camDir = [1, 1, -1]
        
        eqX = camDir[0]
        eqY = camDir[1]
        eqZ = camDir[2]
        
        camDir[1] = eqY * math.cos(self._rot[1]) - eqY * math.sin(self._rot[1])
        camDir[2] = eqZ * math.sin(self._rot[1]) + eqZ * math.cos(self._rot[1])
        
        camDir[0] = eqX * math.cos(self._rot[0]) - eqY * math.sin(self._rot[0])
        camDir[2] = eqZ * math.sin(self._rot[0]) + eqZ * math.cos(self._rot[0])
        
        
        return tuple(camDir)
        
    def rotate(self, pos, screenSize, axis):
    
        x, y = pos[0], pos[1]
            
        xEq = x 
        yEq = y 
        
        if axis == "y":
            
            xEq -= self._pos[0]
            yEq -= self._pos[2]
            
            x = xEq * math.cos(self._rot[0]) - yEq * math.sin(self._rot[0])
            y = xEq * math.sin(self._rot[0]) + yEq * math.cos(self._rot[0])
           
            x += self._pos[0]
            y += self._pos[2]
        
            return x, y 
        
        else:
            
            xEq -= self._pos[1]
            yEq -= self._pos[2]
            
            x = xEq * math.cos(self._rot[1]) - yEq * math.sin(self._rot[1])
            y = xEq * math.sin(self._rot[1]) + yEq * math.cos(self._rot[1])
          
          
            x += self._pos[1]
            y += self._pos[2]
            
            return x, y 
        
        
        
    def event(self, event):
        
        if event.type == pygame.MOUSEMOTION:
                    
            x, y = event.rel
            
            x, y = float(x), float(y)
                                    
            x /= 800
            y /= 800
        
            self._rot[0] += x
            self._rot[1] += y
    
    
    def validateMove(self, dt, speed, key, locationObject):
    
        auxPos = deepcopy(self._pos)
    
        s = dt * speed
        x, z = s * math.sin(self._rot[0]), s * math.cos(self._rot[0])
          
        '''
        if key[pygame.K_SPACE]:
            auxPos[1] -= s
            if not locationObject._center.isInside(auxPos):
                return False
                  
        elif key[pygame.K_RSHIFT]:
            auxPos[1] += s
            if not locationObject._center.isInside(auxPos):
                return False
        '''
    
        if key[pygame.K_w] and key[pygame.K_a]:
            auxPos[0] += x; auxPos[2] += z;
            
            if not locationObject._center.isInside(auxPos) and locationObject._up == None:
                return False 
    
            auxPos[0] -= x; auxPos[2] -= z
            
            auxPos[0] -= z; auxPos[2] += x
            
            if not locationObject._center.isInside(auxPos) and locationObject._left == None:
                return False 
        
        if key[pygame.K_w] and key[pygame.K_d]:
            auxPos[0] += x; auxPos[2] += z;
            
            if not locationObject._center.isInside(auxPos) and locationObject._up == None:
                return False 
    
            auxPos[0] -= x; auxPos[2] -= z
            
            auxPos[0] += z; auxPos[2] -= x
            
            if not locationObject._center.isInside(auxPos) and locationObject._right == None:
                return False 
            
        
        if key[pygame.K_s] and key[pygame.K_a]:
            auxPos[0] -= x; auxPos[2] -= z;
            
            if not locationObject._center.isInside(auxPos) and locationObject._down == None:
                return False 
    
            auxPos[0] += x; auxPos[2] += z
            
            auxPos[0] -= z; auxPos[2] += x
            
            if not locationObject._center.isInside(auxPos) and locationObject._left == None:
                return False 
        
        if key[pygame.K_s] and key[pygame.K_d]:
            auxPos[0] += x; auxPos[2] += z;
            
            if not locationObject._center.isInside(auxPos) and locationObject._down == None:
                return False 
    
            auxPos[0] -= x; auxPos[2] -= z
            
            auxPos[0] += z; auxPos[2] -= x
            
            if not locationObject._center.isInside(auxPos) and locationObject._right == None:
                return False 
        
        if key[pygame.K_w] :
            auxPos[0] += x; auxPos[2] += z;
            
            if not locationObject._center.isInside(auxPos) and locationObject._up == None:
                return False 
           
        elif key[pygame.K_s]:
            auxPos[0] -= x; auxPos[2] -= z; 
            
            if not locationObject._center.isInside(auxPos) and locationObject._down == None:
                return False 
 
                
        elif key[pygame.K_a]:     
            auxPos[0] -= z; auxPos[2] += x; 
            
            if not locationObject._center.isInside(auxPos) and locationObject._left == None:
                return False 
        
        
        elif key[pygame.K_d]:
            auxPos[0] += z; auxPos[2] -= x; 
            
            if not locationObject._center.isInside(auxPos) and locationObject._right == None:
                return False 
 
        return True
    
        
        
    
    
    def update(self, dt, key, speed, locationObject):
        
        s = dt * speed
        
        x, z = s * math.sin(self._rot[0]), s * math.cos(self._rot[0])
        
        if self.validateMove(dt, speed, key, locationObject):
            '''
            if key[pygame.K_SPACE]: self._pos[1] -= s 
            if key[pygame.K_LSHIFT]: self._pos[1] += s
            '''
            if key[pygame.K_w]: self._pos[0] += x; self._pos[2] += z; 
            if key[pygame.K_s]: self._pos[0] -= x; self._pos[2] -= z; 
                    
            if key[pygame.K_a]: self._pos[0] -= z; self._pos[2] += x 
            if key[pygame.K_d]: self._pos[0] += z; self._pos[2] -= x         
                    
    

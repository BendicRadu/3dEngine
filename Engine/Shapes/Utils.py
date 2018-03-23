'''
Created on Dec 7, 2017

@author: Radu
'''



class Location:
    
    def __init__(self, center = None, up = None, left = None, back = None, right = None):
        self._center = center
        self._up = up
        self._left = left
        self._back = back
        self._right = right


    def __repr__(self):
        return "Center: " + str(self._center) + '\n' +\
            "Up: " + str(self._up) + '\n'  + \
            "Down: " + str(self._down) + '\n'  + \
            "Left: " + str(self._left) + '\n'  + \
            "Right: " + str(self._right) + '\n' 
    
    
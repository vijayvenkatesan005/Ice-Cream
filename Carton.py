#Vijay Venkatesan
# 11/26/2022

import math #this gives you pi
import Scoop

class Carton:
    ''' Class: Carton
        Attributes: contains
        Methods: hasEnoughFor, remove'''
    
    def __init__(self, radius, height):
        ''' Constructor
            Parameters:
                self
                radius - radius of a carton
                height - height of a carton'''
        
        if radius > 10:
            self.radius = 10
        elif radius <= 0:
            self.radius = 1
        else:
            self.radius = radius
        
        if height > 10:
            self.height = 10
        elif height <= 0:
            self.height = 1
        else:
            self.height = height
        
        
        self.contains = math.pi * self.radius**2 * self.height

    def hasEnoughFor(self, scoop:Scoop.Scoop):
        ''' hasEnoughFor
            Parameters:
                self
                scoop - the Scoop to be used on the Carton
            Return:
                whether or not the Carton contains enough to make a Scoop'''
        
        return self.contains >= scoop.volume()

    def remove(self, scoop:Scoop.Scoop):
        ''' remove
            Parameters:
                self
                scoop - the Scoop to be used on the Carton
        '''

        self.contains -= scoop.volume()
        if self.contains < 0:
            self.contains = 0
    
    def get_contains(self):
        '''
        get_contains
        Parameters:
            self
        Return:
            how much ice cream is in the carton
        '''
        return self.contains


    
    
        
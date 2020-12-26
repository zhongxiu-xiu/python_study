# -*-coding:UTF-8 -*-

class Animal():
    def _init_(self):
        self.eye=''
        self.ear=''
        
    def chi(self):
        print('动物吃')
        
    def pao(self):
        print('动物跑')
        
class Cat(Animal):
    def _init_(self):
        self.weiba=None
        
    def zhua(self):
        print('抓老鼠')
        
    def pa(self):
        print('猫咪趴')
        
class Bird():
    
    def fei(self):
        print('我飞飞飞')
        
class Dog(Cat,Bird):
    def chi(self):
        print('用啃的')
        
tom=Cat()
tom.pao()
tom.chi()
    
        
    
    
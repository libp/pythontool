# -*- coding: utf-8 -*-

print("A")
class Person(object):
    print("B")
    def __init__(self,name):
        print("C")
        self.name = name
    print("D")
print("E")
p1 = Person('name1')
p2 = Person('name2')
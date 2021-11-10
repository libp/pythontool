# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
class Circle(object):
   pi = 3.14  # 类属性

   def __init__(self, r):
       self.r = r  # 实例属性

   def get_area(self):
       """ 圆的面积 """
       # return self.r**2 * Circle.pi # 通过实例修改pi的值对面积无影响，这个pi为类属性的值
       return self.r**2 * self.pi  # 通过实例修改pi的值对面积我们圆的面积就会改变

circle1 = Circle(1)
print(circle1.get_area())
        
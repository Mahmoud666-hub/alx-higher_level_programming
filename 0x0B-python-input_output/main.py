#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

m = MyClass("John")
m.win()
print(m)
print(m.__dict__)
# print(type(m))
# print(dir(m))
# d = ()
# u = ()
# for x in dir(m):
#     if x[0:2] != "__":
#         d += (x,)
# print(d)

# print(m._MyClass__name)
# print(m.is_team_red)
# print(m.number)
# print(m.score)




# class MyClass:
#     """ My class
#     """

#     def __init__(self, name):
#         self.name = name
#         self.number = 0

#     def __str__(self):
#         return "[MyClass] {} - {:d}".format(self.name, self.number)
    
# m = MyClass("John")
# m.number = 89
# print(type(m))
# print(m)

# d = []
# for x in dir(m):
#     if x[0:2] != "__":
#         d.append(x)
# print(d)
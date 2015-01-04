__author__="mike"
__date__ ="$3-Jan-2015 11:08:49 PM$"

"""
Return various representations of the Building object
"""
class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        d = {}
        d['north-east'] = [self.south + self.width_NS, self.west + self.width_WE]
        d['south-east'] = [self.south, self.west + self.width_WE]
        d['south-west'] = [self.south, self.west]
        d['north-west'] = [self.south + self.width_NS, self.west]
        return d

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.width_WE * self.width_NS * self.height

    def __repr__(self):
        param_list = (self.south, self.west, self.width_WE, self.width_NS, self.height)
        return "Building" + str(param_list)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    print(json_dict(b.corners())) #== {'north-east': [4, 4], 'south-east': [1, 4],
                                      #'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    print(b.area()) #== 6, "Area"
    print(b.volume()) #== 60, "Volume"
    print(b2.volume()) #== 30, "Volume2"
    print(str(b)) #== "Building(1, 2, 2, 3, 10)", "String"

class Delta:
    def __init__(self):
        self.UniqueId = id(self)
    
    def getUniqueId(self):
        return self.UniqueId


class Delta1:
    idCounter = 0
    def __init__(self):
        self.UniqueId = Delta1.idCounter
        Delta1.idCounter = Delta1.idCounter + 1

    def getUniqueId(self):
        return self.UniqueId


arr = []

for i in range(14):
    x = Delta()
    print(x.getUniqueId())
    arr.append(x)

for i in range(14):
    x = Delta1()
    print(x.getUniqueId())
    arr.append(x)



class User:
    def __init__(self, name):
        self.name = name
        self.prefSet = False

    def getName(self):
        return self.name

    def setPref(self, option1, option2, option3, minPrice, maxPrice, isNorth, isCentral, priceWeight):
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.priceWeight = priceWeight
        self.prefSet = True
        self.isNorth = isNorth
        self.isCentral = isCentral

    def isPrefSet(self):
        return self.prefSet

    def getCuisines(self):
        return [self.option1, self.option2, self.option3]

    def getMinPrice(self):
        return self.minPrice

    def getMaxPrice(self):
        return self.maxPrice

    def getPriceCuisineWeight(self):
        return [self.priceWeight, 1.0 - self.priceWeight]

    def getIsNorth(self):
        return self.isNorth
    
    def getIsCentral(self):
        return self.isCentral
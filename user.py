class User:
    def __init__(self, name):
        self.name = name
        self.prefSet = False

    def getName(self):
        return self.name

    def setPref(self, option1, option2, option3):
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.prefSet = True

    def isPrefSet(self):
        return self.prefSet

    def getCuisines(self):
        return (self.option1, self.option2, self.option3)
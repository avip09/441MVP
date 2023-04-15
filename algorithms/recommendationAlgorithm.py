DATASET = [
    ('Tomokun Noodle Bar', 'Japanese', 2, 'Central'),
    ('Totoro', 'Japanese', 2, 'Central'),
    ('Slurping Turtle', 'Japanese', 2, 'Central'),
    ('Tomokun Korean BBQ', 'Korean', 2, 'Central'),
    ('The Seoul', 'Korean', 2, 'Central'),
    ('Hola Seoul', 'Korean', 1, 'Central'),
    ('Chipotle', 'Mexican', 1, 'Central'),
    ('Isalita', 'Mexican', 2, 'Central'),
    ('Condado Tacos', 'Mexican', 2, 'Central'),
    ('The Origin Cottage Inn Pizza', 'Italian', 2, 'Central'),
    ('Mani Osteria and Bar', 'Italian', 2, 'Central'),
    ('The Earle', 'Italian', 3, 'Central'),
    ('Asian Legend', 'Chinese', 2, 'Central'),
    ('Panda Express', 'Chinese', 1, 'North'),
    ('One Bowl Asian Cuisine', 'Chinese', 2, 'Central'),
    ('Namaste Flavors Arbor', 'Indian', 2, 'Central'),
    ('Taste of India', 'Indian', 2, 'Central'),
    ('Shalimar', 'Indian', 2, 'Central'),
    ('New York Pizza Depot', 'Pizza', 2, 'Central'),
    ('Pizza House', 'Pizza', 2, 'Central'),
    ("Joe's Pizza", 'Pizza', 1, 'Central'),
    ("Knight's Steakhouse", 'Steak', 3, 'Central'),
    ("Ruth's Chris Steak House", 'Steak', 4, 'Central'),
    ("Hibachi-san", 'Japanese', 2, 'North'),
    ("Marco's Pizza", 'Pizza', 1, 'North'),
    ("Nagomi", 'Korean', 2, 'North'),
    ("Seoul Street", 'Korean', 2, 'North'),
    ("Evergreen", 'Chinese', 2, 'North'),
    ("El Limon", 'Mexican', 1, 'North'),
    ("Carson's American Bistro", 'Steak', 2, 'North'),
    ("Jet's Pizza", 'Pizza', 1, 'North')
]

NUM_OF_OUTPUTS = len(DATASET)

class Recommender:

    def __init__(self, users):
        self.users = users
        self.submitted_preferences_ = 0
        self.weighed_preferences_ = []

    def getPreferences(self):

        if self.submitted_preferences_ != self.users:
            return -1

        # Argsort the list of scores
        sorted_list = [i for i in sorted(self.weighed_preferences_, key=lambda x:x[1])]
        sorted_list.reverse()

        # Return the top restaurant names and scores
        output = sorted_list[:5]

        return output

    def addUserPreferences(self, cuisine, lowPrice, highPrice, inCentral, inNorth, weights=[0.5, 0.5]):
        
        prefs = recommendationAlgorithm(cuisine, lowPrice, highPrice, inCentral, inNorth, weights)

        if self.weighed_preferences_ == []:
            self.weighed_preferences_ = prefs
        else:
            for j in prefs:
                check = False
                for i in range(len(self.weighed_preferences_)):
                    if self.weighed_preferences_[i][0] == j[0]:
                        self.weighed_preferences_[i][1] += j[1]
                        check = True
                        break
                if check == False:
                    self.weighed_preferences_.append(i)
        
        self.submitted_preferences_ += 1
        #return self.getPreferences()

    def getSubmittedPreferences(self):
        return self.submitted_preferences_


def recommendationAlgorithm(cuisine, lowPrice, highPrice, inCentral, inNorth, weights=[0.5, 0.5]):
    scores = []

    for restaurant in DATASET:
        if (restaurant[3] == 'North' and inNorth == False) or (restaurant[3] == 'Central' and inCentral == False):
            locationScore = -3
        else:
            locationScore = 3
        
        priceScore = 0
        
        if not (restaurant[2] >= lowPrice and restaurant[2] <= highPrice):
            priceScore = (- abs(restaurant[2] - lowPrice) - abs(restaurant[2] - highPrice)) / 2
        
        cuisineScore = 0
        if restaurant[1] in cuisine:
            cuisineScore = 3 - cuisine.index(restaurant[1])

        scores.append(weights[0] * priceScore + weights[1] * cuisineScore + locationScore)

    # Argsort the list of scores
    sorted_list = [i[0] for i in sorted(enumerate(scores), key=lambda x:x[1])]
    sorted_list.reverse()

    # Return the top restaurant names and scores - [Name, Score, Cuisine, Price]
    output = [[DATASET[sorted_list[i]][0], scores[sorted_list[i]], DATASET[sorted_list[i]][1], DATASET[sorted_list[i]][2], DATASET[sorted_list[i]][3]] for i in range(NUM_OF_OUTPUTS)]
    
    return output

# TESTING

# if __name__ == '__main__':
#     print(recommendationAlgorithm(['Japanese', 'Korean', 'Chinese'], 2, 3))
#     print(recommendationAlgorithm(['Steak', 'Korean', 'Italian'], 1, 2, [0.1, 0.9]))
#     print(recommendationAlgorithm(['Steak', 'Korean', 'Italian'], 1, 2, [0.9, 0.1]))
#     print(recommendationAlgorithm(['Steak', 'Chinese', 'French'], 3, 3, [0, 1]))


# Hard coded dataset, to be replaced by Google Maps API
DATASET = [
    ('Tomokun Noodle Bar', 'Japanese', 2),
    ('Totoro', 'Japanese', 2),
    ('Slurping Turtle', 'Japanese', 2),
    ('Tomokun Korean BBQ', 'Korean', 2),
    ('The Seoul', 'Korean', 2),
    ('Hola Seoul', 'Korean', 1),
    ('Chipotle', 'Mexican', 1),
    ('Isalita', 'Mexican', 2),
    ('Condado Tacos', 'Mexican', 2),
    ('The Origin Cottage Inn Pizza', 'Italian', 2),
    ('Mani Osteria and Bar', 'Italian', 2),
    ('The Earle', 'Italian', 3),
    ('Asian Legend', 'Chinese', 2),
    ('Panda Express', 'Chinese', 1),
    ('One Bowl Asian Cuisine', 'Chinese', 2),
    ('Namaste Flavors Arbor', 'Indian', 2),
    ('Taste of India', 'Indian', 2),
    ('Shalimar', 'Indian', 2),
    ('New York Pizza Depot', 'Pizza', 2),
    ('Pizza House', 'Pizza', 2),
    ("Joe's Pizza", 'Pizza', 1),
    ("Knight's Steakhouse", 'Steak', 3),
    ("Ruth's Chris Steak House", 'Steak', 4),
    ("The Chop House", 'Steak', 4)
]

NUM_OF_OUTPUTS = len(DATASET)

class Recommender():

    def __init__(self, users):
        self.users = users
        self.submitted_preferences_ = 0
        self.weighed_preferences_ = []

    def addUserPreferences(self, cuisine, lowPrice, highPrice, weights=[0.5, 0.5]):
        
        prefs = recommendationAlgorithm(cuisine, lowPrice, highPrice, weights)

        if self.weighed_preferences_ == []:
            self.weighed_preferences_ = prefs
        else:
            for i in range(len(self.weighed_preferences_)):
                for j in prefs:
                    if self.weighed_preferences_[i][0] == j[0]:
                        self.weighed_preferences_[i][1] += j[1]
                        break
        
        submitted_preferences_ += 1
        if submitted_preferences_ == users:
            return getPreferences()
        else:
            return -1

    def getPreferences(self):

        # Argsort the list of scores
        sorted_list = [i for i in sorted(self.weighed_preferences_, key=lambda x:x[1])]
        sorted_list.reverse()

        # Return the top restaurant names and scores
        output = sorted_list[:5]

        return output

    def getSubmittedPreferences(self):
        return self.submitted_preferences_


def recommendationAlgorithm(cuisine, lowPrice, highPrice, weights=[0.5, 0.5]):
    scores = []

    for restaurant in DATASET:
        priceScore = 0
        
        if not (restaurant[2] >= lowPrice and restaurant[2] <= highPrice):
            priceScore = (- abs(restaurant[2] - lowPrice) - abs(restaurant[2] - highPrice)) / 2
        
        cuisineScore = 0
        if restaurant[1] in cuisine:
            loc = 3 - cuisine.index(restaurant[1])
        
        scores.append(weights[0] * priceScore + weights[1] * cuisineScore)

    # Argsort the list of scores
    sorted_list = [i[0] for i in sorted(enumerate(scores), key=lambda x:x[1])]
    sorted_list.reverse()

    # Return the top restaurant names and scores
    output = [(DATASET[sorted_list[i]][0], scores[sorted_list[i]]) for i in range(NUM_OF_OUTPUTS)]
    
    return output

# TESTING

# if __name__ == '__main__':
#     print(recommendationAlgorithm(['Japanese', 'Korean', 'Chinese'], 2, 3))
#     print(recommendationAlgorithm(['Steak', 'Korean', 'Italian'], 1, 2, [0.1, 0.9]))
#     print(recommendationAlgorithm(['Steak', 'Korean', 'Italian'], 1, 2, [0.9, 0.1]))
#     print(recommendationAlgorithm(['Steak', 'Chinese', 'French'], 3, 3, [0, 1]))


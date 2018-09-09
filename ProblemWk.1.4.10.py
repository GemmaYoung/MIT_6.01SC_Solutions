class FruitSalad:
    fruits = ['melons', 'pineapples']
    servings = 4
    def __init__(self, ingredients, numservings):
        self.fruits = ingredients
        self.servings = numservings
    def __str__(self):
        return str(self.servings) + ' servings of fruit salad with ' + \
               str(self.ingredients)
    def add(self, fruit):
        self.fruits += [fruit,]
    def serve(self):
        if self.servings == 0:
            return 'sorry'
        self.servings -= 1
        return 'enjoy'

salad = FruitSalad(['bananas', 'apples'], 2)
salad.add('cherries')
print salad.fruits 

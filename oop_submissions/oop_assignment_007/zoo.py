class Animal:
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        self._reserved_food_in_kgs = 0
        
        if self._age_in_months != 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(self._age_in_months))
        if self._required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))
    
    # def feed(self, animal):
    #     self._reserved_food_in_kgs -= animal.required_food_in_kgs
    #     self._age_in_months += 1
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    

class LandAnimal:
    def breathe(self):
        print("Breathe in air")

class WaterAnimal:
    def breathe(self):
        print("Breathe oxygen from water")

class Deer(Animal, LandAnimal):
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs +=2
        
    def make_sound(self):
        print("Buck Buck")

class Lion(Animal, LandAnimal):
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 4
        
    def make_sound(self):
        print("Roar Roar")
        
class Shark(Animal, WaterAnimal):
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 8
        
    def make_sound(self):
        print("Shark Sound")
        
class GoldFish(Animal, WaterAnimal):
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.2
        
    def make_sound(self):
        print("Hum Hum")
    
class Snake(Animal, LandAnimal):
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.5
        
    def make_sound(self):
        print("Hiss Hiss")
        
class Zoo(Animal):
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self._animals_list = []
        
    def count_animals(self):
        return len(self._animals_list)
        
    def add_food_to_reserve(self, food):
        self._reserved_food_in_kgs += food
        
    def add_animal(self, new_animal):
        self._animals_list.append(new_animal)
        
    def feed(self, animal):
        self._reserved_food_in_kgs -= animal.required_food_in_kgs
        animal.grow()
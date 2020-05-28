class Animal:
    sound = ""
    feed = 0
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        self._reserved_food_in_kgs = 0
        
        if self._age_in_months != 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(self._age_in_months))
        if self._required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))
            
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.feed
            
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)

class LandAnimal:
    def breathe(self):
        print("Breathe in air")

class WaterAnimal:
    def breathe(self):
        print("Breathe oxygen from water")

class Deer(Animal, LandAnimal):
    sound = "Buck Buck"
    feed = 2
        
class Lion(Animal, LandAnimal):
    sound = "Roar Roar"
    feed = 4
  
class Shark(Animal, WaterAnimal):
    sound = "Shark Sound"
    feed = 8
        
class GoldFish(Animal, WaterAnimal):
    sound = "Hum Hum"
    feed = 0.2
    
class Snake(Animal, LandAnimal):
    sound = "Hiss Hiss"
    feed = 0.5
        
class Zoo:
    animal_count = []
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self._animals_list = []
        
    def count_animals(self):
        return len(self._animals_list)
        
    def addfood_to_reserve(self, food):
        self._reserved_food_in_kgs += food
        
    def add_animal(self, new_animal):
        self._animals_list.append(new_animal)
        self.animal_count.append(new_animal)
        
    def feed(self, animal):
        self._reserved_food_in_kgs -= animal.required_food_in_kgs
        animal.grow()
        
    
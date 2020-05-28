class Pokemon:
    sound = ""
    
    def __init__(self, name, level = 1):
        self._name = name
        self._level = level
        
        if len(self._name) <= 0:            raise ValueError("name cannot be empty")
        if self._level <= 0:
            raise ValueError("level should be > 0")
            
    def __str__(self):
        return ("{} - Level {}".format(self._name, self._level))

    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
        
class Run:
    pokemon_run = ""
    
    @classmethod
    def run(cls):
        print(cls.pokemon_run)
        
class Fly:
    pokemon_fly = ""
    
    @classmethod
    def fly(cls):
        print(cls.pokemon_fly)
        
class Swim:
    pokemon_swim = ""
    
    @classmethod
    def swim(cls):
        print(cls.pokemon_swim)
    
class Pikachu(Pokemon, Run):
    sound = "Pika Pika"
    pokemon_run = "Pikachu running..."
    
    def attack(self):
        if self._level >= 1:
            another_pikachu = self._level * 10
            self._level += self._level
            print("Electric attack with {} damage".format(another_pikachu))

class Squirtle(Pokemon, Run, Swim):
    sound = "Squirtle...Squirtle"
    pokemon_run = "Squirtle running..."
    pokemon_swim = "Squirtle swimming..."
    
    def attack(self):
        if self._level >= 1:
            another_squirtle = self._level * 9
            self._level += self._level
            print("Water attack with {} damage".format(another_squirtle))
    
class Pidgey(Pokemon, Fly):
    sound = "Pidgey...Pidgey"
    pokemon_fly ="Pidgey flying..."
    
    def attack(self):
        if self._level >= 1:
            another_pidgey = self._level * 5
            self._level += self._level
            print("Air attack with {} damage".format(another_pidgey))
    
class Swanna(Pokemon, Fly, Swim):
    sound = "Swanna...Swanna"
    pokemon_fly ="Swanna flying..."
    pokemon_swim = "Swanna swimming..."
    
    def attack(self):
        if self._level >= 1:
            another_swanna = self._level * 9
            another_swanna1 = self._level * 5
            self._level += self._level
            print("Water attack with {} damage\nAir attack with {} damage".format(another_swanna, another_swanna1))
    
class Zapdos(Pokemon, Fly):
    sound = "Zap...Zap"
    pokemon_fly ="Zapdos flying..."
    
    def attack(self):
        if self._level >= 1:
            another_zapdos = self._level * 10
            another_zapdos1 = self._level * 5
            self._level += self._level
            print("Electric attack with {} damage\nAir attack with {} damage".format(another_zapdos, another_zapdos1))

class Island(Pokemon):
    total_pokemon_list = []
    def __init__(self, name, max_no_of_pokemon, total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.pokemon_list = []
    def __str__(self):
        return ("{} - {} pokemon - {} food".format(self._name, self._pokemon_left_to_catch, self._total_food_available_in_kgs))
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def add_pokemon(self, pokemon):
        # self.pokemon_list.append(pokemon)
        # self.total_pokemon_list.append(pokemon)
        if self._max_no_of_pokemon > self._pokemon_left_to_catch:
            self.pokemon_list.append(pokemon)
            self.total_pokemon_list.append(pokemon)
            self._pokemon_left_to_catch += 1
        else:
            print("Island at its max pokemon capacity")
    
    def get_all_islands(self):
        #for items in range(total_pokemon_list:
        return("{} - {} pokemon - {} food".format(self._name, self.total_pokemon_list, self._total_food_available_in_kgs))
            
class Trainer(Pokemon):
    def __init__(self, name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = 10 * (self._experience)
        self._food_in_bag = 0
    
    def __str__(self):
        return self._name
    
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag
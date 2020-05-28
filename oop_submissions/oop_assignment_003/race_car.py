from car import Car 
import math
class RaceCar(Car):
    
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._nitro = 0 
        
    def accelerate(self):
        if self._nitro > 0:
            if self._nitro < self._max_speed:
                self._current_speed += math.ceil((self._acceleration * 30) / 100)
                self._nitro -= 10
        super().accelerate()
        
    def apply_brakes(self):
        if self._current_speed > self._max_speed // 2:
            self._nitro += 10
        super().apply_brakes()
        
    def sound_horn(self):
        if self._is_engine_started == True:
            print("Peep Peep\nBeep Beep")
        else:
            print("Start the engine to sound_horn")
            
    @property
    def nitro(self):
        return self._nitro

racecar = RaceCar(color="Red", max_speed=250, acceleration=50, tyre_friction=30)
racecar.start_engine()  
racecar.accelerate()  
racecar.accelerate()
racecar.accelerate()  
print(racecar.current_speed)
racecar.apply_brakes()
print(racecar.current_speed)
print(racecar.nitro)
racecar.accelerate()
print(racecar.current_speed)
print(racecar.nitro)
racecar.sound_horn()

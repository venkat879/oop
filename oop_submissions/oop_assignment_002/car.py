class Car:
    
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._current_speed = 0
        self._is_engine_started = False
        
        if self._max_speed < 0:
            raise ValueError("Invalid value for max_speed")
        
        if self._tyre_friction < 0:
            raise ValueError("Invalid value for tyre_friction")
            
        if self._acceleration < 0:
            raise ValueError("Invalid value for acceleration")
        
    def start_engine(self):
        self._is_engine_started = True
        
    def stop_engine(self):
        self._is_engine_started = False
    
    def accelerate(self):
        if self._is_engine_started == True:
            self._current_speed += self._acceleration
            
            if self._current_speed >= self._max_speed:
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
    
    def apply_brakes(self):
        if self._current_speed > 0:
            self._current_speed -= self._tyre_friction
            if self._current_speed < 0:
                self._current_speed = 0
        
    def sound_horn(self):
        if self._is_engine_started == True:
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")
            
    @property 
    def max_speed(self):
        return self._max_speed

    @property
    def color(self):
        return self._color

    @property
    def tyre_friction(self):
        return self._tyre_friction
    
    @property
    def acceleration(self):
        return self._acceleration

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def is_engine_started(self):
        return self._is_engine_started
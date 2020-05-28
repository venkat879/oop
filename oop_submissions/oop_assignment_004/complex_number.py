import math
class ComplexNumber:
    
    def __init__(self, real_part=0, imaginary_part=0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        
        if type(self.real_part) == str and type(self.imaginary_part) == str:
            raise ValueError("Invalid value for real and imaginary part")
        
        elif type(self.real_part) == str:
            raise ValueError("Invalid value for real part")
            
        elif type(self.imaginary_part) == str:
            raise ValueError("Invalid value for imaginary part")
            
    def __str__(self):
        complexnumber = ("{}+{}i".format(self.real_part, abs(self.imaginary_part)))
        return complexnumber
        
    def conjugate(self):
        return ComplexNumber(self.real_part, -self.imaginary_part)
    
    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)
        
    def __sub__(self, other):
        return ComplexNumber (self.real_part - other.real_part, self.imaginary_part - other.imaginary_part)
        
    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.imaginary_part * other.imaginary_part, self.imaginary_part * other.real_part + self.real_part * other.imaginary_part)
        
    def __truediv__(self,other):
        if other.real_part and other.imaginary_part == 0:
            raise ZeroDivisionError("division by zero")
        else:
            r = float(other.real_part ** 2 + other.imaginary_part ** 2)
            return ComplexNumber((self.real_part * other.real_part + self.imaginary_part * other.imaginary_part)/r, (self.imaginary_part * other.real_part - self.real_part * other.imaginary_part)/r)
        
    def __abs__(self):
        r = math.sqrt(self.real_part**2 + self.imaginary_part**2)
        return (round(r, 3))
    
    def __eq__(self, other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part
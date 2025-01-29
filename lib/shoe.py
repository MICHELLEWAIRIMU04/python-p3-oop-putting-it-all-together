#!/usr/bin/env python3

class Shoe:
    def  __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "used"

    def get_brand(self):
        self._brand 
    
    def set_brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError("Brand must be a string")

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size 

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            raise ValueError("size must be an integer")
        
    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    
    def __str__(self):
        return f"Shoe(Brand: {self.brand}, Size: {self.size}, Condition: {self.condition})"  
        

shoe = Shoe("Adidas", 9)
print(shoe)
shoe.cobble()
print(shoe)
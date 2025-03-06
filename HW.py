class Ferrari:
    def fuel(self):
        print('petrole')

    def price(self):
        print('$500,000')

    def type(self):
        print('Sports Car')

class BMW:
    def fuel(self):
        print('deisel')
    
    def price(self):
        print('$450,000')
    
    def type(self):
        print('SUV')

#making object for each class

F = Ferrari()
B = BMW()

for details in (F,B):
    details.fuel()
    details.price()
    details.type()
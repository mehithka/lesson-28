class India():
    def capital(self):
       print("New Delhi is the capital oif india")
    
    def language(self):
        print('hindi is the most widely spoken language in india')
    
    def type(self):
         print('india is a developing country')

class USA():
    def capital(self):
        print('Washington D.C is the capital of USA')

    def language(self):
        print('english is the primary language of USA')
    
    def type(self):
        print('USA IS A DEVELOPED COUNTRY')

obj_ind = India()
obj_usa = USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()
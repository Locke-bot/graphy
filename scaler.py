# person
class Tan:
    '''body tan'''
    def __init__(self, race, temp, ):
        self.race = race
        self.temp = temp
    
    def _tan(self):
        if self.race == 'white': # white has a product value of 2.5, they tan more than we blacks
            return 2.5*self.temp/30
        elif self.race == 'black':
            return 1.5*self.temp/30
        
    @property
    def tan(self):
        return self._tan()
    
tan = Tan('black', 30)
print(tan._tan())
            
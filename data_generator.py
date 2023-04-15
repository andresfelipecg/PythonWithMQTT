import random

def message_random():
    print("Random")

# Defining our variables
base_temperature = 100

dict = {1: ["Toronto"], 2: ["Vancouver"], 3: ["Winnipeg"], 4: [0]}

dict2 = {
  "cities": "Toronto, Vancouver, Winnipeg, Calgary",
  "temperature": 0
}

# Defining a class
class Sample_set:
    def __init__(self, base_temperature: int = None):
        self.base_temperature = random.randint(5, 10)
        self.dict = {1: ["Toronto"], 2: ["Vancouver"], 3: ["Winnipeg"], 4: [self.base_temperature]}
     
    
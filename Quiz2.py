class Hammock():
    def __init__(self):
        self.numPersons = 0
        self.request = None
    def sitDown(self, person):
        if self.numPersons == 0:
            self.numPersons += 1
            self.request = None
            return 'welcome'
        else:
            if self.request == person:
                self.numPersons += 1
                self.request = None
                return 'welcome'
            else:
                self.request = person
                return 'sorry, no room'
    def leave(self):
        if self.numPersons != 0:
            self.numPersons -= 1
        return self.numPersons
                

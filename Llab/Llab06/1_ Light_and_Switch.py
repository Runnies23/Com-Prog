
#swtich - light True = on, False = off

class Switch():
    def __init__(self, name, status=False):
        self.status = status
        self.name = name

        self.on_off = {
            True : "on",
            False : "off"
        }

    def turn(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def clone(self):
        return Switch(self.name + ".copy", self.status)

    def __str__(self):
        return f"switch({self.name}) is {self.on_off[self.status]}"


class Light():
    def __init__(self, name, switch):
        self.switch = switch
        self.name = name

    def turn(self):
        self.switch.turn()

    def get_status(self):
        return self.switch.status


    def set_switch(self,new_switch:Switch):
        self.switch = new_switch
        
    def clone(self):
        return Light(self.name + ".copy", self.switch.clone())

    def __str__(self):
        return f"light({self.name}) with switch({self.switch.name}) is {self.switch.on_off[self.switch.status]}"
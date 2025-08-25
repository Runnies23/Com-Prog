class Radio:
    def __init__(self,mode:str="FM",frequency:float=87.5):
        self.mode = mode
        self.frequency = frequency
        self.pre = {
            "FM" : "MHz",
            "AM" : "kHz"
        }

    def __str__(self):
        return f"{self.mode} Radio: {self.frequency:.1f} {self.pre[self.mode]}"

    def set_mode(self,mode):
        self.mode = mode
        if self.mode == "AM":
            self.frequency = 150
        elif self.mode == "FM":
            self.frequency = 87.5

    def set_frequency(self,frequency):
        if (frequency >= 87.5 and frequency <= 108) or (frequency >= 150  and frequency <= 280):
            self.frequency = frequency
        self.correct_frequency()

    def correct_frequency(self):
        if self.frequency < 87.5:
            self.frequency = 87.5
        elif self.frequency > 108 and self.frequency < 120:
            self.frequency = 108
        elif self.frequency > 120 and self.frequency < 150:
            self.frequency = 150
        elif self.frequency > 280 and self.frequency < 300:
            self.frequency = 280
        
    def get_mode(self):
        return self.mode
    
    def get_frequency(self):
        return self.frequency

    def adjust_frequency(self,frequency):
        rst = self.frequency + frequency
        if (rst >= 87.5 and rst <= 108) or (rst >= 150  and rst <= 280):
            self.frequency = rst
            return True
        return  False


############## test case for Radio class
def print_des(a):
    print("mode:", a.get_mode())
    print("freq:", a.get_frequency())
    print("str:", a)
    print("")


def do_set_freq(a, fre):
    a.set_frequency(fre)
    print(f"set_frequency({fre})")
    print_des(a)


def do_set_mode(a, mode):
    a.set_mode(mode)
    print(f"set_mode({mode})")
    print_des(a)


def do_adjust(a, adjust):
    b = a.adjust_frequency(adjust)
    print(f"adjust({adjust})")
    print(f"return: {b}")
    print_des(a)
    return b


a = Radio()
b = False
print("Init")
print_des(a)
a.set_mode("AM")
print("a.set_mode(AM)")
print_des(a)
do_set_freq(a, 149.9)
do_set_freq(a, 270)
do_set_freq(a, 280.0001)
do_set_freq(a, 280)
do_set_mode(a, "FM")
do_set_freq(a, 10)
do_set_freq(a, 107.9)
do_set_freq(a, 108.1)
do_set_freq(a, 108)
do_set_freq(a, 87.5)
do_adjust(a, 0.5)
do_adjust(a, -5)
do_adjust(a, 19.9)
do_adjust(a, 0.1)
do_adjust(a, 1)
do_adjust(a, -20.5)
do_adjust(a, 0.0001)
do_set_mode(a, "AM")
do_adjust(a, -0.001)
do_adjust(a, 100.51)
do_adjust(a, -0.51)
do_adjust(a, 30)
do_adjust(a, 20.5)
do_adjust(a, -2000)
do_adjust(a, -130)
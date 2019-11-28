class sausage:
    def __init__(self, stuffing='pork!', length = 1):
        self.stuffing = stuffing
        self.length = length
        self.length = eval(str(length)) * 12

        if len(stuffing) > 12:
            self.stuff = stuffing[:12]
        else:
            self.stuff = stuffing * (12 // len(stuffing)) + stuffing[:12 % len(stuffing)]
        
    def __str__(self):
        if int(self.length) == 0:
            b = "||"
            u = "/|"
            d = "\\|"
        else:
            b = ("|" + self.stuff + "|") * (int(self.length) // 12)
            u = "/------------\\"        * (int(self.length) // 12)
            d = "\\------------/"        * (int(self.length) // 12)
        
        if int(self.length) % 12:
            b += ("|" + self.stuff + "|")[:int(self.length) % 12 + 1] + "|"
            u += "/------------\\"[:int(self.length) % 12 + 1]        + "|"
            d += "\\------------/"[:int(self.length) % 12 + 1]        + "|"

        return "\n".join((u, b, b, b, d))

    def __mul__(self, value):
        return sausage(self.stuffing, (self.length * value) / 12)
    
    def __truediv__(self, value):
        return sausage(self.stuffing, (self.length / value) / 12)

    def __sub__(self, other):
        return sausage(self.stuffing, self.length - other.length) if (self.length - other.length) > 0 else sausage(self.stuffing, 0)

    def __add__(self, other):
        return sausage(self.stuffing, (self.length + other.length) / 12)

    def __bool__(self):
        return True if self.length else False

    __rmul__ = __mul__
#Recursive Formulas
#Defintion of the clases:
class Formula():
    def __init__(self):
        pass

class Letter(Formula):
    def __init__(self, letter):
        self.letter = letter


class Negation(Formula):
    def __init__(self, subf:Formula):
        self.subf = subf

class Binary(Formula):
    def __init__(self, connector:str, left:Formula, right:Formula):
        assert(connector in ["Y", "O", ">", "="])# ">" = entonces "=" = si y sólo si
        self.connector = connector
        self.left = left
        self.right = right

#Methods
    def __str__(self):
        if type(self) == Letter:
            return self.letter
        
        elif type(self) == Negation:
            return "-" + str(self.subf)
        
        elif type(self) == Binary:
            return "(" + str(self.left) + self.connector + str(self.right) + ")"
        
    setattr(Formula, "__str__", __str__)

    def num_connec(self):
        if type(self) == Letter:
            return 0
        elif type(self) == Negation:
            return 1 + self.subf.num_connec()
        elif type(self) == Binary:
            return 1 + self.left.num_connec() + self.right.num_connec()


if __name__ == "__main__":
    p = Letter("p")
    q = Letter("q")
    a1 = Negation(p)
    print(a1)

    a2 = N



#Recursive Formulas
#Defintion of the clases:
class Formula():
    def __init__(self):
        pass

#Methods
    def __str__(self):
        if type(self) == Letter:
            return self.letter
        
        elif type(self) == Negation:
            return "-" + str(self.subf)
        
        elif type(self) == Binary:
            return "(" + str(self.left) + self.connector + str(self.right) + ")"
        

    def num_connec(self):
        if type(self) == Letter:
            return 0
        elif type(self) == Negation:
            return 1 + self.subf.num_connec()
        elif type(self) == Binary:
            return 1 + self.left.num_connec() + self.right.num_connec()
        
    def num_paren(self):
        if type(self) == Letter:
            return 0
        elif type(self) == Negation:
            return 0 + self.subf.num_paren()
        elif type(self) == Binary:
            return 2 + self.left.num_paren() + self.right.num_paren()
    
    def num_letras(self):
        if type(self) == Letter:
            return 1
        elif type(self) == Negation:
            return 0+ self.subf.num_letras()
        elif type(self) == Binary:
            return self.left.num_letras() + self.right.num_letras()
    
    def num_bin(self):
        if type(self) == Letter:
            return 0
        elif type(self) == Negation:
            return 0 + self.subf.num_bin()
        elif type(self) == Binary:
            return 1 + self.left.num_bin() + self.right.num_bin()

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



if __name__ == "__main__":
    # Ejercicio 1
    print("Ejercicio 1")
    p = Letter("p")
    print("Varaible" , p)

    s = Letter("s")
    print("Variable", s)

    r = Letter("r")
    print("Variable", r)
    
    q = Letter("q")
    print("Varaible" , q)

    a1 = Negation(p)
    print("Formula #1 ", a1)

    a2 = Binary(">", a1,q)
    print("Formula #2", a2)

    a3 = Negation(Binary("Y",p,Negation(q)))
    print( "Formula #3 " , a3)

    a4 = Binary("Y",p,q)
    print("Formula #4 ", a4 )

    a5 = Negation(Binary("Y",p,q))
    print("Formula #5 ", a5)



    #print("There are " ,a1.num_connec(), " connectors in the second formula ")
    #print("There are " ,a2.num_connec(), " connectors in the second formula ")
    #print("There are " ,a3.num_connec(), " connectors in the third formula ")
    #print(a4.num_connec())
    #print(a5.num_connec())
    print(a4.num_bin())

  
    

    #print("There are " ,a1.num_paren(), " parenthesis in the second formula ")
    #print("There are " ,a2.num_paren(), " parenthesis in the second formula ")
    #print("There are " ,a3.num_paren(), " parenthesis in the third formula ")
    


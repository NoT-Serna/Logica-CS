from itertools import product
from copy import deepcopy
from tkinter import NE
#Recursive Formulas
#Defintion of the clases:
class Formula():
    def __init__(self):
        pass

    def delete_double_imp(self):
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
    
    def letters(self):
        if type(self) == Letter:
            return {self.letter}
        elif type(self) == Negation:
            return {self.subf.letters()}
        elif type(self) == Binary:
            return self.left.letters() | self.right.letters() 
    
    def sub_forms(self):
        if type(self) == Letter:
            return {self}
        elif type(self) == Negation:
            return {self}| self.subf.sub_forms()
        elif type(self) == Binary:
            return {self}|self.left.sub_forms()|self.right.sub_forms()
    
    def sust(self, n, n1):
        if n not in self.sub_forms():
            return self
        elif n == self:
            return n1
        elif self == Negation:
            return Negation(self.subf.sust(n,n1))
        elif self == Binary:
            return Binary(self.connector, self.left.sust(n,n1), self.right.sust(n,n1))

    def value(self, I):
        if type(self) == Letter:
            return I[self.letter]
        elif type(self) == Negation:
            return not self.subf.value(I)
        elif type(self) == Binary:
            if self.connector == "Y":
                return self.left.value(I) and self.right.value(I)
            if self.connector == "O":
                return self.left.value(I) or self.right.value(I)
            if self.connector == ">":
                return not self.left.value(I) or self.right.value(I)
            if self.connector == "=":
                return  (self.left.value(I) and self.right.value(I)) or (not self.left.value(I) and not self.right.value(I))
    
    def delete_double_imp(self):
        if type(self) == Letter:
            return self
        elif type(self) == Negation:
            return Negation(self.subf.delete_double_imp())
        elif type(self) == Binary:
            if self.connector == "=":
                return Binary("Y",
                            Binary("O",
                                Negation(self.left.delete_double_imp()),
                                self.right.delete_double_imp(),
                                ),
                            Binary("O",
                                Negation(self.right.delete_double_imp()),
                                self.left.delete_double_imp(),
                                ))
            else:
                return Binary(self.connector,
                        self.left.delete_double_imp(),
                        self.right.delete_double_imp()
                        )

    def delete_double_negation(self):
        if type(self) == Letter:
            return self
        elif type(self) == Negation:
            if type(self.subf) == Negation:
                return deepcopy(self.subf.subf.delete_double_negation())
            else:
                return Negation(self.subf.delete_double_negation())
        elif type(self) == Binary:
            return Binary(self.connector,
                           self.left.delete_double_negation(),
                           self.right.delete_double_negation())
    
    def change_morgan_and(self):
        if type(self) == Letter:
            return self
        elif type(self) == Negation:
            if type(self.subf) == Binary:
                if self.subf.connector == "Y":
                    return Binary("O",
                                Negation(self.subf.left.change_morgan_and()),
                                Negation(self.subf.right.change_morgan_and())
                                )
                else:
                    return Negation(self.subf.change_morgan_and())
            else:
                return Negation(self.subf.change_morgan_and())
        elif type(self) == Binary:
            return Binary(self.connector,
                           self.left.change_morgan_and(),
                           self.right.change_morgan_and())
    
    

    

def inorder_to_tree(cadena):
    connector = ["Y", "O", ">", "="]
    if len(cadena) == 1:
        return Letter(cadena)
    elif cadena[0] == "-":
        return Negation(inorder_to_tree(cadena[1::]))
    elif cadena[0] == "(":
        counter = 0
        for i in range(1,len(cadena)):
            if cadena[i] == "(":
                counter +=1
            elif cadena[i] == ")":
                counter -=1
            elif cadena[i] in connector and counter == 0:
                return Binary(cadena[i], inorder_to_tree(cadena[1:i]),inorder_to_tree(cadena[i + 1:-1]))
    else:
            raise Exception('¡Cadena inválida!')
        

    


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


    I = {"p": True, "q": False}
    print(f"{a1} tiene el valor {a1.value(I)}")

    #print("There are " ,a1.num_connec(), " connectors in the second formula ")
    #print("There are " ,a2.num_connec(), " connectors in the second formula ")
    #print("There are " ,a3.num_connec(), " connectors in the third formula ")
    #print(a4.num_connec())
    #print(a5.num_connec())
    #print(a4.num_bin())
    prueba = "(-p>((pY-q)>(pYq)))"
    Tree = inorder_to_tree(prueba)
    print(Tree)
    print(Tree.num_bin())
  
    

    #print("There are " ,a1.num_paren(), " parenthesis in the second formula ")
    #print("There are " ,a2.num_paren(), " parenthesis in the second formula ")
    #print("There are " ,a3.num_paren(), " parenthesis in the third formula ")
    


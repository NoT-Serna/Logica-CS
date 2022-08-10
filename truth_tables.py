from itertools import product

interpretations = list(product([True,False], [True,False]))
print(interpretations)

#p not p
print("-" *13)
print("p     not  p")
for p in [True,False]:
    espacio1 = " " if p else " "
    print(f"{p}{espacio1}{not p}")


print("")
print("-"*20)
print("p     q     p and q")
for I in interpretations:
    p= I[0]
    q= I[1]
    espacio1 = "  " if p else " "
    espacio2 = "  " if q else " "
    print(f"{p}{espacio1}{q}{espacio2}{p and q}")

### With dictionaries ####
I = {"p": True, "q": False}
print(I["p"])
print(I["q"])

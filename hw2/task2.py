import fractions

f1 = input("a1/b1 = ")
f2 = input("a2/b2 = ")

a1, b1 = f1.split("/")
a1 = int(a1)
b1 = int(b1)

a2, b2 = f2.split("/")
a2 = int(a2)
b2 = int(b2)

sa = (a1 * b2 + a2 * b1)
sb = (b1 * b2)
ma = (a1 * a2)
mb = (b1 * b2)

print(f"my {f1} + {f2} = {sa}/{sb}")
print(f"my {f1} * {f2} = {ma}/{mb}")

ff1 = fractions.Fraction(a1, b1)
ff2 = fractions.Fraction(a2, b2)

print(f"check {f1} + {f2} = {ff1 + ff2}")
print(f"check {f1} * {f2} = {ff1 * ff2}")

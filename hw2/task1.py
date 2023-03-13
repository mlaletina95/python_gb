n = int(input("n = "))
print("check hex =", hex(n))

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
s = ""
while n > 0:
    m = n % 16
    n = n // 16
    s = s + digits[m]

# reverse
s = s[::-1]
print(f"my hex = 0x{s}")

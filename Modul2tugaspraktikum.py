print("Program mencari bilangan terbesar")
print("---------------------------------")
a = int(input("Masukan nilai a: "))
b = int(input("Masukan nilai b: "))
c = int(input("Masukan nilai c: "))

if a > b and a > c:
    maks = a
    print ("Nilai Terbesar adalah ",maks)
elif b > a and b > c:
    maks = b
    print ("Nilai Terbesar adalah ",maks)
else:
    maks = c
    print ("Nilai Terbesar adalah ",maks)

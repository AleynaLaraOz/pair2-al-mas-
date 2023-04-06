vize = int(input("notunuzu giriniz"))
final = int(input("final notunuzu giriniz"))
ortalama = int((vize * 0.4) + (final * 0.6))

if ortalama < 50:
    print("FF")
elif ortalama < 60:
    print("DD")
elif ortalama < 70:
    print("CC")
elif ortalama < 80:
    print("BB")
elif ortalama < 101:
    print("AA")
else:
    print("Yanlış bir değer girdiniz.")
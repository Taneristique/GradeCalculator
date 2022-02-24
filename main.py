def didIpass(vize,final,toplamDersSaati,devamsizlik):
    devamsizlikNotu=4 if devamsizlik<=toplamDersSaati*70/100 else 0
    karar= "Dersden geçti!" if vize+final+devamsizlikNotu>=60 and devamsizlikNotu!=0 else  "Dersten kaldı!"
    return karar
v=int(input("Vize notunuzu giriniz:"))*16/100
f=int(input("Final notunuzu giriniz:"))*80/100
t=int(input("Kaç saat ders görüyorsunuz:"))*80/100
d=int(input("Toplam devamsızlığınızı yazınız:"))
print(didIpass(v,f,t,d))
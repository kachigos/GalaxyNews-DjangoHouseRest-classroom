k = int(input("kolichestvo kotlet odnovremenno:"))
m = int(input("kolychestvo minut:"))
n = int(input("kolychestvo kotlet:"))
if n/k%1 == 0:
    print("kolychestvo minut:", n/k*m*2)
else:
    print("kolychestvo minut",(n//k+1)*m*2)

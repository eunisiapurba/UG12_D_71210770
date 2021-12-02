bilangan1 = int(input("Masukkan awal deret : "))
bilangan2 = int(input("Masukkan akhir deret : "))

x = []
if (bilangan1 + 1) % 2 == 0:
     for i in range (bilangan1+1,bilangan2,2):
         if i % 3 == 0 or i % 7 == 0: continue
         print ( i , end = " " )
else:
     for i in range (bilangan1 , bilangan2 , 2):
         if i % 3 == 0 or i % 7 == 0 : continue
         print (i , end = " ")
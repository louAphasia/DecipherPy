alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in=input("Enter message Uppcase letters ")

#SHIFT

shift=int(input("podaj shift value liczbe "))
n=len(str_in)
str_out=""

for i in range(n):
    c=str_in[i]
    loc=alpha.find(c)
    print(" indeks %d litera %s lokalizacja w alpha %d" %(i,c,loc))
    newloc=(loc+ shift)%26  # przesuniecie o ile
    # DLUGOSC ALFPABETU  26

    str_out+=alpha[newloc]
    print("nowa LOKALIZACJA W alpha po shift  %d  litera new %s" %(newloc,str_out))

print("Obsfucate version", str_out)
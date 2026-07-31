print("\n._. WELCOME TO THE FLAMES GAME ._.\n")
a=str(input("ENTER THE BOY NAME: \t"))
b=str(input("ENTER THE GIRL NAME: \t"))
a=a.lower( )
b=b.lower( )
a=a.replace(" ","")
b=b.replace(" ","")
lista=list(a)
listb=list(b)
print('BOY NAME IN LIST:',lista)
print('GIRL NAME IN LIST:',listb)
for ch in lista[:]:
    if ch in listb:
        lista.remove(ch)
        listb.remove(ch)
print('\nRemove common letter after the name list: ')        
print(lista)
print(listb)
count=len(lista)+len(listb)
print('\nno.of uncommon character in a names:',count)
flames=["F","L","A","M","E","S"]
print(flames)
index=0
while len(flames) >1:
    index=(index+count-1)%len(flames)
    flames.pop(index)    
print(flames)
if flames[0]=='F':
    result = "FRIENDS 🫂"
elif flames[0]=='L':
    result = "Love ❤️"
elif flames[0]=='A':
    result = "Affection 🧲"
elif flames[0]=='M':
    result = "Marriage 💍"
elif flames[0]=='E':
    result = "Enemies 👊"
elif flames[0]=='S':
    result = "Siblings 👥"  
print("\n ❤️ FLAMES Result ❤️")
print(a,"&",b,"=",result,"\n")    
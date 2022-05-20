item={}
price={}
stock={}
f=open('sspp.txt','r')
try:
    n=int((f.readline()).rstrip('\n'))
except:
    n=0
for i in range(0,n):
    line=((f.readline()).rstrip('\n'))
    x1,x2=line.split('#')
    x1=int(x1)
    x2=str(x2)
    item.update({x1:x2})
for i in range(0,n):
    line=((f.readline()).rstrip('\n'))
    x1,x2=line.split('#')
    x1=int(x1)
    x2=float(x2)
    price.update({x1:x2})
for i in range(0,n):
    line=((f.readline()).rstrip('\n'))
    x1,x2=line.split('#')
    x1=int(x1)
    x2=int(x2)
    stock.update({x1:x2})
f.close()
def home():
    print('\n\nSHIV SHAKTI PAPER PRODUCTS, MUZAFFARNAGAR','\n')
    print('A : Add an item')
    print('R : Remove an item')
    print('L : List all items')
    print('U : Update an item')
    print('Q : Quit','\n')
def add_item():
    inum=len(item)+1
    print('Enter item name : ')
    iname=str(input())
    print('Enter item price : ')
    iprice=float(input())
    print('Enter item stock : ')
    istock=int(input())
    item.update({inum:iname})
    price.update({inum:iprice})
    stock.update({inum:istock})
    print('Item added successfully')
def remove_item():
    print('which item you want to remove ?\n')
    for i in range(0,len(item)):
        print(f'{i+1} : {item.get(i+1)}')
    r=int(input())
    item.pop(r)
    price.pop(r)
    stock.pop(r)
    print('Item removed successfully')
def list_item():
    print('S.No   Item               Price     Stock')
    for i in range(0,len(item)):
        print(f'{i+1}      {item.get(i+1)}    {price.get(i+1)}    {stock.get(i+1)}')
def update_item():
    print('which item you want to edit ?\n')
    for i in range(0,len(item)):
        print(f'{i+1} : {item.get(i+1)}')
    r=int(input())
    print('Enter item name : ')
    iname=str(input())
    print('Enter item price : ')
    iprice=float(input())
    print('Enter item stock : ')
    istock=int(input())
    item.update({r:iname})
    price.update({r:iprice})
    stock.update({r:istock})
    print('Item edited successfully')
while True:
    home()
    print('Enter your choice :',end='')
    choice=str(input())
    if choice=='Q' or choice=='q':
        break
    elif choice=='A'or choice=='a':
        add_item()
    elif choice=='R'or choice=='r':
        remove_item()
    elif choice=='L'or choice=='l':
        list_item()
    elif choice=='U'or choice=='u':
        update_item()

n=int(len(item))
f=open('sspp.txt','w')
f.write(f"{n}\n")
for i in range(0,n):
    f.write(f'{i+1}#{item.get(i+1)}\n')
for i in range(0,n):
    f.write(f'{i+1}#{price.get(i+1)}\n')
for i in range(0,n):
    f.write(f'{i+1}#{stock.get(i+1)}\n')

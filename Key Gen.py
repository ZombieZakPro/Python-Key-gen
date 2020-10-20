import time
import random

Altha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

x = 0
print ("Amount of keys")
y = int(input())


while (True):
    x += 1
    Rand = f"{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}"
    st = Rand.replace("'","")
    nd = st.replace(",","")
    rd = nd.replace("[","")
    last = rd.replace("]","")
    lastplus = last.replace(" ","")
    
    print (lastplus)

    if x == y:
        print ("You have 1 min to copy")
        time.sleep(60)
        break

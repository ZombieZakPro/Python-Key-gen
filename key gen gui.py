import turtle
import random
import time

#Screen
scr = turtle.Screen()
scr.title("Key Gen GUI")
scr.bgcolor("black")
scr.setup(width = 550,height = 400)
scr.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

#msg
pen.goto(-270, 150)
pen.write("Press r to roll and Enjoy", align="left", font=("Consolle", 24,"normal"))
#1.
pen.goto(-270, 120)
pen.write("1. 0", align="left", font=("Courier", 24,"italic"))
#2.
pen.goto(-270, 90)
pen.write("2. 0", align="left", font=("Courier", 24,"italic"))
#3.
pen.goto(-270, 60)
pen.write("3. 0", align="left", font=("Courier", 24,"italic"))
#4.
pen.goto(-270,30)
pen.write("4. 0", align="left", font=("Courier", 24,"italic"))
#5.
pen.goto(-270, 0)
pen.write("5. 0", align="left", font=("Courier", 24,"italic"))



def reroll():
    scr.clear()
    scr.bgcolor("black")
    
    Altha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    pen1_reroll = f"{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}"
    pen2_reroll = f"{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}"
    pen3_reroll = f"{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}"
    pen4_reroll = f"{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}"
    pen5_reroll = f"{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}-{random.choices(Altha, k=5)}"

    replacest1 = pen1_reroll.replace("'","")
    replacend1 = replacest1.replace(" ", "")
    replacerd1 = replacend1.replace(",","")
    replaceth1 = replacerd1.replace("]","")
    replacelast1 = replaceth1.replace("[","")
    
    replacest2 = pen2_reroll.replace("'","")
    replacend2 = replacest2.replace(" ", "")
    replacerd2 = replacend2.replace(",","")
    replaceth2 = replacerd2.replace("]","")
    replacelast2 = replaceth2.replace("[","")
    
    replacest3 = pen3_reroll.replace("'","")
    replacend3 = replacest3.replace(" ", "")
    replacerd3 = replacend3.replace(",","")
    replaceth3 = replacerd3.replace("]","")
    replacelast3 = replaceth3.replace("[","")

    replacest4 = pen4_reroll.replace("'","")
    replacend4 = replacest4.replace(" ", "")
    replacerd4 = replacend4.replace(",","")
    replaceth4 = replacerd4.replace("]","")
    replacelast4 = replaceth4.replace("[","")

    replacest5 = pen5_reroll.replace("'","")
    replacend5 = replacest5.replace(" ", "")
    replacerd5 = replacend5.replace(",","")
    replaceth5 = replacerd5.replace("]","")
    replacelast5 = replaceth5.replace("[","")
    
    #msg
    pen.goto(-270, 150)
    pen.write("Press r to roll and Enjoy", align="left", font=("Consolle", 24,"normal"))
    #color
    pen.color("red")
    pen.goto(-270, 120)
    pen.write("1. {}".format(replacelast1), align="left", font=("Courier", 24,"italic"))
    pen.color("purple")
    pen.goto(-270, 90)
    pen.write("2. {}".format(replacelast2), align="left", font=("Courier", 24,"italic"))
    pen.color("green")
    pen.goto(-270, 60)
    pen.write("3. {}".format(replacelast3), align="left", font=("Courier", 24,"italic"))
    pen.color("orange")
    pen.goto(-270, 30)
    pen.write("4. {}".format(replacelast4), align="left", font=("Courier", 24,"italic"))
    pen.color("blue")
    pen.goto(-270,0)
    pen.write("5. {}".format(replacelast5), align="left", font=("Courier", 24,"italic"))
    pen.color("lime")

scr.listen()
while (True):
    scr.update()
    scr.onkeypress(reroll, "r")
    scr.onkeypress(reroll, "R")

    


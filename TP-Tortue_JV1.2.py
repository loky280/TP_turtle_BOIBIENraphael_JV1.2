import random
import turtle


#creation tortue

nbTortue = 5
liste=[]
for i in range(nbTortue):
    listeofcolor=["blue","orange","yellow","green","black","purple","red"]
    a=random.randint(0,6)
    mx=random.randint(-80,80)
    my=random.randint(-80,80)
    n=random.randint(0,2)*2
    
    size=2+n

    maTortueNinja1=turtle.Turtle() 
    turtle.delay(1)
    maTortueNinja1.color(listeofcolor[a])
    maTortueNinja1.shape("circle")
    maTortueNinja1.shapesize(size,size)
    maTortueNinja1.penup()
    maTortueNinja1.goto(mx*3,my*3)
    maTortueNinja1.pendown()
    
    liste.append(maTortueNinja1)

"""
maTortueNinja=turtle.Turtle() 
n=random.randint(0,2)*2
size=2+n
maTortueNinja.shapesize(size,size)
"""
turtle.delay(0)

#tortues pour les premiers exercices
"""
maTortueNinja=turtle.Turtle()
maTortueNinja1.color("blue")

maTortueNinja=turtle.Turtle()
maTortueNinja2.color("purple")

maTortueNinja=turtle.Turtle()
maTortueNinja3.color("orange")

maTortueNinja=turtle.Turtle()
maTortueNinja.color("red")

"""


# Pour faire un cercle
"""

for i in range (1,500,1):
    maTortueNinja.forward(2)
    maTortueNinja.left(1)"""

# pour faire un carré
"""

for i in range (1,5,1):
    maTortueNinja.forward(100)
    maTortueNinja.left(90)"""


# pour faire un escargot carré (littéralement)




"""for i in range (1,17,1):
    maTortueNinja.forward(80+i*10)
    maTortueNinja.left(90)

    maTortueNinja.forward(500)
    maTortueNinja.left(90)
    maTortueNinja.forward(60)
    maTortueNinja.left(90)
    maTortueNinja.forward(240)"""


# pour faire un escargot carré

"""

for i in range (1,500,1):
    maTortueNinja.forward(20+i*5)
    maTortueNinja.left(90)"""


# pour faire un escargot rond

"""for i in range (1,5000,1):
    maTortueNinja.forward(1+i/750)
    maTortueNinja.left(1)"""

#deplacement aléatoire de 4 tortues
'''
def randomRightLeft(tortueNinja):
    res=random.randint(0,2)
    if res==1:
        tortueNinja.left(90)
    else:
        tortueNinja.right(90)



def deplacementalea(tortueNinja):   
    
        salade=random.randint(0,60)
        tortueNinja.forward(salade)
        randomRightLeft(tortueNinja)

for i in range(0,1000,1):
    deplacementalea(maTortueNinja3)
    deplacementalea(maTortueNinja2)
    deplacementalea(maTortueNinja1)
    deplacementalea(maTortueNinja)

'''


#agar.o

turtle.pendown()

def randomRightLeft(tortueNinja):
    res=random.randint(0,2)
    if res==1:
        tortueNinja.left(90)
    else:
        tortueNinja.right(90)



def deplacementalea(tortueNinja):   
    
        salade=random.randint(0,60)
        tortueNinja.forward(salade)
        randomRightLeft(tortueNinja)








#mouvement du joueur
def directHaut ():
    turtle.setheading (90)
def directBas ():
    turtle.setheading (270)
def directGauche ():
    turtle.setheading (180)
def direcDroite ():
    turtle.setheading (0)


turtle.onkeypress(directHaut,"Up")
turtle.onkeypress(directBas,"Down")
turtle.onkeypress(directGauche,"Left")
turtle.onkeypress(direcDroite,"Right")
turtle.listen()


while 1:
    turtle.speed(0)
    turtle.forward(6)

    for i in liste:
        deplacementalea(i)

    for i in range(n-1):
        if turtle.distance(liste[i]) < size*7:
            liste[i].hideturtle()
            del liste[i]
            size = size+0,5
            turtle.shapesize(size)


input()

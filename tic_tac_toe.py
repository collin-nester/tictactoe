#tictactoe
import turtle

def pos1x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(10)
    tim.left(90)
    tim.forward(110)
    tim.right(45)
    tim.pendown()
    tim.forward(113)
    tim.right(135)
    tim.penup()
    tim.forward(80)
    tim.pendown()
    tim.right(135)
    tim.forward(113)
    tim.color("white")
    tim.forward(10)
def pos1o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.penup()
    tim.left(90)
    tim.forward(150)
    tim.pendown()
    tim.left(180)
    tim.circle(40)
    tim.penup()
    tim.color("white")
    tim.forward(40)
def pos2x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(110)
    tim.left(90)
    tim.forward(110)
    tim.pendown()
    tim.right(45)
    tim.forward(113)
    tim.right(135)
    tim.penup()
    tim.forward(80)
    tim.pendown()
    tim.right(135)
    tim.forward(113)
    tim.color("white")
    tim.forward(10)
def pos2o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.penup()
    tim.forward(150)
    tim.left(90)
    tim.forward(110)
    tim.pendown()
    tim.right(90)
    tim.circle(40)
    tim.left(90)
    tim.color("white")
    tim.penup()
    tim.forward(40)
def pos3x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(210)
    tim.left(90)
    tim.forward(110)
    tim.right(45)
    tim.pendown()
    tim.forward(113)
    tim.penup()
    tim.right(135)
    tim.forward(80)
    tim.right(135)
    tim.pendown()
    tim.forward(113)
    tim.color("white")
    tim.penup()
    tim.forward(10)
def pos3o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.penup()
    tim.forward(250)
    tim.left(90)
    tim.forward(110)
    tim.right(90)
    tim.pendown()
    tim.circle(40)
    tim.penup()
    tim.color("white")
    tim.left(90)
    tim.forward(40)
def pos4x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(10)
    tim.left(90)
    tim.forward(10)
    tim.right(45)
    tim.pendown()
    tim.forward(113)
    tim.right(135)
    tim.penup()
    tim.forward(80)
    tim.pendown()
    tim.right(135)
    tim.forward(113)
    tim.color("white")
    tim.forward(10)
def pos4o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)
    tim.backward(10)
    tim.left(90)
    tim.pendown()
    tim.circle(40)
    tim.penup()
    tim.color("white")
    tim.forward(40)
def pos5x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(110)
    tim.left(90)
    tim.forward(10)
    tim.pendown()
    tim.right(45)
    tim.forward(113)
    tim.right(135)
    tim.penup()
    tim.forward(80)
    tim.pendown()
    tim.right(135)
    tim.forward(113)
    tim.color("white")
    tim.forward(10)
def pos5o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.penup()
    tim.forward(150)
    tim.left(90)
    tim.forward(10)
    tim.pendown()
    tim.right(90)
    tim.circle(40)
    tim.left(90)
    tim.color("white")
    tim.penup()
    tim.forward(40)
def pos6x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(210)
    tim.left(90)
    tim.forward(10)
    tim.right(45)
    tim.pendown()
    tim.forward(113)
    tim.penup()
    tim.right(135)
    tim.forward(80)
    tim.right(135)
    tim.pendown()
    tim.forward(113)
    tim.color("white")
    tim.penup()
    tim.forward(10)
def pos6o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.penup()
    tim.forward(250)
    tim.left(90)
    tim.forward(10)
    tim.right(90)
    tim.pendown()
    tim.circle(40)
    tim.penup()
    tim.color("white")
    tim.left(90)
    tim.forward(40)
def pos7x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(10)
    tim.left(90)
    tim.backward(90)
    tim.right(45)
    tim.pendown()
    tim.forward(113)
    tim.right(135)
    tim.penup()
    tim.forward(80)
    tim.pendown()
    tim.right(135)
    tim.forward(113)
    tim.color("white")
    tim.forward(10)
def pos7o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.penup()
    tim.forward(10)
    tim.right(90)
    tim.forward(50)
    tim.pendown()
    tim.circle(40)
    tim.penup()
    tim.color("white")
    tim.forward(40)
def pos8x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(110)
    tim.left(90)
    tim.backward(90)
    tim.pendown()
    tim.right(45)
    tim.forward(113)
    tim.right(135)
    tim.penup()
    tim.forward(80)
    tim.pendown()
    tim.right(135)
    tim.forward(113)
    tim.color("white")
    tim.forward(10)
def pos8o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.penup()
    tim.forward(150)
    tim.left(90)
    tim.backward(90)
    tim.pendown()
    tim.right(90)
    tim.circle(40)
    tim.left(90)
    tim.color("white")
    tim.penup()
    tim.forward(40)
def pos9x():
    tim=turtle.Turtle()
    tim.color("red")
    tim.penup()
    tim.forward(210)
    tim.left(90)
    tim.backward(90)
    tim.right(45)
    tim.pendown()
    tim.forward(113)
    tim.penup()
    tim.right(135)
    tim.forward(80)
    tim.right(135)
    tim.pendown()
    tim.forward(113)
    tim.color("white")
    tim.penup()
    tim.forward(10)
def pos9o():
    tim=turtle.Turtle()
    tim.color("blue")
    tim.penup()
    tim.forward(250)
    tim.left(90)
    tim.backward(90)
    tim.right(90)
    tim.pendown()
    tim.circle(40)
    tim.penup()
    tim.color("white")
    tim.left(90)
    tim.forward(40)
def main():
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    x=0
    xList=[""]
    oList=[""]
    usedList=[]
    tommy=turtle.Turtle()
    tommy.speed(100)
    tommy.forward(300)
    tommy.penup()
    tommy.left(90)
    tommy.forward(100)
    tommy.left(90)
    tommy.pendown()
    tommy.forward(300)
    tommy.penup()
    tommy.backward(100)
    tommy.left(90)
    tommy.backward(100)
    tommy.pendown()
    tommy.forward(300)
    tommy.penup()
    tommy.left(90)
    tommy.forward(100)
    tommy.pendown()
    tommy.left(90)
    tommy.forward(300)
    tommy.color("white")
    tommy.forward(50)
    while x<9:
        y=0
        if x==0 or x==2 or x==4 or x==6 or x==8:
            xSpot=input("What position do you want to put your x in? ")
            if xSpot not in usedList:
                xList.insert(0,xSpot)
                usedList.append(xSpot)
            else:
                print("Oops. You have already filled this spot. Try again.")
                y=1
        if x==1 or x==3 or x==5 or x==7:
            oSpot=input("What position do you want to put your o in? ")
            if oSpot not in usedList:
                oList.insert(0,oSpot)
                usedList.append(oSpot)
            else:
                print("Oops. You have already filled this spot. Try again.")
                y=1
        if y==1:
            x=x-1
        if xList[0]=="1":
            pos1x()
        if oList[0]=="1":
            pos1o()
        if xList[0]=="2":
            pos2x()
        if oList[0]=="2":
            pos2o()
        if xList[0]=="3":
            pos3x()
        if oList[0]=="3":
            pos3o()
        if xList[0]=="4":
            pos4x()
        if oList[0]=="4":
            pos4o()
        if xList[0]=="5":
            pos5x()
        if oList[0]=="5":
            pos5o()
        if xList[0]=="6":
            pos6x()
        if oList[0]=="6":
            pos6o()
        if xList[0]=="7":
            pos7x()
        if oList[0]=="7":
            pos7o()
        if xList[0]=="8":
            pos8x()
        if oList[0]=="8":
            pos8o()
        if xList[0]=="9":
            pos9x()
        if oList[0]=="9":
            pos9o()
        oList.insert(0,"")
        xList.insert(0,"")
        x=x+1
        if x==9:
            print("Tie game")
        if "1" in xList and "2" in xList and "3" in xList or "1" in xList and "4" in xList and "7" in xList or "1" in xList and "5" in xList and "9" in xList or "2" in xList and "5" in xList and "8" in xList or "3" in xList and "6" in xList and "9" in xList or "3" in xList and "5" in xList and "7" in xList or "4" in xList and "5" in xList and "6" in xList or "2" in xList and "5" in xList and "8" in xList or "7" in xList and "8" in xList and "9" in xList: 
            print("X wins!!!!!")
            x=9
        if "1" in oList and "2" in oList and "3" in oList or "1" in oList and "4" in oList and "7" in oList or "1" in oList and "5" in oList and "9" in oList or "2" in oList and "5" in oList and "8" in oList or "3" in oList and "6" in oList and "9" in oList or "3" in oList and "5" in oList and "7" in oList or "4" in oList and "5" in oList and "6" in oList or "2" in oList and "5" in oList and "8" in oList or "7" in oList and "8" in oList and "9" in oList: 
            print("O wins!!!!!")
            x=9
main()

# import pgzrun
# from random import randint
# apple = Actor("apple")
# orange = Actor("orange")
# pineapple = Actor("pineapple")
# def draw():
#     screen.clear()
#     screen.fill("pink")
#     apple.draw()
#     pineapple.draw()
#     orange.draw()
# def place_apple():
#     apple.x = randint(50, 400)
#     apple.y = randint(50,400)
# def place_pineapple():
#     pineapple.x = randint(90, 600)
#     pineapple.y = randint(90,400)
# place_pineapple()
# def place_orange():
#     orange.x = randint(100, 800)
#     orange.y = randint(100,300)
# place_orange()
# def on_mouse_down(pos):
   
#         if  apple.collidepoint(pos):
#             print("Good shot!")
#             place_apple()
    
#         else:
#             print("You missed!")
#         if  pineapple.collidepoint(pos):
#             place_pineapple() 
#         if orange.collidepoint(pos):
#             place_orange()
    
# pgzrun.go()

import pgzrun
from random import randint

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
fruits = [apple, orange, pineapple]

def draw():
    screen.clear()
    screen.fill("pink")
    for fruit in fruits:
        fruit.draw()

def place_fruit(fruit):
    fruit.x = randint(50, 800)
    fruit.y = randint(50, 400)

def on_mouse_down(pos):
    for fruit in fruits:
        if fruit.collidepoint(pos):
            print("Good shot!")
            place_fruit(fruit)

pgzrun.go()


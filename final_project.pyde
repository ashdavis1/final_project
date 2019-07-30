def setup():
    global yogoogle,x,y,gameStarted,firstScreen
    size(1680,1000)
    background(90, 100, 255)
    yogoogle = "YO GOOGLE"
    img = loadImage("multipleandroids.jpg")
    image(img,0,0,1680,1000)
    x = True
    y = True
    x2 = True
    y2 = True
    firstScreen(x,y)
    # secondScreen (x2,y2)
    gameStarted = False
    frameRate = 10
    gameStarted2 = False

    
    
    
def firstScreen(x,y):
# start screen
    fill(random(255),random(255),random(255))
    textSize (90)
    text ("YO GOOGLE", 800,1200)
    text(yogoogle ,570,100)
    textSize(42)
    fill(0)
    text ("Click To Begin YO GAME", 600, 900)
#second screen
def draw():
    pass
def mousePressed():
    global gameStarted
    gameStarted = True
    secondScreen()
    
            
def secondScreen():
    print("To Do")
    size(1680,1000)
    background(0,110,255)
    img = loadImage("android.jpg")
    image(img,0,0,250,150)
    image(img,1450,0,250,150)
#rect 1 
    rect(300,250,350,250)
# rect 2
    rect(600,600,350,250)
# rect 3 
    rect(1000,250,350,250)
    # thirdScreen()
    
    

    
    
def thirdScreen():

    size(1680,1000)
    # background(102, 102, 153)
    


    

    




    
    




        
    
    

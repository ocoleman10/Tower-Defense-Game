# ====================================================================================================
# Program: Final Project
# Author: Omar Coleman
# Description: The classes for my project
# Date Modified: 5/29/2022
# Version: 1.0
# ====================================================================================================
# Import Libraries
from graphics import *
import random
# import simpleaudio
# ====================================================================================================
class Weapon:
    def __init__(self, x, y, dmg, size, reloadAmmo, ammo, relaodTime, imgURL, window:GraphWin):
        """Constructs a weapon object."""
        self.x = x
        self.y = y
        self.dmg = dmg
        self.size = size
        self.reloadAmmo = reloadAmmo
        self.ammo = ammo
        self.reloadTime = relaodTime
        self.imgURL = imgURL
        self.window = window
        self.speed = 10
        self.image = Image(Point(x, y), imgURL)
        self.firing = False
        self.projectiles = []
        self.reloadTxt = Image(Point(650, 400), "Assets/TitleStuff/reload.png")
        self.reloadTxt.transform(0.5)
    def draw(self):
        """Function draws the weapon."""
        self.image.transform(self.size)
        self.image.undraw()
        self.image.draw(self.window)
    def update(self):
        """Function updates the state of the weapon."""
        self.shoot()
    def shoot(self):
        """Function fires the bullet/projectile."""
        if self.window.mousePressed and not self.firing:
            mouse = self.window.getCurrentMouseLocation()
            velX = 0.5 * (mouse.x - self.x)
            velY = 0.5 * (mouse.y - self.y)
            if self.ammo > 0:
                self.projectiles.append(Projectile(10, self.x, self.y, 0.06, self.window, "", velX, velY))
                self.ammo -= 1
            firing = True
        if not self.window.mousePressed:
            firing = False
        for projectile in self.projectiles:
            projectile.update()
            if projectile.x < 0 or projectile.x > self.window.getWidth() or projectile.y < 0 or projectile.y > self.window.getHeight():
                projectile.image.undraw()
        return True
    def reload(self):
        """Function reloads the weapon."""
        if len(self.projectiles) >= self.ammo:
            self.reloadTxt.undraw()
            self.reloadTxt.draw(self.window)
            for projectile in self.projectiles:
                projectile.velX = 0
                projectile.velX = 0
                projectile.undraw()
        keys = self.window.checkKeys()
        if "r" in keys:
            for projectile in self.projectiles:
                projectile.undraw()
            self.projectiles.clear()
            self.reloadTxt.undraw()
            self.ammo = self.reloadAmmo

class Minigun(Weapon):
    def __init__(self, x, y, dmg, size, reloadAmmo, ammo, realoadTime, imgURL, window:GraphWin):
        """Constructs a minigun weapon."""
        super().__init__(x, y, dmg, size, reloadAmmo,ammo, realoadTime, imgURL, window)
    def shoot(self):
        """Function fires the bullet/projectile."""
        if self.window.mousePressed and not self.firing:
            mouse = self.window.getCurrentMouseLocation()
            velX = 0.1 * (mouse.x - self.x)
            velY = 0.1 * (mouse.y - self.y)
            self.projectiles.append(Projectile(10, self.x, self.y, 0.06, self.window, f"Assets/Weapons/Bullet (1).png", velX, velY))
            firing = True
        if not self.window.mousePressed:
            firing = False
        for projectile in self.projectiles:
            projectile.update()
            if projectile.x < 0 or projectile.x > self.window.getWidth() or projectile.y < 0 or projectile.y > self.window.getHeight():
                projectile.image.undraw()

class RocketLauncher(Weapon):
    def __init__(self, x, y, dmg, size, reloadAmmo, ammo, realoadTime, imgURL, window:GraphWin):
        """Constructs a minigun weapon."""
        super().__init__(x, y, dmg, size, reloadAmmo,ammo, realoadTime, imgURL, window)
    def shoot(self):
        """Function fires the rocket/projectile."""
        if self.window.mousePressed and not self.firing:
            mouse = self.window.getCurrentMouseLocation()
            velX = 0.1 * (mouse.x - self.x)
            velY = 0.1 * (mouse.y - self.y)
            self.projectiles.append(Projectile(10, self.x, self.y, 0.5, self.window, f"Assets/Weapons/rocketprojectile.png", velX, velY))
            firing = True
        if not self.window.mousePressed:
            firing = False
        for projectile in self.projectiles:
            projectile.update()
            if projectile.x < 0 or projectile.x > self.window.getWidth() or projectile.y < 0 or projectile.y > self.window.getHeight():
                projectile.image.undraw()

class Projectile:
    def __init__(self, dmg, x, y, size, window:GraphWin, imgURL, velX, velY):
        """Constructs a projectile object."""
        self.x = x
        self.y = y
        self.dmg = dmg
        self.size = size
        self.window = window
        self.imgURL = imgURL
        self.velX = velX
        self.velY = velY
        self.angle = 0
        self.image = Image(Point(x, y), imgURL)
    def update(self):
        """Function updates the state of the projectile."""
        self.image.undraw()
        self.image.transform(self.size, self.angle)
        self.angle += 10
        self.x += self.velX
        self.y += self.velY
        self.image.anchor = Point(self.x, self.y)
        self.image.draw(self.window)
    def undraw(self):
        """Function undraws the projectile."""
        self.image.undraw()
    def getImgURL(self):
        """Function returns the image URL"""
        return self.imgURL
    def getDamage(self):
        """Returns self.dmg."""
        return self.dmg

class Alien:
    def __init__(self, x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window:GraphWin):
        """Constructs an alien object."""
        self.x = x
        self.y = y
        self.health = health
        self.attackDMG = attackDMG
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.wallHealth = wallHealth
        self.limit = limit
        self.window = window
        self.size = size
        self.walkForward = []
        self.loadImages()
        self.imgIndex = 0
    def loadImages(self):
        """Function adds images to list so that they are able to show."""
        self.walkForward.append(Image(Point(self.x, self.y), ""))
        self.walkForward.append(Image(Point(self.x, self.y), ""))
        for image in self.walkForward:
            image.transform(0.3)
    def show(self):
        """Function shows the aliens on the graphics window."""
        self.walkForward[self.imgIndex].undraw()
        self.imgIndex = (self.imgIndex + 1) % len(self.walkForward)
        self.walkForward[self.imgIndex].anchor = Point(self.x, self.y)
        self.walkForward[self.imgIndex].draw(self.window)
    def unDraw(self):
        """Functions undraws the images."""
        for image in self.walkForward:
            image.undraw()
    def walk(self, x, y):
        """Function moves the aliens to make it look like their walking closer."""
        self.x += x
        self.y += y
        if self.y >= self.limit:
            self.y = self.limit
            return True
    def attack(self):
        """Method allows alien to attack the base."""
        if self.y >= self.limit:
            self.wallHealth -= 1
            if self.wallHealth <= 0:
                return True
    def die(self, projectiles):
        """Method allows the alien to die when all health is lost."""
        for alienImage in self.walkForward:
            for projectile in projectiles:
                if Image.testCollision_ImageVsImage(alienImage, projectile.image):
                    self.health -= projectile.getDamage()
                    if self.health <= 0:
                        projectile.undraw()
                        self.walkForward[0].undraw()
                        self.walkForward[1].undraw()
                        projectiles.remove(projectile)
                        return True
        return False
    def getHealth(self):
        """Returns the alines health."""
        return self.health

class IRobot(Alien):
    def __init__(self, x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window:GraphWin):
        """Constructs a IRobot alien type."""
        super().__init__(x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window)
    def loadImages(self):
        """Function adds certain images to list so that they are able to show."""
        self.walkForward.append(Image(Point(self.x, self.y), "Assets/Irobot/Irobot0.png"))
        self.walkForward.append(Image(Point(self.x, self.y), "Assets/Irobot/Irobot1.png"))
        for image in self.walkForward:
            image.transform(0.3)

class ArmoredAlien(Alien):
    def __init__(self, x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window:GraphWin):
        """Constructs a IRobot alien type."""
        super().__init__(x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window)
    def loadImages(self):
        """Function adds certain images to list so that they are able to show."""
        self.walkForward.append(Image(Point(self.x, self.y), "Assets/ArmoredAlien/ArmoredAlien0.png"))
        self.walkForward.append(Image(Point(self.x, self.y), "Assets/ArmoredAlien/ArmoredAlien1.png"))
        for image in self.walkForward:
            image.transform(0.3)

class BirdAlien(Alien):
    def __init__(self, x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window:GraphWin):
        """Constructs a IRobot alien type."""
        super().__init__(x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window)
    def loadImages(self):
        """Function adds certain images to list so that they are able to show."""
        self.walkForward.append(Image(Point(self.x, self.y), "Assets/BirdAlien/BirdAlien0.png"))
        self.walkForward.append(Image(Point(self.x, self.y), "Assets/BirdAlien/BirdAlien1.png"))
        for image in self.walkForward:
            image.transform(0.3)

class GiantAlien(Alien):
    def __init__(self, x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window:GraphWin):
        """Constructs a IRobot alien type."""
        super().__init__(x, y, health, attackDMG, pos, vel, acc, size, wallHealth, limit, window)
    def loadImages(self):
        """Function adds certain images to list so that they are able to show."""
        self.walkForward.append(Image(Point(self.x, self.y), "Assets/GiantAlien/GiantAlien0.png"))
        self.walkForward.append(Image(Point(self.x, self.y), "Assets/GiantAlien/GiantAlien1.png"))
        for image in self.walkForward:
            image.transform(0.3)

class GameScreen:
    def __init__(self, x, y, x2, y2, width, height, imgURL, size, window:GraphWin):
        """Contructs a game screen."""
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.height = height
        self.imgURL = imgURL
        self.size = size
        self.window = window
        self.boundary = Rectangle(Point(x, y), (Point(x + width, y + height)))
        self.txt = Image(Point(x2, y2), f"{self.imgURL}")
    def resize(self):
        """Resizes title screen objects."""
        self.txt.transform(self.size)
    def setBackground(self, color):
        """Sets the color for the game screen."""
        self.boundary.setFill(f"{color}")
    def show(self):
        """Draws the game screen to the window."""
        self.boundary.undraw()
        self.boundary.draw(self.window)
        self.txt.undraw()
        self.txt.draw(self.window)
    def undraw(self):
        """Undraws the game screen from the window."""
        self.boundary.undraw()
        self.txt.undraw()
    def proceed(self, key):
        """Allows the game to resume based on user input."""
        keys = self.window.checkKeys()
        if f"{key}" in keys:
            self.boundary.undraw()
            self.txt.undraw()
            return True

class GameOverScreen(GameScreen):
    """Contructs a game over screen."""
    def __init__(self, x, y, x2, y2, width, height, imgURL, size, window:GraphWin):
        super().__init__(x, y, x2, y2, width, height, imgURL, size, window)

class LevelCompleteScreen(GameScreen):
    """Contructs a level complete screen."""
    def __init__(self, x, y, x2, y2, width, height, imgURL, size, window:GraphWin):
        super().__init__(x, y, x2, y2, width, height, imgURL, size, window)
class titleScreen(GameScreen):
    """Contructs a level complete screen."""
    def __init__(self, x, y, x2, y2, width, height, imgURL, size,  window:GraphWin):
        super().__init__(x, y, x2, y2, width, height, imgURL, size, window)
# =======================================================================================================================
# =======================================================================================================================
# =======================================================================================================================
# Function for the game background.
def background(buildings, plants, transportation, wall, window):
    """Function draws the background of the game."""
    #BUILDINGS
    faceTower = Image(Point(220, 227), "Assets/Buildings/Face Tower.png")
    faceTower.transform(0.4)
    buildings.append(faceTower)
    # ====================================================================================================
    twoSlantTower = Image(Point(275, 230), "Assets/Buildings/2 slant tower.png")
    twoSlantTower.transform(0.6)
    buildings.append(twoSlantTower)
    # ====================================================================================================
    diamondTower = Image(Point(350, 208), "Assets/Buildings/Diamond Tower.png")
    diamondTower.transform(1.2)
    buildings.append(diamondTower)
    # ====================================================================================================
    willisTower = Image(Point(520, 203), "Assets/Buildings/Willis Tower.png")
    willisTower.transform(0.9)
    buildings.append(willisTower)
    # ====================================================================================================
    checkersBuildingDES = Image(Point(430, 234), "Assets/Destroyed Buildings/Checkers Building Destroyed (1).png")
    checkersBuildingDES.transform(0.6)
    buildings.append(checkersBuildingDES)
    # ====================================================================================================
    lineBuilding = Image(Point(555, 236), "Assets/Buildings/Line Building.png")
    lineBuilding.transform(0.6)
    buildings.append(lineBuilding)
    # ====================================================================================================
    grayGenericBuilding = Image(Point(605, 230), "Assets/Buildings/Gray Generic Building.png")
    grayGenericBuilding.transform(0.9)
    buildings.append(grayGenericBuilding)
    # ====================================================================================================
    faceTowerDES = Image(Point(650, 261), "Assets/Destroyed Buildings/Face Tower Destroyed.png")
    faceTowerDES.transform(0.3)
    buildings.append(faceTowerDES)
    # ====================================================================================================
    checkersBuilding = Image(Point(710, 216), "Assets/Buildings/Checkers Building (1).png")
    checkersBuilding.transform(0.8)
    buildings.append(checkersBuilding)
    # ====================================================================================================
    glassTower = Image(Point(765, 246), "Assets/Buildings/glass tower.png")
    glassTower.transform(0.5)
    buildings.append(glassTower)
    # ====================================================================================================
    windowBuilding = Image(Point(823, 276), "Assets/Buildings/Window Building.png")
    windowBuilding.transform(0.3)
    buildings.append(windowBuilding)
    # ====================================================================================================
    lineBuildingDES = Image(Point(885, 229), "Assets/Destroyed Buildings/Line Building Destroyed.png")
    lineBuildingDES.transform(0.7)
    buildings.append(lineBuildingDES)
    # ====================================================================================================
    genericBuildingDESTwo = Image(Point(940, 230), "Assets/Destroyed Buildings/Generic Building Destroyed(2).png")
    genericBuildingDESTwo.transform(0.9)
    buildings.append(genericBuildingDESTwo)
    # ====================================================================================================
    genericBuilding = Image(Point(1010, 225), "Assets/Buildings/Generic Building.png")
    genericBuilding.transform(1)
    buildings.append(genericBuilding)
    # ====================================================================================================
    maskedBuilding = Image(Point(1060, 266), "Assets/Buildings/Masked Building.png")
    maskedBuilding.transform(0.3)
    buildings.append(maskedBuilding)
    # ====================================================================================================
    #PLANTS AND GRASS
    counter = 0
    counter2 = 0
    for i in range(15):
        grass = Image(Point(0 + counter, 450 + counter2), "Assets/Plants/Grass (2).png")
        grass.transform(1)
        plants.append(grass)
        if counter > 1300:
            counter = -20
            counter2 += 180
        counter += 190
    # ====================================================================================================
    #LEFT SIDE TREES
    skinnyTree = Image(Point(40, 450), "Assets/plants/Skinny Tree.png")
    skinnyTree.transform(2)
    plants.append(skinnyTree)

    mediumTree = Image(Point(200, 300), "Assets/Plants/Medium Tree.png")
    mediumTree.transform(2)
    plants.append(mediumTree)

    tallTree = Image(Point(30, 625), "Assets/plants/Tall Messy tree.png")
    tallTree.transform(2.5)
    plants.append(tallTree)

    bigTree = Image(Point(100, 455), "Assets/plants/Big Tree.png")
    bigTree.transform(1.5)
    plants.append(bigTree)

    genericTree = Image(Point(230, 345), "Assets/plants/Generic Tree.png")
    genericTree.transform(2.5)
    plants.append(genericTree)
    #=======================================================================
    #RIGHT SIDE TREES
    skinnyTree2 = Image(Point(1260, 500), "Assets/plants/Skinny Tree.png")
    skinnyTree2.transform(2)
    plants.append(skinnyTree2)

    tallTree2 = Image(Point(1205, 400), "Assets/plants/Tall Messy Tree.png")
    tallTree2.transform(1.5)
    plants.append(tallTree2)

    mediumTree2 = Image(Point(1125, 340), "Assets/Plants/Medium Tree.png")
    mediumTree2.transform(2)
    plants.append(mediumTree2)

    tallTree2 = Image(Point(1270, 675), "Assets/plants/Tall Messy tree.png")
    tallTree2.transform(2)
    plants.append(tallTree2)

    bigTree2 = Image(Point(1210, 505), "Assets/plants/Big Tree.png")
    bigTree2.transform(1.5)
    plants.append(bigTree2)

    genericTree2 = Image(Point(1150, 405), "Assets/plants/Generic Tree.png")
    genericTree2.transform(2.5)
    plants.append(genericTree2)
    # ====================================================================================================
    #TRANSPORTATION METHODS
    pavementCounter = 0
    for i in range(45):
        pavement1 = Image(Point(230 + pavementCounter, 300), "Assets/Transportation/Pavement.png")
        pavement1.transform(0.3)
        transportation.append(pavement1)
        pavement2 = Image(Point(230 + pavementCounter, 320), "Assets/Transportation/Pavement.png")
        pavement2.transform(0.3)
        transportation.append(pavement2)
        pavementCounter += 20
    roadCounter = 0
    for i in range(45):
        road = Image(Point(240 + roadCounter, 305), "Assets/Transportation/Road.png")
        road.transform(0.15)
        transportation.append(road)
        roadCounter += 20
    riverCounter = 0
    for i in range(22):
        river = Image(Point(265 + riverCounter, 339), "Assets/Transportation/River.png")
        river.transform(0.7)
        transportation.append(river)
        riverCounter += 35
    # ====================================================================================================
    # MOUNTAINS
    mountain1 = Polygon(Point(100,300), Point(195, 300), Point(150, 150))
    mountain1.setFill("gray")
    mountain1.setOutline("black")
    mountain1.draw(window)

    mountain3 = Polygon(Point(380, 300), Point(519, 300), Point(435, 94))
    mountain3.setFill("gray")
    mountain3.setOutline("black")
    mountain3.draw(window)

    mountain2 = Polygon(Point(150, 300), Point(450, 300), Point(299, 94))
    mountain2.setFill("gray")
    mountain2.setOutline("black")
    mountain2.draw(window)

    mountain5 = Polygon(Point(640, 300), Point(760, 100), Point(905, 300))
    mountain5.setFill("gray")
    mountain5.setOutline("black")
    mountain5.draw(window)

    mountain7 = Polygon(Point(800, 300), Point(1025, 50), Point(1220, 300))
    mountain7.setFill("gray")
    mountain7.setOutline("black")
    mountain7.draw(window)

    mountain4 = Polygon(Point(519, 300), Point(610, 165), Point(720, 300))
    mountain4.setFill("gray")
    mountain4.setOutline("black")
    mountain4.draw(window)

    mountain8 = Polygon(Point(1150, 300), Point(1240, 300), Point(1420, 300))
    mountain8.setFill("gray")
    mountain8.setOutline("black")
    mountain8.draw(window)
    # ====================================================================================================
    # WALL/BASE
    wallFloorCounter = 0
    wallBlockCounter = 0
    for i in range(20):
        wallFloor = Image(Point(5 + wallFloorCounter, 675), "Assets/Wall/Wall Floor.png")
        wallFloor.transform(2)
        wallBlock = Image(Point(5 + wallBlockCounter, 690), "Assets/Wall/Wall Block.png")
        wallBlock.transform(0.5)
        wall.append(wallFloor)
        wall.append(wallBlock)
        wallFloorCounter += 250
        wallBlockCounter += 68

    return buildings, plants, transportation, wall
# ======================================================================================================================
# Functions for the gameplay.

IRobotAliens = []
AAliens = []
BirdAliens = []
GiantAliens = []
def spawnAliens(window, numOfAliens):
    """Function spawns the aliens to the game/window."""
    IRobotCounter1 = 0
    IRobotCounter2 = 0
    AAlienCounter1 = 0
    AAlienCounter2 = 0
    BirdAlienCounter1 = 0
    BirdAlienCounter2 = 0
    GiantAlienCounter1 = 0
    GiantAlienCounter2 = 0
    for i in range(numOfAliens):
        IRobotAliens.append(IRobot(550 + IRobotCounter1, 370 + IRobotCounter2, 300, 5, 1, 1, 1, 5, 300, 630, window))
        IRobotCounter1 = random.randrange(0, 100)
        IRobotCounter2 = random.randrange(0, 100)
        AAliens.append(ArmoredAlien(350 + AAlienCounter1, 370 + AAlienCounter2, 400, 5, 1, 1, 1, 5, 300, 630, window))
        AAlienCounter1 = random.randrange(0, 100)
        AAlienCounter2 = random.randrange(0, 100)
        BirdAliens.append(BirdAlien(650 + BirdAlienCounter1, 275 + BirdAlienCounter2, 250, 5, 1, 1, 1, 5, 300, 630, window))
        BirdAlienCounter1 = random.randrange(0, 100)
        BirdAlienCounter2 = random.randrange(0, 100)
        GiantAliens.append(GiantAlien(750 + GiantAlienCounter1, 370 + GiantAlienCounter2, 500, 5, 1, 1, 1, 5, 300, 630, window))
        GiantAlienCounter1 = random.randrange(0, 100)
        GiantAlienCounter2 = random.randrange(0, 100)
def moveAliens():
    """Function moves the aliens on the window."""
    for alien in IRobotAliens:
        alien.show()
        alien.walk(0, 0.2)
    for alien in AAliens:
        alien.show()
        alien.walk(0, 0.2)
    for alien in BirdAliens:
        alien.show()
        alien.walk(0, 0.2)
    for alien in GiantAliens:
        alien.show()
        alien.walk(0, 0.2)
def aliensAttack():
    """Functions allows the alien to deal damage to the wall."""
    for alien in IRobotAliens:
        alien.attack()
        if alien.attack():
            return True
        else:
            return False
    for alien in AAliens:
        alien.attack()
        if alien.attack():
            return True
        else:
            return False
    for alien in BirdAliens:
        alien.attack()
        if alien.attack():
            return True
        else:
            return False
    for alien in GiantAliens:
        alien.attack()
        if alien.attack():
            return True
        else:
            return False


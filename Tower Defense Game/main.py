# ====================================================================================================
# Program: Final Project
# Author: Omar Coleman
# Description: Main program for my project
# Date Modified: 8/3/2025
# Version: 1.0
# ====================================================================================================
# Import Libraries
import simpleaudio

from classes import *
# ====================================================================================================
# Global Variables
window = GraphWin("Defend The City", 1300, 800, autoflush=False)
minigun = Minigun(600, 720, 10, 1, 50, 50, 5, "Assets/Weapons/Minigun.png", window)
bullet = Projectile(10, 600, 720, 0.1, window, "Assets/Weapons/Bullet (1).png", 100, 100)
rocketlauncher = RocketLauncher(600, 720, 10, 1, 50, 50, 5, "Assets/Weapons/rocketlauncher.png", window)
rocket = Projectile(10, 600, 720, 1, window, "Assets/Weapons/rocketprojectile.png", 100, 100)
# ====================================================================================================
gOverScreen = GameOverScreen(0, 0, 650, 400, 1300, 800, "Assets/TitleStuff/gameover.png", 1, window)
gOverScreen.setBackground("Black")
lvlCompleteScreen = LevelCompleteScreen(0, 0, 650, 400, 1300, 800, "Assets/TitleStuff/levelcomplete.png", 0.75, window)
lvlCompleteScreen.setBackground("Black")
tScreen = titleScreen(0, 0, 650, 300, 1300, 800, "Assets/TitleStuff/titlescreen.png", 0.75, window)
tScreen.setBackground("White")
tScreen.resize()
tScreenInstructions = titleScreen(0, 0, 670, 700, 1300, 800, "Assets/TitleStuff/pause.png", 0.4, window)
tScreenInstructions.resize()
tScreenESC = titleScreen(0, 0, 670, 750, 1300, 800, "Assets/TitleStuff/escape.png", 0.4, window)
tScreenESC.resize()
# ====================================================================================================
buildings = []
plants = []
transportation = []
wall = []
buildings, plants, transportation, wall = background(buildings, plants, transportation, wall, window)
# ====================================================================================================
# User-Defined Functions
def drawBackground():
    """Function draws the background of the game(city, sky, river)."""
    window.setBackground(color_rgb(88, 88, 88))
    for item in transportation:
        item.undraw()
        item.draw(window)
    for building in buildings:
        building.undraw()
        building.draw(window)
    for plant in plants:
        plant.undraw()
        plant.draw(window)
    for item in wall:
        item.undraw()
        item.draw(window)
def die():
    """Function will allow the aliens to die."""
    for alien in IRobotAliens:
        if alien.die(minigun.projectiles):
            IRobotAliens.remove(alien)
    for alien in AAliens:
        if alien.die(minigun.projectiles):
            AAliens.remove(alien)
    for alien in BirdAliens:
        if alien.die(minigun.projectiles):
            BirdAliens.remove(alien)
    for alien in GiantAliens:
        if alien.die(minigun.projectiles):
            GiantAliens.remove(alien)
def lvl1():
    """Function for level 1."""
    minigun.update()
    minigun.reload()
    bullet.update()
    moveAliens()
    die()
    aliensAttack()
    if aliensAttack():
        gOverScreen.show()
    if len(IRobotAliens) <= 0 and len(AAliens) <= 0 and len(BirdAliens) <= 0 and len(GiantAliens) <= 0:
        return True
# ====================================================================================================
# Main Function
def main():
    """Main function for program"""

    wave_obj = simpleaudio.WaveObject.from_wave_file("assets/sounds/gamemusic.wav")
    drawBackground()
    minigun.draw()
    spawnAliens(window, 1)
    tScreen.show()
    tScreenInstructions.show()
    tScreenESC.show()
    sound = wave_obj.play()
    while not window.closed:
        if tScreen.proceed("c") and tScreenInstructions.proceed("c") and tScreenESC.proceed("c") and not lvl1():
            sound.stop()
            lvl1()
            if lvl1():
                spawnAliens(window, 1)
                tScreen.undraw()
                tScreenInstructions.undraw()
                tScreenESC.undraw()
        else:
            if not sound.is_playing():
                sound = wave_obj.play()
            tScreen.show()
            tScreenInstructions.show()
            tScreenESC.show()
            keys = window.checkKeys()
            if "Escape" in keys:
                window.close()

        window.update()
# ====================================================================================================
# Call the Main Function
main()

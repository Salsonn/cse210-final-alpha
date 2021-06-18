# cse210-final Title
There's no time to explain! Grab a weapon and kill the weird things, and most importantly don't let them touch you!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and python Arcade installed 
and running on your machine. You can install Arcade by opening a terminal 
and running the following command.
```
python3 -m pip install arcade
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 rfk 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- gameNameHere               (source code for game)
  +-- game              (specific game classes)
    +-- director.py     (manages gameloop, level loading, etc)
    +-- physics.py      (manages entity movement and bouncing)
    +-- collision.py    (handles collision detection between entities)
    +-- entity.py       (basic characteristics of in-game entities)

  +-- maps              (stores map data for loading on demand)
    +-- mainMenu.map    (data for loading the main menu map)

  +-- img               (stores sprite data for all entities)
    +-- player          (stores sprite data for the player)

  +-- snd               (repository for sounds)
  
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Current Delegations
---
The following are different general tasks, claimed and unclaimed:

#### Caleb (Salsonn)
  * Movement Physics
  * Camera Physics
  * Collision Detection

#### Austin (pondels | The Elite Gamer)
  * Weapons
  * Projectiles
  * Game Art

#### Josh (coder199420 | coder20)
  * Map Design

#### Tyler (Tjcaldron)
  * [null]

#### Undelegated
  * Enemies (saving for later)


## Required Technologies
---
* Python 3.8.0
* Arcade

## Authors
---
* Caleb Salyards - sal18014@byui.edu
* Austin Oldroyd - old20004@byui.edu
* Josh Thieme - thi17001@byui.edu

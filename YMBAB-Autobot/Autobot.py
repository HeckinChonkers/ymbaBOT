from imagesearch import *
import numpy as np
import sys

#Sword = 0
#Shield = 1
#Wand = 2
#Key = 3
#Crate = 4
#Brain = 5
#Arm = 6
#Spell = 7
#NotFound = 8

startFromTop = True
positions = [[-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1]]

def build_grid_from_top():
    grid = [[-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1]]
    startY = 410

    #im = region_grabber((startX, startY, 1180, 1240))
    #im.save('testarea.png')#useful for debugging purposes, this will save the captured region as "testarea.png"

    #For every row (Y)
    for i in range(8):
        startX = 540
        #For every column in that row (X)
        for j in range(6):
            #grab that cell in the grid and store approx center position in positions matrix
            im = region_grabber((startX, startY, startX + 106, startY + 106))
            if positions[i][j] == -1:
                positions[i][j] = (600 + 106*(j), 450 + 106*(i))
            #the cells are roughly 106 pixels apart from left side to left side, so move the starting X to the next cell for next iteration
            startX = startX + 106
            #im.save('testarea{}{}.png'.format(j,i))#useful for debugging purposes, this will save the captured region as "testarea.png"

            #use image recognition to match cell type and mark it in the grid with the assigned number
            swordPOS = imagesearcharea("Sword.png", 0, 0, 106, 106, 0.8, im)
            sword2XPOS = imagesearcharea("2xSword.png", 0, 0, 106, 106, 0.8, im)
            if swordPOS[0] != -1 or sword2XPOS[0] != -1:
                grid[i][j] = 0
                continue
            shieldPOS = imagesearcharea("Shield.png", 0, 0, 106, 106, 0.8, im)
            if shieldPOS[0] != -1:
                grid[i][j] = 1
                continue
            wandPOS = imagesearcharea("Wand.png", 0, 0, 106, 106, 0.8, im)
            wand2XPOS = imagesearcharea("2xWand.png", 0, 0, 106, 106, 0.8, im)
            if wandPOS[0] != -1 or wand2XPOS[0] != -1:
                grid[i][j] = 2
                continue
            keyPOS = imagesearcharea("Key.png", 0, 0, 106, 106, 0.8, im)
            if keyPOS[0] != -1:
                grid[i][j] = 3
                continue
            cratePOS = imagesearcharea("Crate.png", 0, 0, 106, 106, 0.8, im)
            if cratePOS[0] != -1:
               grid[i][j] = 4
               continue
            brainPOS = imagesearcharea("Brain.png", 0, 0, 106, 106, 0.8, im)
            if brainPOS[0] != -1:
                grid[i][j] = 5
                continue
            armPOS = imagesearcharea("Arm.png", 0, 0, 106, 106, 0.8, im)
            if armPOS[0] != -1:
                grid[i][j] = 6
                continue
            lightningPOS = imagesearcharea("Lightning.png", 0, 0, 106, 106, 0.8, im)
            if lightningPOS[0] != -1:
                grid[i][j] = 7
                continue
            freezePOS = imagesearcharea("Freeze.png", 0, 0, 106, 106, 0.8, im)
            if freezePOS[0] != -1:
                grid[i][j] = 7
                continue
            firePOS = imagesearcharea("Fire.png", 0, 0, 106, 106, 0.8, im)
            if firePOS[0] != -1:
                grid[i][j] = 7
                continue
            tntPOS = imagesearcharea("tnt.png", 0, 0, 106, 106, 0.8, im)
            if tntPOS[0] != -1:
                grid[i][j] = 7
                continue
            shieldSpellPOS = imagesearcharea("shieldSpell.png", 0, 0, 106, 106, 0.8, im)
            if shieldSpellPOS[0] != -1:
                grid[i][j] = 7
                continue
            fishPOS = imagesearcharea("fish.png", 0, 0, 106, 106, 0.8, im)
            if fishPOS[0] != -1:
                grid[i][j] = 7
                continue
            bowPOS = imagesearcharea("bow.png", 0, 0, 106, 106, 0.8, im)
            if bowPOS[0] != -1:
                grid[i][j] = 7
                continue
            #if we haven't continued at this point, set the spot to Undefined number
            grid[i][j] = 8
        #the cells are roughly 106 pixels apart from top of one cell to the top of the cell beneath it, so move the starting Y to the next cell for next iteration
        startY = startY + 106
    #pretty print the matrix
    print("From top:")
    print(np.matrix(grid))
    return grid

def build_grid_from_bottom():
    grid = [[-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1]]
    startY = 1250
    #im = region_grabber((startX, startY, 1180, 1240))
    #im.save('testarea.png')#useful for debugging purposes, this will save the captured region as "testarea.png"
    #For every row (Y)
    for i in range(8):
        startX = 540
        #For every column in that row (X)
        for j in range(6):
            #grab that cell in the grid and store approx center position in positions matrix
            im = region_grabber((startX, startY- 106, startX + 106, startY))
            if positions[7-i][5-j] == -1:
                positions[7-i][5-j] = (600 + 106*(5-j), 450 + 106*(7-i))
            startX = startX + 106
            #im.save('testarea{}{}.png'.format(j,i))#useful for debugging purposes, this will save the captured region as "testarea.png"
            swordPOS = imagesearcharea("Sword.png", 0, 0, 106, 106, 0.8, im)
            sword2XPOS = imagesearcharea("2xSword.png", 0, 0, 106, 106, 0.7, im)
            if swordPOS[0] != -1 or sword2XPOS[0] != -1:
                grid[7-i][j] = 0
                continue
            shieldPOS = imagesearcharea("Shield.png", 0, 0, 106, 106, 0.8, im)
            if shieldPOS[0] != -1:
                grid[7-i][j] = 1
                continue
            wandPOS = imagesearcharea("Wand.png", 0, 0, 106, 106, 0.8, im)
            wand2XPOS = imagesearcharea("2xWand.png", 0, 0, 106, 106, 0.8, im)
            if wandPOS[0] != -1 or wand2XPOS[0] != -1:
                grid[7-i][j] = 2
                continue
            keyPOS = imagesearcharea("Key.png", 0, 0, 106, 106, 0.8, im)
            if keyPOS[0] != -1:
                grid[7-i][j] = 3
                continue
            cratePOS = imagesearcharea("Crate.png", 0, 0, 106, 106, 0.8, im)
            if cratePOS[0] != -1:
                grid[7-i][j] = 4
                continue
            brainPOS = imagesearcharea("Brain.png", 0, 0, 106, 106, 0.8, im)
            if brainPOS[0] != -1:
                grid[7-i][j] = 5
                continue
            armPOS = imagesearcharea("Arm.png", 0, 0, 106, 106, 0.8, im)
            if armPOS[0] != -1:
                grid[7-i][j] = 6
                continue
            lightningPOS = imagesearcharea("Lightning.png", 0, 0, 106, 106, 0.8, im)
            if lightningPOS[0] != -1:
                grid[7-i][j] = 7
                continue
            freezePOS = imagesearcharea("Freeze.png", 0, 0, 106, 106, 0.8, im)
            if freezePOS[0] != -1:
                grid[7-i][j] = 7
                continue
            firePOS = imagesearcharea("Fire.png", 0, 0, 106, 106, 0.8, im)
            if firePOS[0] != -1:
                grid[7-i][j] = 7
                continue
            tntPOS = imagesearcharea("tnt.png", 0, 0, 106, 106, 0.8, im)
            if tntPOS[0] != -1:
                grid[7-i][j] = 7
                continue
            shieldSpellPOS = imagesearcharea("shieldSpell.png", 0, 0, 106, 106, 0.8, im)
            if shieldSpellPOS[0] != -1:
                grid[7-i][j] = 7
                continue
            fishPOS = imagesearcharea("fish.png", 0, 0, 106, 106, 0.8, im)
            if fishPOS[0] != -1:
                grid[7-i][j] = 7
                continue
            bowPOS = imagesearcharea("bow.png", 0, 0, 106, 106, 0.8, im)
            if bowPOS[0] != -1:
                grid[i][j] = 7
                continue
            grid[7-i][j] = 8
        startY = startY - 106
    print("From bottom:")
    print(np.matrix(grid))
    return grid

def get_match_from_top(grid):
    #result will be returned with the following format:
    #1st param is 
    result = [[-1, -1],
             [-1, -1],
             [-1, -1]]
    for y in range(8):
        for x in range(6):
            up = False
            left = False
            right = False
            down = False
            posOfMatch = [-1, -1]
        #check for any surrounding matching numbers
            numberToMatch = grid[y][x]
            if numberToMatch == 8:
                continue
            result[0] = [x, y]
            if y != 0:
                up = grid[y-1][x] == numberToMatch
            if x != 0:
                left = grid[y][x-1] == numberToMatch
            if y != 7:
                down = grid[y+1][x] == numberToMatch
            if x != 5:
                right = grid[y][x+1] == numberToMatch

            if numberToMatch == 7:
                result[1] = [x, y]
                result[2] = [x, y]
                return result

            #if we have a match to the right, we need to check the column to the left for matches
            if right and x != 0:
                for i in range(8):
                    if grid[i][x-1] == numberToMatch:
                        posOfMatch = [x-1, i]
                        break
                if posOfMatch != [-1. -1]:
                    result[1] = posOfMatch
                    result[2] = posOfMatch[0],y
                    break
            #if we have a match below, we need to check the row above for matches
            if down and y != 0:
                for i in range(6):
                    if grid[y-1][i] == numberToMatch:
                        posOfMatch = [i, y-1]
                        break
                if posOfMatch != [-1. -1]:
                    result[1] = posOfMatch
                    result[2] = x,posOfMatch[1]
                    break
            #if we have a match to the left, we need to check the column to the right for matches
            if left and x != 5:
                for i in range(8):
                    if grid[i][x+1] == numberToMatch:
                        posOfMatch = [x+1,i]
                        break
                if posOfMatch != [-1. -1]:
                    result[1] = posOfMatch
                    result[2] = posOfMatch[0],y
                    break
            #if we have a match above, we need to check the row below for matches
            if up and y != 7:
                for i in range(6):
                    if grid[y+1][i] == numberToMatch:
                        posOfMatch = [i, y+1]
                        break
                if posOfMatch != [-1. -1]:
                    result[1] = posOfMatch
                    result[2] = x,posOfMatch[1]
                    break
        if result[1] != [-1, -1]:
            return result

def get_match_from_bottom(grid):
    #result will be returned with the following format:
    #1st param is 
    result = [[-1, -1],
             [-1, -1],
             [-1, -1]]
    for i in range(8):
        for j in range(6):
            y = 7-i
            x = 5-j
            up = False
            left = False
            right = False
            down = False
            posOfMatch = [-1, -1]
        #check for any surrounding matching numbers
            numberToMatch = grid[y][x]
            if numberToMatch == 8:
                continue
            result[0] = [x, y]
            if y != 0:
                up = grid[y-1][x] == numberToMatch
            if x != 0:
                left = grid[y][x-1] == numberToMatch
            if y != 7:
                down = grid[y+1][x] == numberToMatch
            if x != 5:
                right = grid[y][x+1] == numberToMatch

            if numberToMatch == 7:
                result[1] = [x, y]
                result[2] = [x, y]
                return result

            #if we have a match to the right, we need to check the column to the left for matches
            if right and x != 0:
                for i in range(8):
                    if grid[i][x-1] == numberToMatch:
                        posOfMatch = [x-1, i]
                        break
                if posOfMatch != [-1. -1]:
                    result[1] = posOfMatch
                    result[2] = [posOfMatch[0],y]
                    break
            #if we have a match below, we need to check the row above for matches
            if down and y != 0:
                for i in range(6):
                    if grid[y-1][i] == numberToMatch:
                        posOfMatch = [i, y-1]
                        break
                if posOfMatch != [-1. -1]:
                    result[1] = posOfMatch
                    result[2] = [x,posOfMatch[1]]
                    break
            #if we have a match to the left, we need to check the column to the right for matches
            if left and x != 5:
                for i in range(8):
                    if grid[i][x+1] == numberToMatch:
                        posOfMatch = [x+1,i]
                        break
                if posOfMatch != [-1. -1]:
                    result[1] = posOfMatch
                    result[2] = [posOfMatch[0],y]
                    break
            #if we have a match above, we need to check the row below for matches
            if up and y != 7:
                for i in range(6):
                    if grid[y+1][i] == numberToMatch:
                        posOfMatch = [i, y+1]
                        break
                if posOfMatch != [-1. -1]:
                    result[1] = posOfMatch
                    result[2] = [x,posOfMatch[1]]
                    break
        if result[1] != [-1, -1]:
            return result

def make_match(result):
    originOfMatch = result[0]
    tileToMove = result[1]
    moveToHere = result[2]
    #print("Moving from {},{} to {},{}".format(tileToMove[0], tileToMove[1], moveToHere[0], moveToHere[1]))
    moveFromX = positions[tileToMove[1]][tileToMove[0]][0]
    moveFromY = positions[tileToMove[1]][tileToMove[0]][1]
    moveToX = positions[moveToHere[1]][moveToHere[0]][0]
    moveToY = positions[moveToHere[1]][moveToHere[0]][1]
    if moveToHere == tileToMove:
        pyautogui.click(moveToX, moveToY)
        time.sleep(0.1)
        pyautogui.moveTo(100,100)
        return
    #print("Move from {},{} to {},{}".format(moveFromX, moveFromY, moveToX, moveToY))
    pyautogui.moveTo(moveFromX,moveFromY)
    if abs((moveToX-moveFromX) + (moveToY-moveFromY)) < 300:
        pyautogui.dragTo(moveToX,moveToY,0.3)
    else:
        pyautogui.dragTo(moveToX,moveToY,0.5)
    time.sleep(0.1)
    pyautogui.moveTo(100,100)

def click_run_again():
    pyautogui.click(700, 1020)
    pyautogui.moveTo(100,100)
    return

#Begin Game loop
while True:
    try:
        currentGrid = build_grid_from_top() if startFromTop else build_grid_from_bottom()
        currentMatch = get_match_from_top(currentGrid) if startFromTop else get_match_from_bottom(currentGrid)
        if currentMatch:
            make_match(currentMatch)
        else:
            click_run_again()
        startFromTop = not startFromTop
        time.sleep(0.5)
    except:
        print("Unexpected error:", sys.exc_info()[0])

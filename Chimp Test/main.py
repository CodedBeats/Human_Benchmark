import time
import cv2 as cv
import numpy as np
import pyautogui


def findNum(imgPath, xSpawn, ySpawn, widthSpawn, heightSpawn, coordsArr): 
    # load img to look for
    template = cv.imread(imgPath, cv.IMREAD_UNCHANGED)

    # capture the screen in the defined region
    image = pyautogui.screenshot(region=(xSpawn, ySpawn, widthSpawn, heightSpawn))
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    # write the image to disk
    cv.imwrite("Chimp Test/imgs/screenshot.png", image)

    # match template image within the screenshot
    result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # threshold to determine if image is found
    threshold = 0.8

    if max_val >= threshold:
        # If the image is found, store the coordinates
        top_left = max_loc

        # mini arr for x,y coords
        xyCoords = [top_left[0] + xSpawn + 25, top_left[1] + ySpawn + 25]
        # add to main arr
        coordsArr.append(xyCoords)

        # Draw a rectangle around the found image
        # cv.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        # Save the screenshot with the found image
        # cv.imwrite("Chimp Test/imgs/found.png", image)

    

def automateRound(spawningNums, xSpawn, ySpawn, widthSpawn, heightSpawn, coordsArr):
    time.sleep(1)

    # find nums
    for i in range(spawningNums):
        imgPath = "Chimp Test/imgs/num" + str(i+1) + "Img.png"
        findNum(imgPath, xSpawn, ySpawn, widthSpawn, heightSpawn, coordsArr)
    
    # click nums
    for i in range(spawningNums):
        pyautogui.click(coordsArr[i][0], coordsArr[i][1])
        time.sleep(0.02)
    
    # clear arr
    coordsArr.clear()


def automate():
    time.sleep(3)
    # spawn dimensions
    xSpawn = 457
    ySpawn = 162
    # dimension
    widthSpawn = 970
    heightSpawn = 520
    # init numbers this round
    spawningNums = 4
    # arr of arrs storing x,y coords
    coordsArr = []

    time.sleep(2)
    for i in range(40):
        automateRound(spawningNums, xSpawn, ySpawn, widthSpawn, heightSpawn, coordsArr)
        spawningNums += 1

        # click continue
        pyautogui.click(950, 550)


automate()

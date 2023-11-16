import time
import cv2 as cv
import numpy as np
import pyautogui

time.sleep(3)

# spaw dimensions
xSpawn = 457
ySpawn = 162
# dimension
widthSpawn = 970
heightSpawn = 520

# Define the path to the image you want to look for
image_path = "Aim Trainer/imgs/Target.png"

# Load the image you want to search for
template = cv.imread(image_path, cv.IMREAD_UNCHANGED)


for i in range(33):
    pyautogui.PAUSE = 0.01
    # Capture the screen in the defined region
    image = pyautogui.screenshot(region=(xSpawn, ySpawn, widthSpawn, heightSpawn))
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    # write the image to disk
    cv.imwrite("Aim Trainer/imgs/screenshot.png", image)

    # Match the template image within the screenshot
    result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # Define a threshold to determine if the image is found
    threshold = 0.8

    if max_val >= threshold:
        # If the image is found, store the coordinates
        top_left = max_loc
        bottom_right = (top_left[0] + 42, top_left[1] + 40)

        # click
        pyautogui.click(x=top_left[0] + xSpawn + 5, y=top_left[1] + ySpawn + 5)
        time.sleep(0.1)


        # Draw a rectangle around the found image
        # cv.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        
        # image2 = pyautogui.screenshot()
        # image2 = cv.cvtColor(np.array(image2), cv.COLOR_RGB2BGR)
        # cv.imwrite("Aim Trainer/imgs/fullScreenshot.png", image2)
        # cv.rectangle(image2, new_top_left, new_bottom_right, (255, 0, 0), 2)

        # Save the screenshot with the found image
        # cv.imwrite("Aim Trainer/imgs/found.png", image)
        # cv.imwrite("Aim Trainer/imgs/found2.png", image2)

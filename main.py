import time
import pyautogui 
from PIL import ImageGrab 


def presskey(key):
    pyautogui.keyDown(key)
    return

''' Here 0 means Black color and 255 means white color '''
def game(data):
    # First Part for White Background
    for i in range(300, 302):
        for j in range(900, 902):
            if data[i, j] < 100:
            # above two line we r taking very tiny range because we just want to chk background color so no need to go for wide number range
                # Above Three line is checking that background is white or black
                for i in range(300, 645):
                    for j in range(564, 670):
                        if data[i, j] > 150:
                            # print("white")
                            presskey("up")
                            return

    # Second Part for Black Background
    for i in range(300, 302):
        for j in range(900, 902):
            if data[i, j] > 100:
                for i in range(300, 645):
                    for j in range(564, 650):
                        if data[i, j] < 150:
                            # print("black")
                            presskey("up")
                            return
    
    return


if __name__ == "__main__":
    print("Game will start in 3 seconds")
    time.sleep(3)

    while True:
        image = ImageGrab.grab().convert('L')
         #convert("L") will conver img to black and white
        ''' Here 0 means Black color and 255 means white color '''
        data = image.load()
        game(data)

        # for i in range(300, 302):
        #     for j in range(900, 902):
                # data[i, j] = 150  #this line shows that show img of 150 number ractangle... between 0(black) and 255(white)

        # for i in range(300, 645):
        #     for j in range(564, 650):
        #         data[i, j] = 50
        # image.show()
        # break

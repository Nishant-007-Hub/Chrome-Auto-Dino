import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    # for i in range(300, 415):
    #     for j in range(410, 563):
    #         if data[i, j] < 100:
    #             return
    #             # hit("down")
    for i in range(300, 302):
        for j in range(900, 902):
            if data[i, j] < 100:
                for i in range(220, 660):
                    for j in range(563, 650):
                        if data[i, j] > 100:
                            hit("up")
                            return
            else:
                break

    for i in range(300, 302):
        for j in range(900, 902):
            if data[i, j] > 100:
                for i in range(220, 660):
                    for j in range(563, 650):
                        if data[i, j] < 100:
                            print("ok")
                            hit("up")
                            return
            else:
                break
    # for i in range(300, 302):
    #     for j in range(900, 902):
    #         if 0 < data[i,j] < 255:
    #             for i in range(200, 600):
    #                 for j in range(563, 650):
    #                     if 0 < data[i,j] < 255:
    #                         hit("up")
    #                         print("oh")
    #                         break
    #                     break
    #                 break
    #             break
    #         break
    #     break

    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))
        '''
        # Draw the rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 650):
                data[i, j] = 0

        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 171

'''
        # for i in range(300, 302):
        #     for j in range(900, 902):
        #         data[i, j] = 0
        # for i in range(270, 650):
        #     for j in range(563, 650):
        #         data[i, j] = 100
        # for i in range(300, 600):
        #     for j in range(563, 650):
        #         data[i, j] = 0
        # for i in range(300, 302):
        #     for j in range(900, 902):
        #         data[i, j] = 175
        # image.show()
        # break

        #         # hit("down")
        #         # return
        # for i in range(300, 415):
        #     for j in range(563, 650):
        #         data[i, j] = 200
        # # for i in range(375, 480):
        # #     for j in range(550, 675):
        # #         data[i, j] = 175
        # # #             # hit("up")

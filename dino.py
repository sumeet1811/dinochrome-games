import pyautogui  # pip install pyautogui


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
'''
        # print(asarray(image))

         #Draw the rectangle for cactus
        for i in range(620, 730):
            for j in range(338,395):
                data[i, j] = 0

        

        image.show()
        break
'''


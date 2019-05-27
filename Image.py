import numpy as np
import cv2
import math
import random
import collections

temp_x = []
temp_y = []
co_3 = []
co_4 = []
h = 0
s = 0
v = 0

def FindHsv(r,g,b):
    global h,s,v
    r_ = r / 255
    g_ = g / 255
    b_ = b / 255
    Cmax = max(r_, g_, b_)
    Cmin = min(r_, g_, b_)
    diff = Cmax - Cmin
    v = Cmax
    if v != 0:
        s = diff / Cmax
    else:
        s = 0
    if diff == 0:
        h = 0
    elif Cmax == r_:
        h = 60 * (((g_ - b_) / diff) % 6)
    elif Cmax == g_:
        h = 60 * ((b_ - r_) / diff + 2)
    elif Cmax == b_:
        h = 60 * ((r_ - g_) / diff + 4)


def getColorList(h,s,v):
    dict = collections.defaultdict(list)

    if h == 0 and s == 0:
        if v == 0:
            return 'black'
        elif v ==1:
            return 'white'
        elif v > 0 and v < 1:
            return 'gray'

    if (h >= 0 and h < 20) or (h > 340 and h < 360):
        if s <= 0.03 and v ==1:
            return 'white'
        if v ==0:
            return 'black'
        else:
            return 'red'
    if h >= 20 and h <50:
        if s <= 0.03 and v ==1:
            return 'white'
        if v ==0:
            return 'black'
        else:
            return 'orange'
    if h >= 50 and h < 70:
        if s <= 0.03 and v ==1:
            return 'white'
        if v ==0:
            return 'black'
        else:
            return 'yellow'
    if h >=70 and h < 170:
        if s <= 0.03 and v ==1:
            return 'white'
        if v ==0:
            return 'black'
        else:
            return 'green'
    if h >=170 and h <210:
        if s <= 0.03 and v ==1:
            return 'white'
        if v ==0:
            return 'black'
        else:
            return 'blue'
    if h >=210 and h < 260:
        if s <= 0.03 and v ==1:
            return 'white'
        if v ==0:
            return 'black'
        else:
            return 'indigo'
    if h >=260 and h <=340:
        if s <= 0.03 and v ==1:
            return 'white'
        if v ==0:
            return 'black'
        else:
            return 'purple'


def distance(x1,x2,y1,y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def main():
    #繪製隨機圖形
    def rectangle(width, high, angle, coordinate,num):
        global temp_x,temp_y,co
        temp_x = []
        temp_y = []
        #print(coordinate)
        #print(angle)
        #print(width)
        if num == 3:
            temp_x.append(coordinate[0])
            temp_y.append(coordinate[1])
            #co_3.append([temp_x[0], temp_y[0]])
            temp_x.append(temp_x[0] + int((width * math.cos(-angle * (math.pi / 180)))))
            temp_y.append(temp_y[0] - int(abs((width * math.sin(-angle * (math.pi / 180))))))
            #co_3.append([temp_x[1], temp_y[1]])
            temp_x.append(temp_x[1] - int(high * math.cos(-(90-angle) * (math.pi / 180))))
            temp_y.append(temp_y[1] - int(abs(high * math.sin(-(90-angle) * (math.pi / 180)))))
            #co_3.append([temp_x[2], temp_y[2]])
            pts = np.array([[temp_x[0], temp_y[0]],
                            [temp_x[1], temp_y[1]],
                            [temp_x[2], temp_y[2]]], np.int32)
            cv2.fillPoly(img, [pts], (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
            co_3.append(pts)
        elif num == 4:
            temp_x.append(coordinate[0])
            temp_y.append(coordinate[1])

            temp_x.append(temp_x[0] + int((width * math.cos(-angle * (math.pi / 180)))))
            temp_y.append(temp_y[0] - int(abs((width * math.sin(-angle * (math.pi / 180))))))

            temp_x.append(temp_x[1] - int(high * math.cos(-(90 - angle) * (math.pi / 180))))
            temp_y.append(temp_y[1] - int(abs(high * math.sin(-(90 - angle) * (math.pi / 180)))))

            temp_x.append(temp_x[2] - int(width * math.cos((-angle) * (math.pi / 180))))
            temp_y.append(temp_y[2] + int(abs(width * math.sin((-angle) * (math.pi / 180)))))

            pts = np.array([[temp_x[0], temp_y[0]],
                            [temp_x[1], temp_y[1]],
                            [temp_x[2], temp_y[2]],
                            [temp_x[3], temp_y[3]]], np.int32)
            cv2.fillPoly(img, [pts], (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
            co_4.append(pts)

    img2 = np.zeros((720, 720, 4), np.uint8)
    img2.fill(0)

    while True:
        co_3 = []
        co_4 = []
        img = np.zeros((720, 720, 4), np.uint8)
        img.fill(0)
        t = 0
        c = []
        for i in range(10):
            rectangle(random.randint(50, 100), random.randint(50, 100), random.randint(0, 90), [random.randint(100, 600), random.randint(100, 600)], 3)
            rectangle(random.randint(50, 100), random.randint(50, 100), random.randint(0, 90), [random.randint(100, 600), random.randint(100, 600)], 4)
        break
    cv2.imwrite('output.png', img)
    cv2.imshow('Image', img)
    cv2.waitKey(0)

    #讀取圖片
    img2 = cv2.imread('output.png')

    #計算有幾種顏色
    color = []
    for i in range(720):
        for j in range(720):
            if img2[i][j][0] != [0] and img2[i][j][1] != [0] and img2[i][j][2] != [0]:
                if [img2[i][j][0],img2[i][j][1],img2[i][j][2]] not in color:
                    color.append([img2[i][j][0],img2[i][j][1],img2[i][j][2]])

    #把每一個顏色寫在另一張畫布進行判斷
    for n in range(len(color)):
        img3 = np.zeros((720, 720, 4), np.uint8)
        img3.fill(0)
        for i in range(720):
            for j in range(720):
                if img2[i][j][0] == color[n][0] and img2[i][j][1] == color[n][1] and img2[i][j][2] == color[n][2]:
                    cv2.line(img3, (j, i), (j, i), (255,0,0), 1)


        gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

        a = 0
        for j in contours:
            cnt = contours[a]
            area = cv2.contourArea(cnt)
            peri = cv2.arcLength(j, True)
            approx = cv2.approxPolyDP(j, 0.02 * peri, True)
            #print(area)
            if len(approx) == 4 or len(approx) == 3:
                if area >= 1840 and area < 10000: #尚未確定如何界定面積範圍
                    cv2.drawContours(img, j, -1, (0, 0, 255), 2)
            a+=1

    cv2.imshow('Image', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
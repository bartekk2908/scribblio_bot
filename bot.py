import numpy as np
from PIL import Image
import pynput
import time

colors_rgbs = {"white": (255, 255, 255),       "black": (0, 0, 0),    "grey_l": (193, 193, 193),   "grey_d": (76, 76, 76),
               "red_l": (239, 19, 11),       "red_d": (116, 11, 7),    "orange_l": (255, 113, 0), "orange_d": (194, 56, 0),
               "yellow_l": (255, 228, 0),    "yellow_d": (232, 162, 0), "green_l": (0, 204, 0),  "green_d": (0, 85, 16),
               "sky_l": (0, 178, 255),       "sky_d": (0, 86, 158),    "blue_l": (35, 31, 211),   "blue_d": (14, 8, 101),
               "purple_l": (163, 0, 186),    "purple_d": (85, 0, 105), "pink_l": (211, 124, 170),   "pink_d": (167, 85, 116),
               "brown_l": (160, 82, 45),     "brown_d": (99, 48, 13)}

colors_coords = {"black": (585, 920),    "grey_l": (610, 895),   "grey_d": (610, 920),
                 "red_l": (635, 895),       "red_d": (635, 920),    "orange_l": (655, 895), "orange_d": (655, 920),
                 "yellow_l": (680, 895),    "yellow_d": (680, 920), "green_l": (705, 895),  "green_d": (705, 920),
                 "sky_l": (730, 895),       "sky_d": (730, 920),    "blue_l": (755, 895),   "blue_d": (755, 920),
                 "purple_l": (780, 895),    "purple_d": (780, 920), "pink_l": (800, 895),   "pink_d": (800, 920),
                 "brown_l": (825, 895),     "brown_d": (825, 920)}

pencil_coord_1 = (870, 905)
pencil_coord_2 = (1085, 905)
pencil_coord_3 = (1135, 905)
pencil_coord_4 = (1190, 905)
dot_coord = (1035, 905)
up_left_cor = (486, 263)
down_right_cor = (1293, 860)

SIZE = (100, 100)

time_s = 0.00005

im = Image.open("test.jpg")
im = im.resize(SIZE)
px = im.load()
# print(im)
# im.show()

n_px_tab = np.empty(SIZE, dtype=object)


for i in range(0, SIZE[1]):
    for j in range(0, SIZE[0]):
        best_color = ""
        best_L = 765
        for key in colors_rgbs:
            L = abs(colors_rgbs[key][0] - px[j, i][0]) + abs(colors_rgbs[key][1] - px[j, i][1]) + abs(colors_rgbs[key][2] - px[j, i][2])
            # L = (colors_rgbs[key][0] - px[j, i][0]) ** 2 + (colors_rgbs[key][1] - px[j, i][1])**2 + (colors_rgbs[key][2] - px[j, i][2])**2
            if L < best_L:
                best_L = L
                best_color = key
        # print(best_color)
        # print(best_L)
        n_px_tab[j, i] = best_color

print(n_px_tab)

mouse = pynput.mouse.Controller()

time.sleep(4)

mouse.position = dot_coord
mouse.click(pynput.mouse.Button.left, 1)
time.sleep(time_s)
mouse.position = pencil_coord_2
mouse.click(pynput.mouse.Button.left, 1)
time.sleep(time_s)
for key in colors_coords:
    mouse.position = colors_coords[key]
    mouse.click(pynput.mouse.Button.left, 1)
    time.sleep(time_s)
    for i in range(0, SIZE[1]):
        for j in range(0, SIZE[0]):
            if n_px_tab[j, i] == key:
                mouse.position = (up_left_cor[0] + abs((down_right_cor[0] - up_left_cor[0]) / SIZE[0] * j), up_left_cor[1] + abs((down_right_cor[1] - up_left_cor[1]) / SIZE[1] * i))
                time.sleep(time_s)
                mouse.click(pynput.mouse.Button.left, 1)

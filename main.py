import argparse
import cv2
import pytesseract

# crop values for the six damage totals for the ship
# values are in relation to the center (top, bottom, left right)
IND_DAMAGES = [[0.362, -0.293, 0.419, -0.282],
               [0.129, -0.075, 0.336, -0.205],
               [-0.091, 0.162, 0.258, -0.127],
               [-0.327, 0.392, 0.181, -0.051],
               [-0.565, 0.614, 0.106, 0.027],
               [-0.786, 0.855, 0.048, 0.102]]

total_calc_dmg, total_ingame_dmg = 0, 0

# set tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# construct argument and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument('-img', required=True, help='path to input image to be OCR\'d')
args = vars(ap.parse_args())
img = cv2.imread(args['img'])

def crop(ty, by, lx, rx):
    center_x, center_y = img.shape[1] / 2, img.shape[0] / 2
    top_y, bottom_y = center_y - img.shape[0] * ty / 2, center_y + img.shape[0] * by / 2
    left_x, right_x = center_x - img.shape[1] * lx / 2, center_x + img.shape[1] * rx / 2
    return img[int(top_y):int(bottom_y), int(left_x):int(right_x)]

def process(val, bool):
    global total_calc_dmg, total_ingame_dmg
    # crop image to isolate specific number
    cropped_num = crop(*val)
    # grayscale and threshold
    gray = cv2.cvtColor(cropped_num, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)[1]
    # morph open
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    # text extraction, convert to int
    converted = int(''.join(filter(str.isdigit, pytesseract.image_to_string(opening, config='--psm 6'))) or 0)
    if bool: total_calc_dmg += converted
    else: total_ingame_dmg = converted

# process individual ship damage totals
for crop_val_arr in IND_DAMAGES: process(crop_val_arr, True)
# process in-game damage total
process([0.59, -0.46, 0.71 , -0.47], False)

if total_calc_dmg > 0:
    print('Image: ', args['img'].split('\\')[-1])
    print('============ANALYSIS============')
    print('TOTAL DAMAGE:\t\t', total_ingame_dmg)
    print('CALCULATED DAMAGE:\t', total_calc_dmg)
    print('DIFFERENCE:\t\t', total_ingame_dmg - total_calc_dmg)
    print('================================')
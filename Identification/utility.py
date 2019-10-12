import logicchecker as lg
import math
import cv2

uni_range = [0.33312159941979147, 0.6528219512240684]  # List contains the spatial range for unicycles
# List of global range for bicycles
w1_w2_range = [0.4545536661228686, 0.6335231719118755]
w1_s_range = [0.19592735476362458, 0.6765103385064127]
w2_s_range = [0.2882471504682855, 0.7786016942582378]

'''Function to compute the euclidean distance between
two wheels and the seat
Input : directory and image filename
Output : True if spatial constraints match False otherwise
Comment : Directory should have a xml file with the same name as '''


def compute_spatial_uni(directory, filename):
    filename_img = directory + "/" + filename
    height, width, channels = cv2.imread(filename_img).shape
    # Extract the coordinates of the wheel and seat position
    coord_w, coord_s = lg.parse_xml(directory + "/" + filename.split(".")[0] + ".xml")
    if len(coord_w) == len(coord_s):
        for i in range(len(coord_w)):
            if len(coord_w[i]) != 0 and len(coord_s[i]) != 0:
                x_mid_w = (float(coord_w[i][0]) + float(coord_w[i][2])) / 2
                y_mid_w = (float(coord_w[i][1]) + float(coord_w[i][3])) / 2
                x_mid_s = (float(coord_s[i][0]) + float(coord_s[i][2])) / 2
                y_mid_s = (float(coord_s[i][3]) + float(coord_s[i][1])) / 2
                distance = math.sqrt(((x_mid_w - x_mid_s) / width) ** 2 + ((y_mid_w - y_mid_s) / height) ** 2)
                # print(i, coord_w[i], coord_s[i])
                if uni_range[0] <= distance <= uni_range[1]:
                    return True
    return False


'''Function to compute the euclidean distance between
two wheels and the seat
Input : directory and image filename
Output : True if spatial constraints match False otherwise
Comment : Directory should have a xml file with the same name as '''


def compute_spatial_bi(directory, filename):
    filename_img = directory + "/" + filename
    height, width, channels = cv2.imread(filename_img).shape
    # Extract the coordinates of the wheel and seat position
    coord_w, coord_s = lg.parse_xml(directory + "/" + filename.split(".")[0] + ".xml")
    if len(coord_w) == 2 and len(coord_s) == 1:
        x_mid_w1 = (float(coord_w[0][0]) + float(coord_w[0][2])) / 2
        x_mid_w2 = (float(coord_w[1][0]) + float(coord_w[1][2])) / 2
        y_mid_w1 = (float(coord_w[0][1]) + float(coord_w[0][3])) / 2
        y_mid_w2 = (float(coord_w[1][1]) + float(coord_w[1][3])) / 2
        x_mid_s = (float(coord_s[0][0]) + float(coord_s[0][2])) / 2
        y_mid_s = (float(coord_s[0][1]) + float(coord_s[0][3])) / 2
        # Calculate the euclidean distance between wheel1 wheel2 and seat
        w1_w2_dist = math.sqrt(((x_mid_w1 - x_mid_w2) / width) ** 2 + ((y_mid_w1 - y_mid_w2) / height) ** 2)
        w1_s_dist = math.sqrt(((x_mid_w1 - x_mid_s) / width) ** 2 + ((y_mid_w1 - y_mid_s) / height) ** 2)
        w2_s_dist = math.sqrt(((x_mid_w2 - x_mid_s) / width) ** 2 + ((y_mid_w2 - y_mid_s) / height) ** 2)
        print(w1_w2_dist, w1_s_dist, w2_s_dist)
        # Check
        if w1_w2_range[0] <= w1_w2_dist <= w1_w2_range[1] and w1_s_range[0] <= w1_s_dist <= w1_s_range[1] and \
                w2_s_range[0] <= w2_s_dist <= w2_s_range[1]:
            return True
    return False

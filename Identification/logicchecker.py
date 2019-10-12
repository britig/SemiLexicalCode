import matplotlib.pyplot as plt
import cv2
import xml.etree.ElementTree as ET
# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries

'''Function to check if image is of unicycle'''
'''Input : filename path'''
'''Output : True or False'''


def check_unicycle(directory, filename):
    epsilon = 30
    filename_img = directory + "/" + filename
    # Extract the coordinates of the wheel and seat position
    coord_w, coord_s = parse_xml(directory + "/" + filename.split(".")[0] + ".xml")
    # Checks if the spatial locations are correct
    result = check_spatial_uni(coord_w, coord_s)
    # If number of wheels are equal to number of seats
    '''if len(coord_w) == len(coord_s):
        for i in range(len(coord_w)):
            if len(coord_w[i]) != 0 and len(coord_s[i]) != 0:
                x_min = coord_w[i][0]
                y_max = (int(coord_w[i][3]) + int(coord_w[i][1])) / 2
                x_max = coord_w[i][2]
                y_min = coord_s[i][3]
                x_mid = (int(x_max) + int(x_min)) / 2
                img = crop(int(x_mid), int(y_min), int(y_max), filename_img, epsilon)
    segments = slic(img, n_segments=10, sigma=5)
    print(segments.shape)
    plt.imshow(mark_boundaries(img, segments))
    # show the output of SLIC
    edges = cv2.Canny(img, 450, 450)
    plt.imshow(edges)
    plt.show()

    plt.imshow(edges, cmap='gray')
    plt.show()
    #val = check_connection(img)'''
    return result


def check_spatial_uni(coord_w, coord_s):
    pass


def check_connection(img):
    edges = edge_detection(img)
    pass


def edge_detection(img):
    edges = cv2.Canny(img, 400, 400)
    # plt.imshow(edges, cmap='gray')
    # plt.show()
    return edges


'''Function to extract the component positions from XML'''
'''Input : xmlfile path'''
'''Output : returns list of x_min, y_min, x_max, y_max for wheel and seat'''


def parse_xml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    list_wheel = []
    list_seat = []
    countW = 0
    countS = 0
    # iterate news items
    for object in root.findall('object'):
        name = object.find('name').text
        if name == "wheel":
            list_wheel.append([])
            list_wheel[countW].append(object.find('bndbox').find('xmin').text)
            list_wheel[countW].append(object.find('bndbox').find('ymin').text)
            list_wheel[countW].append(object.find('bndbox').find('xmax').text)
            list_wheel[countW].append(object.find('bndbox').find('ymax').text)
            countW = countW + 1
        elif name == "seat":
            list_seat.append([])
            list_seat[countS].append(object.find('bndbox').find('xmin').text)
            list_seat[countS].append(object.find('bndbox').find('ymin').text)
            list_seat[countS].append(object.find('bndbox').find('xmax').text)
            list_seat[countS].append(object.find('bndbox').find('ymax').text)
            countS = countS + 1
    return list_wheel, list_seat


'''Function to Crop image '''
'''returns cropped image'''


def crop(x_mid, y_min, y_max, filename, epsilon):
    img = cv2.imread(filename)
    print(x_mid, y_min, y_max)
    crop_img = img[y_min:y_max, x_mid - 15:x_mid + epsilon]
    plt.imshow(img)
    plt.show()
    return crop_img

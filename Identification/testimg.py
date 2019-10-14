import cv2
from darkflow.net.build import TFNet
import os
import xml.etree.ElementTree as ET


def run_yolo():
    options = {
        'model': '../cfg/tiny-yolo-voc-3c.cfg',
        'load': 1200,
        'threshold': 0.1,
    }
    tfnet = TFNet(options)

    for i, file1 in enumerate(os.listdir("../testimg/actual")):
        file1 = "../testimg/actual/" + file1
        img = cv2.imread(file1, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        str1 = 'img{:04}.jpg'.format(i + 1)

        root = ET.Element("annotation")
        ET.SubElement(root, "folder").text = "testimg/actual"
        ET.SubElement(root, "file").text = str1
        ET.SubElement(root, "segmented").text = "0"
        doc1 = ET.SubElement(root, "size")
        ET.SubElement(doc1, "width").text = str(img.shape[1])
        ET.SubElement(doc1, "height").text = str(img.shape[0])
        ET.SubElement(doc1, "depth").text = str(img.shape[2])

        result = tfnet.return_predict(img)
        for j in range(len(result)):
            if result[j]['confidence'] >= 0.4:
                tl = (result[j]['topleft']['x'], result[j]['topleft']['y'])
                br = (result[j]['bottomright']['x'], result[j]['bottomright']['y'])
                label = result[j]['label']
                img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
                img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                doc2 = ET.SubElement(root, "object")
                ET.SubElement(doc2, "name").text = label
                ET.SubElement(doc2, "pose").text = "Unspecified"
                ET.SubElement(doc2, "truncated").text = "0"
                ET.SubElement(doc1, "difficult").text = "0"
                doc3 = ET.SubElement(doc2, "bndbox")
                ET.SubElement(doc3, "xmin").text = str(result[j]['topleft']['x'])
                ET.SubElement(doc3, "ymin").text = str(result[j]['topleft']['y'])
                ET.SubElement(doc3, "xmax").text = str(result[j]['bottomright']['x'])
                ET.SubElement(doc3, "ymax").text = str(result[j]['bottomright']['y'])

        tree = ET.ElementTree(root)
        tree.write('../testimg/modified/img{:04}.xml'.format(i + 1))

        str1 = '../testimg/modified/' + str1
        cv2.imwrite(str1, img)

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import xml.etree.ElementTree as ET
import xml.dom.minidom as xdm
import sys



xml_path = '/media/lz/DATA1/EastGate/part2/labels_ori/sequence_59/'
img_path = '/media/lz/DATA1/EastGate/part2/sequences/sequence_59/'
txt_path = '/media/lz/DATA1/EastGate/part2/annotations'

f = open(os.path.join(txt_path, 'sequence_59.txt'), 'a')

xml_list = os.listdir(xml_path)

class_num = {'person': '1', 'car': '2', 'non-vehicle': '3'}

for xml_file in xml_list:

    with open(os.path.join(xml_path, xml_file), 'r', encoding='gbk') as fh:
        dom = xdm.parse(fh)
        root = dom.documentElement

        imgname = root.getElementsByTagName('filename')

        filename = imgname[0].firstChild.data

        print(xml_file.strip('.xml'))


        # f.write(os.path.join(img_path, filename))

        box_node = root.getElementsByTagName('name') #object_categoty
        target_id = root.getElementsByTagName('id')  #target_id

        box_len = len(box_node)

        xmin_node = root.getElementsByTagName('xmin')
        ymin_node = root.getElementsByTagName('ymin')
        xmax_node = root.getElementsByTagName('xmax')
        ymax_node = root.getElementsByTagName('ymax')
        print(box_len)

        for i in range(box_len):
            name_txt = box_node[i].firstChild.data
            target_id_txt = target_id[i].firstChild.data
            xmin_txt = xmin_node[i].firstChild.data
            xmax_txt = xmax_node[i].firstChild.data
            ymin_txt = ymin_node[i].firstChild.data
            ymax_txt = ymax_node[i].firstChild.data


            f.write(xml_file.strip('.xml')) #frame_idx
            f.write(',')
            f.write(target_id_txt)  # target_id
            f.write(',')
            f.write(xmin_txt)
            f.write(',')
            f.write(ymin_txt)
            f.write(',')
            f.write(str(int(xmax_txt)-int(xmin_txt)))
            f.write(',')
            f.write(str(int(ymax_txt)-int(ymin_txt)))
            f.write(',')
            f.write('1') # confidence score
            f.write(',')
            f.write(class_num[name_txt]) #object category
            f.write(',')
            f.write('0') # truncation ratio
            f.write(',')
            f.write('0') # occlusion ratio
            if i < box_len-1:
                f.write('\n')


    f.write('\n')

f.close()
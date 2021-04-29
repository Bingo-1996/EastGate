

# 将a替换成b

import os

xmldir = '/media/lz/DATA1/EastGate/labels_ori/sequence_51'
savedir = '/media/lz/DATA1/EastGate/wo_path'
xmllist = os.listdir('/media/lz/DATA1/EastGate/labels_ori/sequence_51')
for xml in xmllist:
    if '.xml' in xml:
        fo = open(savedir + '/' + 'new_{}'.format(xml), 'w', encoding='gbk')  # 不要new前缀可以在这改
        print('{}'.format(xml))
        fi = open(xmldir + '/' + '{}'.format(xml), 'r', encoding='gbk')
        content = fi.readlines()
        for line in content:
            line = line.replace('D:\\报告&论文\\组会报告\\流量\\148东门外路口球1F0EED58_1618562181_51\\', '')  # 例：将a替换为b
            fo.write(line)
        fo.close()
        print('替换成功')

# 如通b为空字符串，就是删除


# # coding=utf-8
# import os
# import os.path
# import xml.dom.minidom
#
# # 获得文件夹中所有文件
# FindPath = '/media/lz/DATA1/EastGate/labels_ori/sequence_51/'
# # 获取文件夹下全部文件
# FileNames = os.listdir(FindPath)
# s = []
# # 存储路径
# xml_path = '/media/lz/DATA1/EastGate/labels_ori/sequence_51/'
# for file_name in FileNames:
#     if not os.path.isdir(file_name):  # 判断是否是文件夹,不是文件夹才打开
#         print(file_name)
#
#
#     # 读取xml文件
#     dom = xml.dom.minidom.parse(os.path.join(FindPath, file_name))
#
#     root = dom.documentElement
#
#     # 获取标签对path之间的值，可以修改其他标签名如name
#     name = root.getElementsByTagName('path')
#     # print(len(name))
#     for i in range(len(name)):
#         # if name[i] .firstChild.data== 'screw cap':
#         # 切片拼接新名字地址
#         name[i].firstChild.data = "\home\ssd_object-1\\" + name[i].firstChild.data[3:]
#         print('修改后的 path')
#         print(name[i].firstChild.data)
#     # 将修改后的xml文件保存
#     print(xml_path, file_name)
#     with open(os.path.join(xml_path, file_name), 'w') as fh:
#         dom.writexml(fh)
#         print('写入name/pose OK!')
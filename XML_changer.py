import xml.dom.minidom
import os

path = r'D:\code\Car_project\dataset\label'  # xml文件存放路径
sv_path = r'D:\code\Car_project\dataset\label'  # 修改后的xml文件存放路径
files = os.listdir(path)


for xmlFile in files:
    dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 打开xml文件，送到dom解析
    root = dom.documentElement  # 得到文档元素对象
    item = root.getElementsByTagName('path')  # 获取path这一node名字及相关属性值
    a,b=os.path.splitext(xmlFile) #分离出文件名a
    for i in item:
        i.firstChild.data = f'D:\code\Car_project\dataset\data' '\\' + a + '.jpg'     # xml文件对应的图片路径

    with open(os.path.join(sv_path, xmlFile), 'w', encoding='utf-8') as fh:
        dom.writexml(fh)


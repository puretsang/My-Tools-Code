import re

import chardet
import os
import zipfile
from phone import Phone, write2file
from collections import Counter

cantonese_no = []
beijing_no = []
shanghai_no = []
jiangxi_no = []
jiangsu_no = []
shandong_no = []
sichuan_no = []
chongqing_no = []
zhejiang_no = []
hunan_no = []
hubei_no = []
henan_no = []
hebei_no = []
tianjin_no = []
heilongjiang_no = []
jilin_no = []
liaoning_no = []
neimenggu_no = []
xinjiang_no = []
xizang_no = []
qinghai_no = []
guangxi_no = []
hainan_no = []
fujian_no = []
yunnan_no = []
ningxia_no = []
shanxi_no = []
shanc_no = []
guizhou_no = []
virtual_no = []
p = Phone()


def execute_file(file_path):
    # 实例化
    numbers = []
    # with open(file_path, 'rb') as f:
    #     text = f.read()
    #     print(text)
    #     type = chardet.detect(text)
    #     charenc = type['encoding']
    #     print('charenc---> ', charenc)
    #     for line in f:
    #         a = re.findall('(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', line)
    #         for i in range(len(a)):
    #             numbers.append(a[i].strip("\n"))
    try:
        file_text = open(file_path, mode='rb').read()
        print('file_text ---> ', file_text)
        a = re.findall('(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', str(file_text))
        for i in range(len(a)):
            numbers.append(a[i].strip("\n"))
    except Exception as e:
        print(e)
        return False
    # 去重
    numbers2 = sorted(set(numbers), key=numbers.index)
    if len(numbers2) == 0:
        return False
    print('len ---> ', len(numbers2))
    for _no in numbers2:
        info = p.find(_no)
        if info.get('phone_type') > 3:
            virtual_no.append(info.get('phone'))
        else:
            if info.get('province') == '广东':

                cantonese_no.append(info)
            elif info.get('province') == '北京':
                beijing_no.append(info)
            elif info.get('province') == '江西':
                jiangxi_no.append(info)
            elif info.get('province') == '江苏':
                jiangsu_no.append(info)
            elif info.get('province') == '山东':
                shandong_no.append(info)
            elif info.get('province') == '浙江':
                zhejiang_no.append(info)
            elif info.get('province') == '广西':
                guangxi_no.append(info)
            elif info.get('province') == '海南':
                hainan_no.append(info)
            elif info.get('province') == '青海':
                qinghai_no.append(info)
            elif info.get('province') == '西藏':
                xizang_no.append(info)
            elif info.get('province') == '新疆':
                xinjiang_no.append(info)
            elif info.get('province') == '四川':
                sichuan_no.append(info)
            elif info.get('province') == '重庆':
                chongqing_no.append(info)
            elif info.get('province') == '山西':
                shanxi_no.append(info)
            elif info.get('province') == '陕西':
                shanc_no.append(info)
            elif info.get('province') == '海南':
                hainan_no.append(info)
            elif info.get('province') == '宁夏':
                ningxia_no.append(info)
            elif info.get('province') == '天津':
                tianjin_no.append(info)
            elif info.get('province') == '北京':
                beijing_no.append(info)
            elif info.get('province') == '内蒙古':
                neimenggu_no.append(info)
            elif info.get('province') == '辽宁':
                liaoning_no.append(info)
            elif info.get('province') == '上海':
                shanghai_no.append(info)
            elif info.get('province') == '黑龙江':
                heilongjiang_no.append(info)
            elif info.get('province') == '吉林':
                jilin_no.append(info)
            elif info.get('province') == '贵州':
                guizhou_no.append(info)
            elif info.get('province') == '云南':
                yunnan_no.append(info)
            elif info.get('province') == '福建':
                fujian_no.append(info)
            elif info.get('province') == '湖南':
                hunan_no.append(info)
            elif info.get('province') == '湖北':
                hubei_no.append(info)
            elif info.get('province') == '河南':
                henan_no.append(info)
            elif info.get('province') == '河北':
                hebei_no.append(info)

    if len(beijing_no) > 0:
        write2file('北京', beijing_no)

    if len(shanghai_no) > 0:
        write2file('上海', shanghai_no)

    if len(tianjin_no) > 0:
        write2file('天津', tianjin_no)

    if len(cantonese_no) > 0:
        write2file('广东', cantonese_no)

    if len(guangxi_no) > 0:
        write2file('广西', guangxi_no)

    if len(fujian_no) > 0:
        write2file('福建', fujian_no)

    if len(zhejiang_no) > 0:
        write2file('浙江', zhejiang_no)

    if len(jiangsu_no) > 0:
        write2file('江苏', jiangsu_no)

    if len(shandong_no) > 0:
        write2file('山东', shandong_no)

    if len(liaoning_no) > 0:
        write2file('辽宁', liaoning_no)

    if len(jilin_no) > 0:
        write2file('吉林', jilin_no)

    if len(heilongjiang_no) > 0:
        write2file('黑龙江', heilongjiang_no)

    if len(neimenggu_no) > 0:
        write2file('内蒙古', neimenggu_no)

    if len(shanxi_no) > 0:
        write2file('山西', shanxi_no)

    if len(shanc_no) > 0:
        write2file('陕西', shanc_no)

    if len(qinghai_no) > 0:
        write2file('青海', qinghai_no)

    if len(xinjiang_no) > 0:
        write2file('新疆', xinjiang_no)

    if len(xizang_no) > 0:
        write2file('西藏', xizang_no)

    if len(yunnan_no) > 0:
        write2file('云南', yunnan_no)

    if len(sichuan_no) > 0:
        write2file('四川', sichuan_no)

    if len(chongqing_no) > 0:
        write2file('重庆', chongqing_no)

    if len(hunan_no) > 0:
        write2file('湖南', hunan_no)

    if len(hubei_no) > 0:
        write2file('湖北', hubei_no)

    if len(guizhou_no) > 0:
        write2file('贵州', guizhou_no)

    if len(henan_no) > 0:
        write2file('河南', henan_no)

    if len(hebei_no) > 0:
        write2file('河北', hebei_no)

    if len(hainan_no) > 0:
        write2file('海南', hainan_no)

    if len(jiangxi_no) > 0:
        write2file('江西', jiangxi_no)

    if len(ningxia_no) > 0:
        write2file('宁夏', ningxia_no)

    return True


# 测试
# execute_file(r'D:/PycharmProjects/My-Tools-Code/Python/phone/fan.txt')


def make_zip():
    source_dir = '../phone/number'
    output_filename = 'C:/Users/admin/Desktop/haoma-mofang.zip'
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
            zipf.write(pathfile, arcname)
    zipf.close()

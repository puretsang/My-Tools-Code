from urllib3.connectionpool import xrange

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

# 实例化
p = Phone()
numbers = []
with open('/Users/duncan/pycharmprojects/My-Tools-Code/Python/phone/numbers.txt', 'r') as f:
    for line in f:
        numbers.append(line.strip("\n"))
numbers2 = sorted(set(numbers), key=numbers.index)

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

pass

# print('北京\n', beijing_no)
# print('天津\n', tianjin_no)
# print('上海\n', shanghai_no)
# print('广东\n', cantonese_no)
# print('广西\n', guangxi_no)
# print('福建\n', fujian_no)
# print('浙江\n', zhejiang_no)
# print('江苏\n', jiangsu_no)
# print('山东\n', shandong_no)
# print('辽宁\n', liaoning_no)
# print('吉林\n', jilin_no)
# print('黑龙江\n', heilongjiang_no)
# print('内蒙古\n', neimenggu_no)
# print('山西\n', shanxi_no)
# print('陕西\n', shanc_no)
# print('青海\n', qinghai_no)
# print('新疆\n', xinjiang_no)
# print('西藏\n', xizang_no)
# print('云南\n', yunnan_no)
# print('四川\n', sichuan_no)
# print('重庆\n', chongqing_no)
# print('湖北\n', hubei_no)
# print('湖南\n', hunan_no)
# print('贵州\n', guizhou_no)
# print('海南\n', hainan_no)
# print('江西\n', jiangxi_no)
# print('宁夏\n', ningxia_no)

file_path = '../phone/number/'

if len(beijing_no) > 0:
    file = open(file_path + '北京.txt', 'w')
    write2file(file, beijing_no)

if len(shanghai_no) > 0:
    file = open(file_path + '上海.txt', 'w')
    write2file(file, shanghai_no)

if len(tianjin_no) > 0:
    file = open(file_path + '天津.txt', 'w')
    write2file(file, tianjin_no)

if len(cantonese_no) > 0:
    file = open(file_path + '广东.txt', 'w')
    write2file(file, cantonese_no)

if len(guangxi_no) > 0:
    file = open(file_path + '广西.txt', 'w')
    write2file(file, guangxi_no)

if len(fujian_no) > 0:
    file = open(file_path + '福建.txt', 'w')
    write2file(file, fujian_no)

if len(zhejiang_no) > 0:
    file = open(file_path + '浙江.txt', 'w')
    write2file(file, zhejiang_no)

if len(jiangsu_no) > 0:
    file = open(file_path + '江苏.txt', 'w')
    write2file(file, jiangsu_no)

if len(shandong_no) > 0:
    file = open(file_path + '山东.txt', 'w')
    write2file(file, shandong_no)

if len(liaoning_no) > 0:
    file = open(file_path + '辽宁.txt', 'w')
    write2file(file, liaoning_no)

if len(jilin_no) > 0:
    file = open(file_path + '吉林.txt', 'w')
    write2file(file, jilin_no)

if len(heilongjiang_no) > 0:
    file = open(file_path + '黑龙江.txt', 'w')
    write2file(file, heilongjiang_no)

if len(neimenggu_no) > 0:
    file = open(file_path + '内蒙古.txt', 'w')
    write2file(file, neimenggu_no)

if len(shanxi_no) > 0:
    file = open(file_path + '山西.txt', 'w')
    write2file(file, shanxi_no)

if len(shanc_no) > 0:
    file = open(file_path + '陕西.txt', 'w')
    write2file(file, shanc_no)

if len(qinghai_no) > 0:
    file = open(file_path + '青海.txt', 'w')
    write2file(file, qinghai_no)

if len(xinjiang_no) > 0:
    file = open(file_path + '新疆.txt', 'w')
    write2file(file, xinjiang_no)

if len(xizang_no) > 0:
    file = open(file_path + '西藏.txt', 'w')
    write2file(file, xizang_no)

if len(yunnan_no) > 0:
    file = open(file_path + '云南.txt', 'w')
    write2file(file, yunnan_no)

if len(sichuan_no) > 0:
    file = open(file_path + '四川.txt', 'w')
    write2file(file, sichuan_no)

if len(chongqing_no) > 0:
    file = open(file_path + '重庆.txt', 'w')
    write2file(file, chongqing_no)

if len(hunan_no) > 0:
    file = open(file_path + '湖南.txt', 'w')
    write2file(file, hunan_no)

if len(hubei_no) > 0:
    file = open(file_path + '湖北.txt', 'w')
    write2file(file, hubei_no)

if len(guizhou_no) > 0:
    file = open(file_path + '贵州.txt', 'w')
    write2file(file, guizhou_no)

if len(henan_no) > 0:
    file = open(file_path + '河南.txt', 'w')
    write2file(file, henan_no)

if len(hebei_no) > 0:
    file = open(file_path + '河北.txt', 'w')
    write2file(file, hebei_no)

if len(hainan_no) > 0:
    file = open(file_path + '海南.txt', 'w')
    write2file(file, hainan_no)

if len(jiangxi_no) > 0:
    file = open(file_path + '江西.txt', 'w')
    write2file(file, jiangxi_no)

if len(ningxia_no) > 0:
    file = open(file_path + '宁夏.txt', 'w')
    write2file(file, ningxia_no)



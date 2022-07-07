# # 作業:建立(1050706.csv)此資料中所有的姓氏人口數(不分性別)的總排行

# import csv
# with open("10706.csv", "r", encoding="utf-8") as fp:
#     csv_reader = csv.reader(fp)
#     data = list(csv_reader)
# l=[]
# for row in data:
#     for x in row[2]:
#         l.append(x)
# a=set(l)
# b=list(a)
# print(b)
# ['沙', '幸', '朱', '黄', '謝', '藍', '康', '羅', '兵', '巴', '易', '姜', '王', '武', '周', '廖', '薛', '紀', '氏', '粘', '賴', '溫', '章', '馬', '袁', '宗', '步', '洪', '麥', '蘇', '司', '甘', '葉', '買', '黃', '程', '柯', '盧', '谷', '汪', '鍾', '楊', '簡', '嚴', '彭', '黎', '胡', '馮', '温', '田', '顏', '邵', '梁', '錢', '風', '俞', '徐', '凃', '鐘', '唐', '史', '官', '郭', '林', '蕭', '范', '華', '柳', '才', '留', '湯', '戴', '曾', '毛', '雷', '
# 丁', '辛', '游', '余', '鄭', '邱', '包', '饒', '許', '方', '巫', '卓', '涂', '葛', '侯', '劉', '李', '白', '安', '高', '杜', '阮', '張', '金', '呂', '
# 夏', '龔', '莊', '曹', '董', '宋', '姓', '魏', '力', '潘', '傅', '姚', '趙', '蔡', '孫', '施', '松', '江', '童', '鄧', '石', '何', '歐', '全', '連', '
# 翁', '伍', '沈', '古', '詹', '蔣', '凌', '尤', '陳', '穆', '豊', '吳', '陸']
# import csv
# with open("10706.csv", "r", encoding="utf-8") as fp:
#     csv_reader = csv.reader(fp)
#     data = list(csv_reader)
# list=[]
# sum=0
# for row in data:
#     if "章" in row[2]:
#         x=int(row[4])
#         list.append(x)
# for y in list:
#     sum=sum+y
# sum=str(sum)
# with open("chen.txt", "a" ,encoding="utf-8") as fp:
#     a=fp.write("章"+ "," +sum+"\n")
# list=[]
with open("chen.txt", "r" ,encoding="utf-8") as fp:
    a=fp.readlines()
for line in a[1:]:
    a,c= line.split(",")
    a,c= 
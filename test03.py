with open("data.csv", "r", encoding="Utf-8") as fp:
    data=fp.readlines() #read 全部讀出來變成一個字串 #readline只讀一行，變成字串 #readlines全部讀取，變成串列，每列一個項目
# print(data) #['name,height,weight\n', 'Amy,159,50\n', 'Wendy,180,60\n', 'John,188,70\n', 'Mary,158,61\n', 'Candy,163,58']
for line in data[1:]:
    name,h,w = line.split(",")
    # print(name,h,w) #Amy 159 50
                   #...
    h=int(h)
    w=int(w.strip()) #去掉\n，可將前後符號移除
    bmi=round(w/((h/100)**2),2) #round四捨五入取小數點兩位。
    print("{}'Bmi is {} ".format(name,bmi))
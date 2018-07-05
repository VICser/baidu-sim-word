import csv
import jieba
jieba.load_userdict("user_dic.txt")
f = open("data.txt","a",encoding="utf-8")
def fenci_count():
    word_num = {}
    for i in csv.reader(open('1queryWithCount.csv',mode='r',encoding='utf-8')):
        lst = list(jieba.cut(i[0].strip()))
        #print(lst)
        for j in lst:
            if j not in word_num.keys():
                word_num[j] = int(i[1])
            else:
                num_num = word_num[j] + int(i[1])
                word_num[j] = num_num
        print(word_num)
        #print(word_lst)
    for item in word_num.keys():
        f.write(item)
        f.write(",")
        f.write(str(word_num[item]))
        f.write("\n")
    f.close()

fenci_count()
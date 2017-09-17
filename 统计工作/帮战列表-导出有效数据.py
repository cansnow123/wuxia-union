import re

File_list = ["1.txt", "2.txt", "3.txt", "4.txt"]
Sub_1, Sub_2, Sub_3, Sub_4 = [], [], [], []
Sub_list = [Sub_1, Sub_2, Sub_3, Sub_4]


def convert(raw_line):
    # 删除行首数字
    s1 = re.sub("^\d+ ", "", raw_line)
    # 删除全部0战绩
    s2 = re.sub("^.*\s0 0 0", "", s1)
    # 删除职业
    s3 = re.sub(" 天香| 太白| 五毒| 神威| 真武| 丐帮| 唐门| 神刀", "", s2)
    # 删除空行
    s4 = re.sub("\s*$", "", s3)
    # 空格换成制表符
    s5 = re.sub(" ", "	", s4)
    # 最终保留数据依次为 ID、荣誉数、击杀、助攻
    return s5.split("	")


for x in [0, 1, 2, 3]:
    with open(File_list[x], 'r', encoding='utf-8') as Pre:
            for i in Pre.readlines():
                if convert(i) != [""]:
                    Sub_list[x].append(convert(i))
                else:
                    pass



print(Sub_1)
Sub_1.sort(key=lambda xx: xx[0][0], reverse=True)
print(Sub_1)
# class MemberWarScore(object):
#
#     def __init__(self, member_id, honor, kill, ass):
#         self.member_id = member_id
#         self.honor = honor
#         self.kill = kill
#         self.ass = ass
#
#     def print_score(self):
#         print(self.member_id, self.honor, self.kill, self.ass)

from xlrd import *
import os
import datetime
wb = open_workbook('a.xlsx')
sh1 = wb.sheet_by_name('逐梦-箱子')
sh2 = wb.sheet_by_name('如梦-箱子')
sh3 = wb.sheet_by_name('若梦-箱子')
sh4 = wb.sheet_by_name('何梦-箱子')


# CONVERT EXCEL SHEET TO ARR
def sh2arr(sh):
    temp = []
    for row in range(86):
        values = []
        for col in range(7):
            if row == 0:
                pass
            elif (row > 0) and (col == 5):
                if sh.cell(row, col).value < 1:
                    values.append(sh.cell(row, col).value)
                else:
                    values.append(int(sh.cell(row, col).value))
            else:
                values.append(sh.cell(row, col).value)
        if not values:
            pass
        else:
            temp.append(values)
    return temp

Union_D = [sh2arr(sh1), sh2arr(sh2), sh2arr(sh3), sh2arr(sh4)]

fExcel = "Excel.txt"
JLFile = ["BangPai_DKPFaFangJiLi_G.txt", "BangPai_DKPFaFangJiLi_S.txt"]
UNIONL = []
ignore_list = ["小雪妖", "池小晚", "潇洒仗剑天下", "墨韵玄风", "搞事girl", "顾寻影", "影子月华",
               "友善的狼叔", "冷晓汐灬", "丿几度度丶", "小花狼", "南邦佳人呀", "a逼c迪e诶扶鸡"]
with open(fExcel, 'w', encoding='utf-8') as FFF:
    for bangpai in Union_D:
        for mem_row in bangpai:
            for cell in mem_row:
                # 对应EXCEL中每一行 "	"为制表符
                FFF.write(str(cell)+"	")
            FFF.write("\n")

sample = "发放激励\n领取情况        	帮众                      	等级              	职位                  	剩余PVP-DKP       	" \
         "修改PVP-DKP       	剩余PVE-DKP       	修改PVE-DKP       	发放数量        \n"

# 激励箱子发放文件初始化
with open(JLFile[0], 'w', encoding='utf-8') as initf_g, open(JLFile[1], 'w', encoding='utf-8') as initf_s:
    initf_g.write(sample)
    initf_s.write(sample)
# 加载文件，将EXCEL格式内容转换为数组格式
with open(fExcel, 'r', encoding='utf-8') as array:
    for lines in array:
        bf_list = lines.split("	")
        if bf_list[0] in ignore_list:
            pass
        else:
            UNIONL.append(bf_list)
# 激励文件自动化文件部署
# UNIONL[x][5]对应EXCEL中    发放
# UNIONL[x][0]对应EXCEL中    ID
for x in range(len(UNIONL)):
    # 银箱子
    with open(JLFile[1], 'a', encoding='utf-8') as JLF:
        if float(UNIONL[x][5]) > 0:
            JLF.write("8/8	" + UNIONL[x][0] + "	90	X	0	0	0	0	8" + "\n")
    # 金箱子
    with open(JLFile[0], 'a', encoding='utf-8') as JLF:
        if UNIONL[x][5] == '6':
            JLF.write("6/6	" + UNIONL[x][0] + "	90	X	0	0	0	0	6" + "\n")
        elif UNIONL[x][5] == '5':
            JLF.write("5/6	" + UNIONL[x][0] + "	90	X	0	0	0	0	5" + "\n")
        elif UNIONL[x][5] == '4':
            JLF.write("4/6	" + UNIONL[x][0] + "	90	X	0	0	0	0	4" + "\n")
        elif UNIONL[x][5] == '3':
            JLF.write("3/6	" + UNIONL[x][0] + "	90	X	0	0	0	0	3" + "\n")
        elif UNIONL[x][5] == '2':
            JLF.write("2/6	" + UNIONL[x][0] + "	90	X	0	0	0	0	2" + "\n")
        elif UNIONL[x][5] == '1':
            JLF.write("1/6	" + UNIONL[x][0] + "	90	X	0	0	0	0	1" + "\n")
        else:
            pass

today = datetime.datetime.now().strftime('%Y-%m-%d')

rc = 'rar a {rar_name} {F1} {F2}'.format(rar_name='激励发放'+today+'.rar', F1=JLFile[0], F2=JLFile[1])
res = os.system(rc)
print(res)

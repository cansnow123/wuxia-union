from xlrd import *

# Template
Template = "发放激励\n领取情况\t帮众\t等级\t职位\t剩余PVP-DKP\t修改PVP-DKP\t剩余PVE-DKP\t修改PVE-DKP\t发放数量\n"
GLFile = "BangPai_DKPFaFangJiLi.txt"
SLFile = "BangPai_DKPFaFangJiLi.txt银"

with open(GLFile, 'w', encoding='utf-8') as init_gf:
    init_gf.write(Template)
with open(SLFile, 'w', encoding='utf-8') as init_sf:
    init_sf.write(Template)

wb = open_workbook('a.xlsx')
sheet = wb.sheet_by_name('奖励发放')


Replace_Dict = [
    ['こ若若や', ['梨花雨落']],
    ['こ奉先や', ['快使用双节棍戳']]
]


def rpj(name):
    for nl in Replace_Dict:
        for sn in nl[1]:
            if sn == name:
                name = nl[0]
            else:
                pass
    return name


# CONVERT EXCEL SHEET TO ARR
def sh2arr(sh):
    temp = []
    for row in range(1, sh.nrows):
        cell_v = []
        if sh.cell(row, 0).value != ("" or "None"):
            cell_v.append(rpj(sh.cell(row, 0).value))
            cell_v.append(int(sh.cell(row, 5).value))
        else:
            pass
        if not cell_v:
            pass
        else:
            temp.append(cell_v)
    return temp


UNIONL = sh2arr(sheet)

# 激励文件部署
for x in range(len(UNIONL)):
    # 银箱子
    with open(SLFile, 'a', encoding='utf-8') as SLF:
        if UNIONL[x][1] == 8:
            SLF.write("8/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
        elif UNIONL[x][1] == 7:
            SLF.write("8/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
        elif UNIONL[x][1] == 6:
            SLF.write("8/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
        elif UNIONL[x][1] == 5:
            SLF.write("8/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
        elif UNIONL[x][1] == 4:
            SLF.write("6/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
        elif UNIONL[x][1] == 3:
            SLF.write("6/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
        elif UNIONL[x][1] == 2:
            SLF.write("4/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t4" + "\n")
        else:
            pass
    # 金箱子
    with open(GLFile, 'a', encoding='utf-8') as JLF:
        if UNIONL[x][1] == 8:
            JLF.write("8/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
        elif UNIONL[x][1] == 7:
            JLF.write("7/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t7" + "\n")
        elif UNIONL[x][1] == 6:
            JLF.write("6/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
        elif UNIONL[x][1] == 5:
            JLF.write("5/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t5" + "\n")
        elif UNIONL[x][1] == 4:
            JLF.write("4/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t4" + "\n")
        elif UNIONL[x][1] == 3:
            JLF.write("3/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t3" + "\n")
        elif UNIONL[x][1] == 2:
            JLF.write("2/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t2" + "\n")
        elif UNIONL[x][1] == 1:
            JLF.write("1/8\t" + UNIONL[x][0] + "\t95\tX\t0\t0\t0\t0\t1" + "\n")
        else:
            pass

# today = datetime.datetime.now().strftime('%Y-%m-%d')
#
# rc = 'rar a {rar_name} {F}'.format(rar_name='激励发放' + today + '.rar', F=GLFile)
# res = os.system(rc)
# print(res)

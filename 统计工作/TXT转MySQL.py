import re

def rpfun(list_str):
    rp = re.sub("	", "','", list_str)
    return rp

Pre = open('mysql.txt', 'r', encoding= 'utf8')
Con = open('MySQL_Converted.txt', 'w',encoding= 'utf8')
for line in Pre.readlines():
    new_list = rpfun(line).strip('\n')
    if new_list != "":
        if 'ID' in new_list:
            pass
        else:
            Con.writelines("INSERT INTO `wuxia`.`reward` (`id`, `bangpai`,`weiren`, `zuixia`,`xuezhan`,`zhanchang`,`lueduo`,`zhengfeng`,`dkp`, `xiangzi`)VALUES ('"+new_list+"');"+"\n")
    else:
        pass
Con.close()
Pre.close()


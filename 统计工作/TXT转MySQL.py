import re

def rpfun(list_str):
    rp = re.sub("	", "','", list_str)
    return rp

Pre = open('mysql.txt', 'r', encoding= 'utf8')
Con = open('MySQL_Converted.txt', 'w',encoding= 'utf8')
for line in Pre.readlines():
    new_list = rpfun(line).strip('\n')
    if new_list != "":
        Con.writelines("INSERT INTO `wuxia`.`reward` (`id`, `guild_num`,`rob`, `society_war`,`guild_act`,`guild_war`,`sum_re`,`real_re`,`date_end`)VALUES ('"+new_list+"');"+"\n")
    else:
        pass
Con.close()
Pre.close()


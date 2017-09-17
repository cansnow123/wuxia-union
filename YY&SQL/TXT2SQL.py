import re


def rp_fun(list_str):
    rp = re.sub("	", "','", list_str)
    return rp

with open('MySQL_Converted.txt', 'w', encoding='utf8') as Con, open('mysql.txt', 'r', encoding='utf8') as Pre:
    for line in Pre.readlines():
        new_list = rp_fun(line).strip('\n')
        Con.writelines("INSERT INTO `wuxia`.`reward` (`id`, `guild_num`,`rob`, `society_war`,`guild_act`,`guild_war`,`sum_re`,`real_re`,`date_end`)VALUES ('"+new_list+"');"+"\n")

import re

import zhconv

name_list = []


def get_name_list(input_file, pattern):
    count = 0
    with open(input_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            match = pattern.search(line)
            if match:
                name_list.append(line.strip('\n'))
    if name_list:
        print("搜索结果如下：")
        for i in name_list:
            count += 1
            text = zhconv.convert(i, 'zh-cn')
            print(text)
        print("一共%s条弹幕" % count)
    else:
        print("Error:未找到该用户发的弹幕")
    


while True:
    try:
        input_file = input("请将弹幕文件拖入框中：")
        flag = int(input("选择搜索方式（1为精准搜索，2为模糊搜索）："))
        if flag == 1:
            user_name = input("输入用户名称：")
            pattern = re.compile(r'((:%s) ).*' % user_name)
            get_name_list(input_file, pattern)
            print("输入3直接退出软件！")
            name_list = []
        elif flag == 2:
            user_name = input("输入用户名称：")
            pattern = re.compile(r'(.*?(%s).* ).*' % user_name)
            get_name_list(input_file, pattern)
            print("输入3直接退出软件！")
            name_list = []
        elif flag == 3:
            break
        else:
            print("输入有误！请重新输入。")
    except:
        print("弹幕文件路径有误！")
        pass

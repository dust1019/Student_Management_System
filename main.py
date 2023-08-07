# -*- coding: utf-8 -*-
# Project: Student_sys
# OS: Windows 11
# IDE: PyCharm
# Author: Dust
# Date: 2023/8/6

import ast
import re
import time


def add_stu_info():
    print('*****录入学生信息*****')
    print('--------------------')
    print('1.录入学生ID及姓名')
    print('2.录入学生各科目分数')
    print('0.返回上一级')
    print('--------------------')
    # 获取用户输入
    while True:
        user_input = input('请输入功能选择：')
        if user_input in ['1', '2', '0']:
            if user_input == '1':
                add_stu_info1()
                break
            elif user_input == '2':
                add_stu_info2()
                break
            elif user_input == '0':
                sys_start()
                break
            break
        else:
            print('输入无效')


# 录入学生ID，姓名
def add_stu_info1():
    pattern = r"^[0-9]{4}$"
    pattern1 = r"^[\u4e00-\u9fa5]{2,6}$"
    while True:
        stu_ID = input('请输入学生4位的ID: ')
        stu_Name = input('请输入学生的姓名: ')
        # 检测ID是否已经存在
        if re.match(pattern, stu_ID) and re.match(pattern1, stu_Name) and not check_stu(stu_ID):
            print('ID: ', stu_ID)
            print('姓名: ', stu_Name)
            while True:
                userInput = input('确认录入系统（Y/N）：')
                if userInput == 'y' or userInput == 'Y':
                    with open('student_data.txt', 'a', encoding='UTF-8') as file:
                        dic = {'id': stu_ID, '姓名': stu_Name}
                        file.write(str(dic) + '\n')
                    print('录入成功')
                    sys_start()
                    break
                elif userInput == 'n' or userInput == 'N':
                    print('未录入，退出系统')
                    break
                else:
                    vaild_input()
            break
        else:
            print('学生已存在，或者输入格式错误，请检查')


# 录入学生分数
def add_stu_info2():
    stu_id = input('请输入学生ID: ')
    all_stu = all_stu_info()
    for stu_info in all_stu:
        if stu_info['id'] == stu_id:
            print('ID:', stu_info['id'], ' 姓名: ', stu_info['姓名'])
            yuwen = input('请输入语文分数：')
            math = input('请输入数学分数：')
            english = input('请输入英语分数：')
            grade = {'语文': yuwen, '数学': math, '英语': english}
            stu_info.update(grade)  # 更新学生的信息
            #更新成绩到txt
            update_data(all_stu)
            print('ID:', stu_info['id'],
                  ' 姓名: ', stu_info['姓名'],
                  ' 语文',stu_info['语文'],
                  ' 数学',stu_info['数学'],
                  ' 英语',stu_info['英语'])
            print('更新完成，2s后返回上一级')

            time.sleep(2)
            add_stu_info()
            break
    else:
        print('未查询到该学生')


def update_data(data=[]):
    data = data
    with open('student_data.txt','w',encoding='utf-8') as file:
        for item in data:
            file.write(str(item) + '\n')

    # stu_info = check_stu(input('请输入学生ID: '))
    # if stu_info:
    #     for key, value in stu_info.items():
    #         print(key, ':', value, end='\t')
    #     while True:
    #         print()
    #         yuwen = input('请输入语文分数：')
    #         math = input('请输入数学分数：')
    #         english = input('请输入英语分数：')
    #         if all(i.isdigit() and 0 < int(i) <= 100 for i in (yuwen, math, english)):
    #             print('语文：', yuwen)
    #             print('数学：', math)
    #             print('英语：', english)
    #             grade = {'语文': yuwen, '数学': math, '英语': english}
    #             stu_info.update(grade)
    #             with open('student_data.txt', 'w', encoding='UTF-8') as file:
    #                 file.writelines(str(stu_info) + '\n')
    #             print('录入完成，2秒后返回主菜单')
    #             time.sleep(2)
    #             sys_start()
    #             break
    #
    #         else:
    #             print('输入有误')
    # else:
    #     print('未查询到，或输入出错')
    #     add_stu_info()


# 根据ID查询学生是否存在，若存在返回该学生信息类型字典，否则返回false
def check_stu(stu_id):
    pattern = rf"{{'id': '{stu_id}', [^}}]+}}"
    id = stu_id
    with open('student_data.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                data = ast.literal_eval(match.group())
                return data
    return False


# 根据姓名查找，如果没有返回false，如果存在重名返回一个对象
def check_stu_name(stu_name):
    pass


def find_stu_info():
    print('*****查找学生信息*****')
    print('--------------------')
    print('1.ID查找')
    print('2.姓名查找')
    print('0.返回上一级')
    print('--------------------')

    # 获取用户输入
    while True:
        user_input = input('请输入功能选择：')
        if user_input in ['1', '2', '0']:
            if user_input == '1':
                stu_id = input('请输入四位ID: ')
                if stu_id.isdigit() and len(stu_id) == 4:
                    if check_stu(stu_id) == False:
                        print('未查询到')
                    else:
                        print(check_stu(stu_id))
                else:
                    print('输入有误，自动返回上一级')
                    find_stu_info()
            elif user_input == '2':
                check_stu_name()
            elif user_input == '0':
                sys_start()
                break
            break
        else:
            print('输入无效')

# 获取整个数据库信息，返回列表
def all_stu_info(show=False):
    students = []  # 将students初始化为列表
    with open('student_data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            student = ast.literal_eval(line.strip())
            id_str = student.get('id', '空').ljust(5, chr(12288))
            name_str = student.get('姓名', '空').ljust(6, chr(12288))
            yuwen_str = student.get('语文', '空').ljust(4, chr(12288))
            math_str = student.get('数学', '空').ljust(4, chr(12288))
            english_str = student.get('英语', '空').ljust(4, chr(12288))

            if show:  # 直接检查show参数是否为True
                print(f'ID: {id_str} 姓名: {name_str} 语文: {yuwen_str} 数学: {math_str} 英语: {english_str}')

            students.append(student)

    return students

def vaild_input():
    print('输入无效，请重新输入')


def sys_start():
    # 程序开始
    print('======欢迎进入学生管理系统======')
    print('-----------------------------')
    print('1.录入学生信息')
    print('2.查找学生信息')
    print('3.全部学生信息')
    print('0.退出系统')
    print('-----------------------------')

    # 获取用户输入
    while True:
        user_input = input('请输入功能选择：')
        if user_input in ['1', '2', '3', '0']:
            if user_input == '1':
                add_stu_info()
            elif user_input == '2':
                find_stu_info()
            elif user_input == '3':
                all_stu_info('True')
            elif user_input == '0':
                print('感谢使用，再见！')
                break
            break
        else:
            print('输入无效')


sys_start()

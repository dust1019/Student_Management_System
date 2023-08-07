# -*- coding: utf-8 -*-
# Project: Student_sys
# OS: Windows 11
# IDE: PyCharm
# Author: Dust
# Date: 2023/8/6
# ver: 1.00

import os
import sys
import re
import ast
def add_stu_info():
    print('*****录入学生信息*****')
    print('--------------------')
    print('1.录入学生ID及姓名')
    print('2.录入学生各科目分数')
    print('0.返回上一级')
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

#录入学生ID，姓名
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
                userInput=input('确认录入系统（Y/N）：')
                if userInput == 'y' or userInput == 'Y' :
                    with open('student_data.txt', 'a', encoding = 'UTF-8') as file:
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

#录入学生分数
def add_stu_info2():
    stu_info = check_stu(input('请输入学生ID: '))
    if stu_info:
        for key, value in stu_info.items():
            print(key, ':', value, end='\t')
        while True:
            print()
            yuwen = input('请输入语文分数：')
            math = input('请输入数学分数：')
            english = input('请输入英语分数：')
            if all(i.isdigit() and 0 < int(i) <= 100 for i in (yuwen, math, english)):
                print('语文：', yuwen)
                print('数学：', math)
                print('英语：', english)
                break
            else:
                print('输入有误')
    else:
        print('未查询到，或输入出错')
        add_stu_info()


#根据ID查询学生是否存在，若存在返回学生信息，否则返回false
def check_stu(stu_id):
    pattern = rf"{{'id': '{stu_id}', [^}}]+}}"
    id = stu_id
    with open('student_data.txt','r',encoding='UTF-8') as file:
        for line in file:
            match = re.search(pattern,line)
            if match:
                data = ast.literal_eval(match.group())
                return data
    return False


def find_stu_info():
    print('查找学生信息')

def all_stu_info():
    print('全部学生信息')

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
        user_input=input('请输入功能选择：')
        if user_input in ['1', '2', '3', '0']:
            if user_input == '1':
                add_stu_info()
            elif user_input == '2':
                find_stu_info()
            elif user_input == '3':
                all_stu_info()
            elif user_input == '0':
                print('感谢使用，再见！')
                break
            break
        else:
            print('输入无效')


sys_start()


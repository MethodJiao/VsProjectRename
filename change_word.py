# -*- coding: utf-8 -*-
"""
@Author  : JiaoJingWei
@File    : change_word.py
@Time    : 2020/5/19 9:54 上午
@desc    :
"""

import os
import chardet

def iter_files(old_kw, new_kw, root_dir):
    """
    遍历根目录
    :param old_kw: 旧词
    :param new_kw: 新词
    :param root_dir: 目录的绝对路径
    :return:
    """
    for root, dirs, files in os.walk(root_dir, topdown=False):
        # 先遍历最内层，逐步向上
        for file_name in files:
            old_file_path = os.path.join(root, file_name)
            file_data = ""
            # 读该文件编码格式
            with open(old_file_path, 'rb')as file:
                curr_encode = chardet.detect(file.read())['encoding']
            # 如果被替换的字符串在文件内容中，先按行读出来，在替换
            with open(old_file_path, 'r', encoding=curr_encode, errors='ignore') as f:
                for line in f.readlines():
                    new_line = line.replace(old_kw, new_kw)
                    file_data += new_line
            with open(old_file_path, 'w', encoding=curr_encode, errors='ignore') as f:
                f.write(file_data)

            # 如果被替换的字符串在文件的名中，则替换成新的
            if old_kw in file_name:
                new_file_name = file_name.replace(old_kw, new_kw)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)

        for dir_name in dirs:
            old_dir_path = os.path.join(root, dir_name)
            # 如果被替换的字符串在文件夹的名中，则替换成新的
            if old_kw in dir_name:
                new_dir_name = dir_name.replace(old_kw, new_kw)
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(old_dir_path, new_dir_path)


def run():
    print('输入项目文件夹绝对路径《会修改此文件夹层级之下所有匹配关键字》')
    path = input()
    path = path.replace('\\', '/')
    print('输入原项目名称')
    old_project_name = input()
    print('输入新项目名称')
    new_project_name = input()
    iter_files(old_project_name, new_project_name, path)


if __name__ == '__main__':
    run()

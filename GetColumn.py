# -*- coding: utf-8 -*-
import csv
import os
import shutil

wavDir = os.getcwd() + "/wav"


def mk_dir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("[mkdir],new folder,path:%s", path)
    else:
        print("wav dir has create success!")


def mk_file(filename):
    if not os.path.exists(filename):
        wav_file = open(filename, 'w')
        wav_file.close()
    else:
        print("file " + filename + " ,has exits!")


def get_csv_file():
    csv_file_dir = os.getcwd() + "/csv"
    csv_files = os.listdir(csv_file_dir)
    return csv_file_dir + "/" + csv_files[0] if len(csv_files) else ""


def delete_wav_file():
    if os.path.exists(wavDir):
        shutil.rmtree(wavDir)


csv_file = get_csv_file()

if csv_file:
    print("开始读取csv文件:" + csv_file)

    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            rows = [row['ID'] for row in reader]
        except KeyError:
            rows = ""
            print("请检查csv文件中要读取的列的名字，确保为`ID`")

    if(len(rows)):
        delete_wav_file()
        print(wavDir)
        mk_dir(wavDir)
        for x in rows:
            file = wavDir + "/" + x + ".wav"
            # print(file)
            mk_file(file)
        print("创建wav文件成功!")
    else:
        print("请检查csv文件，没有要读取的内容")
else:
    print("没有csv文件!")




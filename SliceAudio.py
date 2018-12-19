import csv
import os
import shutil
from pydub import AudioSegment

wavDir = os.getcwd() + "/wav"

origin_wav_file = os.getcwd() + "/originwav/slice.wav"

slice_wav_save_dir = os.getcwd() + "/slice_wav"

slice_wav_save_file = os.getcwd() + "/slice_wav/"

sound = AudioSegment.from_wav(origin_wav_file)


def mk_dir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("[mkdir],new folder,path:%s", path)
    else:
        print("wav dir has create success!")


def get_csv_file():
    csv_file_dir = os.getcwd() + "/csv"
    csv_files = os.listdir(csv_file_dir)
    for file in csv_files:
        if (file == "SliceAudio.csv"):
            return csv_file_dir + "/" + file
    return ""


def delete_wav_file(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


csv_file = get_csv_file()

print("file:" + csv_file)

if csv_file:
    print("开始读取csv文件:" + csv_file)
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        IDS = [row['ID'] for row in reader]
        print(IDS)
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        STARTS = [row['START'] for row in reader]
        print(STARTS)
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        ENDS = [row['END'] for row in reader]
        print(ENDS)

    if(len(IDS)):
        delete_wav_file(slice_wav_save_dir)
        mk_dir(slice_wav_save_dir)
        for i in range(len(IDS)):
            start_time = ((int (STARTS[i].split(':')[0])) * 3600 + (int (STARTS[i].split(':')[1])) * 60 + (int (STARTS[i].split(':')[2]))) * 1000
            end_time = ((int (ENDS[i].split(':')[0])) * 3600 + (int (ENDS[i].split(':')[1])) * 60 + (int (ENDS[i].split(':')[2]))) * 1000
            slice_sound = sound[start_time:end_time]
            save_file = slice_wav_save_file + IDS[i] + ".wav"
            slice_sound.export(save_file, format="wav")
    else:
        print("请检查csv文件，没有要读取的内容")
else:
    print("没有csv文件!")


# 导入os模块和random模块
import os
import random

# 定义源文件夹和目标文件夹的路径
source_folder = "/gemini/code/dataset/train" # 你可以修改为你的源文件夹路径
target_folder = "/gemini/code/dataset/test" # 你可以修改为你的目标文件夹路径

# 遍历源文件夹中的所有子文件夹
for subfolder in os.listdir(source_folder):
    # 获取子文件夹的完整路径
    subfolder_path = os.path.join(source_folder, subfolder)
    # 判断是否是文件夹
    if os.path.isdir(subfolder_path):
        # 获取子文件夹中的所有文件名
        files = os.listdir(subfolder_path)
        # 随机选择10%的文件
        sample_size = int(len(files) * 0.1) # 取整数
        sample_files = random.sample(files, sample_size) # 随机抽样
        # 创建目标文件夹中的同名子文件夹，如果不存在的话
        target_subfolder_path = os.path.join(target_folder, subfolder)
        if not os.path.exists(target_subfolder_path):
            os.makedirs(target_subfolder_path)
        # 遍历抽样的文件
        for file in sample_files:
            # 获取源文件和目标文件的完整路径
            source_file_path = os.path.join(subfolder_path, file)
            target_file_path = os.path.join(target_subfolder_path, file)
            # 移动文件到目标文件夹中
            os.rename(source_file_path, target_file_path)
            # 打印移动成功的信息
            print(f"Moved {file} from {subfolder} to {target_subfolder_path}")

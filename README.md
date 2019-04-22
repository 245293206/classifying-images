# classifying-image

#### 介绍
这是我在gitee上的第一个有关AI的练习项目

- step one : time counter
```
from time import time sleep

def main():
    start_time = time()

    sleep(75)

    end_time = time()

    tot_time = end_time - start_time
    hours = round(tot_time / 3600)
    minutes = round((tot_time%3600)/60)
    seconds = round((tot_time%3600)%60)

if name == "__main__":
  main()
```
- step two : args input parse
```
import argparse

def get_input_args():
    """just as the function_name says: 获取命令行输入的参数解析后放入数据结构中并返回
    sunch as input:
        python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
        get --dir --arch --dogfile and parser deal with them
    ArgumentParser object.
     3 command line arguments are created:
       --dir - Path to the pet image files(default- 'pet_images/')
       --arch - CNN model architecture to use for image classification(default-
              pick any of the following vgg, alexnet, resnet)
       --dogfile - Text file that contains all labels associated to dogs(default-
                'dognames.txt'
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """
    # args解析器创建
    parser = argparse.ArgumentParser()
    # 添加参数 dir
    parser.add_argument('--dir',type=str,default='pet_images/',help='path to the folder my_folder')
    #添加参数 arch
    parser.add_argument('--arch',type=str,default='vgg',help='choose a model from [vgg,resnet,alexnet]')
    #添加参数 dogfile
    parser.add_argument('--dogfile',type=str,default='dognames.txt',help='select the file which named dognames.txt')

    #返回args 解析结果
    return parser.parse_args()

```

- understanding mutable and immutable containers
  - 函数外创建 作为参数传入
```
def edit_pets(pets):
    pets.pop(1)
    pets.append("Bella")
    pets += ["Buddy"]

dogs = ["Luna","Cody","Ally","Lincoln"]
edit_pets(dogs)
print(dogs)
```
```
#output
['Luna', 'Ally', 'Lincoln', 'Bella', 'Buddy']
```
---
```
def edit_pets():
    dogs = ["Luna","Cody","Ally","Lincoln"]
    pets.pop(1)
    pets.append("Bella")
    pets += ["Buddy"]


edit_pets()
print("Done")
```
```
#output
Done
```
---
```
def edit_pets():
    pets = ["Luna","Cody","Ally","Lincoln"]
    pets.pop(1)
    pets.append("Bella")
    pets += ["Buddy"]
    return pets
dogs = edit_pets()
print(dogs)
```
```
['Luna', 'Ally', 'Lincoln', 'Bella', 'Buddy']
```

- 创建动物图片标签
```
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image 
    files. Reads in pet filenames and extracts the pet image labels from the 
    filenames and returns these labels as petlabel_dic. This is used to check 
    the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)  
    """
    # 得到文件名列表
    in_files = listdir(image_dir)
    # 以key：filename value:lable 形式，存储当前目录所有图片的信息

    #创建一个空的字典
    petlabels_dic = dict()

    for idx in range(0,len(in_files)):
        if(in_files[idx][0] != "."):
            #排除不是image的文件
            image_name = in_files[idx].lower().split("_")
            pet_label = ""
            #获取label
            for word in image_name:
                if(word.isalpha()):
                    pet_label += word + " "
            #去除\n
            pet_label = pet_label.strip()
            if(in_files[idx] not in petlabels_dic):
                petlabels_dic[in_files[idx]] = pet_label
            else:
                print("Warning: files exist in dictionary: {}".format(in_files[idx]))
    return petlabels_dic
```

from xml.etree import ElementTree
import os
from shutil import copy,rmtree
import random

def adapt_2018():

    base_path = "RDD_Dataset_2018/"
    damageTypes=["D00", "D01", "D10", "D11", "D20", "D40", "D43", "D44"]
    damageType_to_class = {"D00":0,"D01":1, "D10":2, "D11":3, "D20":4, "D40":5, "D43":6, "D44":7}
    # govs corresponds to municipality name.
    govs = ["Adachi", "Chiba", "Ichihara", "Muroran", "Nagakute", "Numazu", "Sumida"]

    # Create the folders
    os.makedirs('RDD_Dataset_2018_Yolo/images/train')
    os.makedirs('RDD_Dataset_2018_Yolo/images/val')
    os.makedirs('RDD_Dataset_2018_Yolo/labels/train')
    os.makedirs('RDD_Dataset_2018_Yolo/labels/val')

    PATH_IMGS = "RDD_Dataset_2018_Yolo/images/"
    PATH_LABELS = "RDD_Dataset_2018_Yolo/labels/"

    # Move the val and train datasets in a good architecture for YoloV5
    print("Moving the 2018 dataset in a good architecture for YoloV5 ...")

    for gov in govs:
        file = open(base_path + gov + "/ImageSets/Main/train.txt")
        for line in file :
            img_name = line.rstrip('\n')
            img_path = base_path + gov + "/JPEGImages/" + img_name + ".jpg"
            train_path = PATH_IMGS + "train/"
            copy(img_path,train_path)

        file.close()
        file = open(base_path + gov + "/ImageSets/Main/val.txt")
        for line in file :
            img_name = line.rstrip('\n')
            img_path = base_path + gov + "/JPEGImages/" + img_name + ".jpg"
            val_path = PATH_IMGS + "val/"
            copy(img_path,val_path)

        file.close()
    
    print("Done!\n")

    # Adapt the labels to YoloV5 format
    print("Adapting 2018 labels to YoloV5 format ...")

    for gov in govs:
        
        for phase in ['train','val'] :

            file_list = []

            file_for_names = open(base_path + gov + "/ImageSets/Main/{}.txt".format(phase))
            for line in file_for_names :
                img_name = line.rstrip('\n')
                file_list.append(img_name)
            file_for_names.close()

            for file in file_list:
                if file =='.DS_Store':
                    pass
                else:
                    infile_xml = open(base_path + gov + '/Annotations/' + file+'.xml')
                    tree = ElementTree.parse(infile_xml)
                    root = tree.getroot()
                    file_txt = open(PATH_LABELS+phase+'/'+file+'.txt','a')
                    for obj in root.iter('object'):
                        cls_name = obj.find('name').text

                        if cls_name == 'D30' :
                            pass
                        else :

                            xmlbox = obj.find('bndbox')
                            xmin = int(xmlbox.find('xmin').text)
                            xmax = int(xmlbox.find('xmax').text)
                            ymin = int(xmlbox.find('ymin').text)
                            ymax = int(xmlbox.find('ymax').text)

                            x_center = 0.5*(xmin + xmax)
                            y_center = 0.5*(ymin + ymax)
                            width = xmax - xmin
                            height = ymax - ymin
                            
                            x_center, y_center, width, height = round(x_center/600,5), round(y_center/600,5), round(width/600,5), round(height/600,5)

                            class_number = damageType_to_class[cls_name]

                            file_txt.write(str(class_number)+' '+str(x_center)+' '+str(y_center)+' '+str(width)+' '+str(height)+'\n')
                    file_txt.close()
    print("Done!\n")
    os.remove('._RoadDamageDataset')
    rmtree('RDD_Dataset_2018', ignore_errors=True)
    print("Original dataset removed.")

def adapt_2020():
    countries = ['Czech','India','Japan']
    base_path = "RDD_Dataset_2020/"
    damageType_to_class = {"D00":0,"D10":1, "D20":2, "D40":3}
    damageTypes = ['D00','D10','D20','D40']
    class_dict = {'D00':0,'D10':0,'D20':0,'D40':0}

    file_list = []
    for country in countries :
        file_list_country = os.listdir('RDD_Dataset_2020/{}/images'.format(country))
        random.shuffle(file_list_country)
        file_list.append(file_list_country)
        print("Number of images in "+country+" : "+str(len(file_list_country)))

    # Create the folders
    os.makedirs('RDD_Dataset_2020_Yolo/images/train')
    os.makedirs('RDD_Dataset_2020_Yolo/images/val')
    os.makedirs('RDD_Dataset_2020_Yolo/labels/train')
    os.makedirs('RDD_Dataset_2020_Yolo/labels/val')

    PROPORTION_TRAIN = 0.9 # Proportion of the images used for training
    PATH_IMGS = "RDD_Dataset_2020_Yolo/images/"
    PATH_LABELS = "RDD_Dataset_2020_Yolo/labels/"

    file_list_train = []
    file_list_val = []
    for i in range(len(countries)) :
        file_list_train.append(file_list[i][:int(PROPORTION_TRAIN*len(file_list[i]))])
        file_list_val.append(file_list[i][int(PROPORTION_TRAIN*len(file_list[i])):])

    phases = ['train','val']
    file_list_train_val = [file_list_train,file_list_val]
    for (j,phase) in enumerate(phases) :
        file_list_phase = file_list_train_val[j]
        for (i,country) in enumerate(countries) :
            file_list_country = file_list_phase[i]

            ################################### FOR THE LABELS ###################################
            for file in file_list_country:
                file_name = file.rsplit('.')[0]
                infile_xml = open(base_path + country + '/annotations/xmls/' + file_name +'.xml')
                tree = ElementTree.parse(infile_xml)
                root = tree.getroot()
                file_txt = open(PATH_LABELS+phase+'/'+file_name+'.txt','w')

                for obj in root.iter('size'):
                    img_height = int(obj.find('height').text)
                    img_width = int(obj.find('width').text)

                nb_boxes_img = 0
                for obj in root.iter('object'):
                    cls_name = obj.find('name').text
                    if cls_name not in damageTypes :
                        pass
                    else :
                        class_dict[cls_name]+=1
                        nb_boxes_img += 1
                        xmlbox = obj.find('bndbox')
                        xmin = int(xmlbox.find('xmin').text)
                        xmax = int(xmlbox.find('xmax').text)
                        ymin = int(xmlbox.find('ymin').text)
                        ymax = int(xmlbox.find('ymax').text)

                        x_center = 0.5*(xmin + xmax)
                        y_center = 0.5*(ymin + ymax)
                        width = xmax - xmin
                        height = ymax - ymin
                        
                        x_center, y_center, width, height = round(x_center/img_width,5), round(y_center/img_height,5), round(width/img_width,5), round(height/img_height,5)

                        class_number = damageType_to_class[cls_name]

                        file_txt.write(str(class_number)+' '+str(x_center)+' '+str(y_center)+' '+str(width)+' '+str(height)+'\n')
                file_txt.close()
                ################################ FOR THE IMAGES ########################################
                img_path = base_path + country + '/images/' + file
                phase_path = PATH_IMGS+phase+'/'
                copy(img_path,phase_path)

    rmtree('RDD_Dataset_2020', ignore_errors=True)
    print("Original dataset removed.")
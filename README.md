# **Introduction**

This object detection project was made during my internship at Universitat Rovira i Virgili, Catalunya, Spain. The goal is to detect and classify road damage with images taken from inside a car.

![](/readme_img/crack2.png)
![](/readme_img/example_image.png)

The following tutorial will help you reproduce the work and train models using YoloV5 on the [Global Road Damage Detection Challenge](https://github.com/sekilab/RoadDamageDetector) Datasets from 2018 and 2020.

# **Set up**

***
The first thing to do is install the requirements by typing in a shell :
```
pip install -r requirements.txt
```
Then you can execute *setup.py* which will download the two datasets and adapt everything for YoloV5 (this step can take some time depending on your network connection) :
```
python setup.py
```
Then change your directory to yolov5 :
```
cd yolov5
```
Install dependencies for yolov5 :
```
pip install -qr requirements.txt
```
(*optional*) If you want to download trained weights on the datasets you can type (at the root of the github repository):
```
python weights.py
```
The weights will be accessible in the folder ```weights/year_of_the_dataset/``` where *year_of_the_dataset* is either 2018 or 2020.

The setup is finished. You can start the training and/or the testing.

# **Training and testing**

If you have any problem with training or testing with YoloV5, please refer to the [YoloV5 wiki](https://github.com/ultralytics/yolov5/wiki)

Make sure your current directory is yolov5 and that you have the datasets ready (RDD_Dataset_2018_Yolo and RDD_Dataset_2020_Yolo folders).

If you want to train/test on the 2018 dataset, use ```--data rdd2018.yaml``` in the commands. If you want to use the 2020 dataset, use ```--data rdd2020.yaml```

## **Train models**

Every train run is saved in yolov5/runs/train/
***
Train with default hyperparameters and predefined weights :
```
python train.py --img 608 --batch 16 --epochs 15 --data rdd2018.yaml --weights 'yolov5x.pt'
```
Train from scratch using yolov5 architecture and randomly initialised weights :
```
python train.py --img 608 --batch 16 --epochs 15 --data rdd2018.yaml --weights ' ' -cfg 'yolov5x.yaml'
```
Use hyperparameter evolution to optimise them
```
python train.py --img 608 --batch 16 --epochs 15 --data rdd2018.yaml --weights 'yolov5x.pt' --evolve 50
```

## **Test models**
Every test run is saved in yolov5/runs/val/
***
Test a neural network on a test dataset :
```
python val.py --weights '../weights/2018/yolov5x_2_608.pt' --data rdd2018.yaml --img 608
```
Test a neural network on a test dataset with Test-Time Augmentation :
```
python val.py --weights '../weights/2018/yolov5x_2_608.pt' --data rdd2018.yaml --img 608 --augment
```
Use model ensembling to make predictions on a test dataset :
```
python val.py --weights '../weights/2018/yolov5x_2_608.pt' '../weights/2018/yolov5x_448.pt' --data rdd2018.yaml --img 608
```

## **Make detections on images**
This section is to produce images on which we can see the predictions.

Every detect run is saved in yolov5/runs/detect/

Detect damage on images using a trained model (and test-time augmentation) :
```
python detect.py --weights '../weights/2018/yolov5x_2_608.pt' --data rdd2018.yaml --img 608 --augment
```

# **Resources**
* My internship report, containing information about the datasets and results of training and testing : the file *Internship_report.pdf*
* [YoloV5 Wiki](https://github.com/ultralytics/yolov5/wiki) containing a lot of useful information and commands to train your models.

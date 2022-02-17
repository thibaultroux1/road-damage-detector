
from download import download_2018, download_2020
from xmlToYolo import adapt_2018, adapt_2020
from git import Repo
import os

download_2018()
adapt_2018()
download_2020()
adapt_2020()

Repo.clone_from('https://github.com/ultralytics/yolov5', 'yolov5')

os.rename('rdd2018.yaml','yolov5/data/rdd2018.yaml')
os.rename('rdd2020.yaml','yolov5/data/rdd2020.yaml')
import urllib.request
import tarfile
import os
from shutil import rmtree

def download_2018() :
    print('Downloading the 2018 GRDDC Dataset (1.7 GB) ...')

    url = 'https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/Japan/CACAIE2018/RoadDamageDataset.tar.gz'
    urllib.request.urlretrieve(url, 'RDD_Dataset_2018.tar.gz')

    print('Extracting file ...')

    my_tar = tarfile.open('RDD_Dataset_2018.tar.gz')
    my_tar.extractall('./') # specify which folder to extract to
    my_tar.close()
    os.rename('RoadDamageDataset','RDD_Dataset_2018')

    print('Extraction done !')

    os.remove('RDD_Dataset_2018.tar.gz')
    print('RDD_Dataset_2018.tar.gz removed.\n')

def download_2020():
    print('Downloading the 2020 GRDDC Dataset (1.1 GB)')

    url = 'https://md-datasets-public-files-prod.s3.eu-west-1.amazonaws.com/7b38c0a4-9c9a-4aa7-8c45-290b70c36262'
    urllib.request.urlretrieve(url, 'RDD_Dataset_2020.tar.gz')

    print('Extracting file ...')

    my_tar = tarfile.open('RDD_Dataset_2020.tar.gz')
    my_tar.extractall('./') # specify which folder to extract to
    my_tar.close()
    os.rename('train','RDD_Dataset_2020')

    print('Extraction done !')

    os.remove('RDD_Dataset_2020.tar.gz')
    print('RDD_Dataset_2020.tar.gz removed.\n')

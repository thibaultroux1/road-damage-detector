import urllib.request
import zipfile

def download_weights() :
    url = 'https://ucab2236b84fb605a1039f737562.dl.dropboxusercontent.com/cd/0/get/BVkA0ky5OPRXhmZcLoIvPJ7DZKzE3Lr_dZoXg92FyNvJW1z2uLKZJCoWkgayLDicDvjuriMhXrbsAX6dFPv60wgdK9xhYv17qYeSbcyFbhVCYN4ITJN8iVfuPEZYOFi4S7Z9VJDh7id2kpX5p12gdJb_/file#'
    urllib.request.urlretrieve(url, 'weights.zip')

def unzip_weights():
    with zipfile.ZipFile('weights.zip', 'r') as zip_ref:
        zip_ref.extractall('./')

if __name__ == "__main__":
    print("Downloading weights ... (853 MB)")
    download_weights()
    unzip_weights()
    print("Done")

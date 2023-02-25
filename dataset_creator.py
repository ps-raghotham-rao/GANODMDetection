import urllib.request
import os

# Download URLs for the COCO 2014 dataset
urls = [
    "http://images.cocodataset.org/zips/train2014.zip",
    "http://images.cocodataset.org/zips/val2014.zip",
    "http://images.cocodataset.org/annotations/annotations_trainval2014.zip",
]

# Directory to save the downloaded files
download_dir = "coco_dataset"

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Download each file and save it in the download_dir directory
for url in urls:
    filename = url.split("/")[-1]
    file_path = os.path.join(download_dir, filename)
    if not os.path.exists(file_path):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, file_path)
    else:
        print(f"{filename} already exists.")

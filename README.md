# Using GAN and Simple Copy Paste Augmentation methods to generate ODM Dataset


Abstract:
This research paper proposes a method to increase the size and diversity of datasets for object detection and segmentation tasks using Generative Adversarial Networks (GANs) and data augmentation techniques. The proposed method involves extracting segmented object images of a specific class from existing datasets, training a GAN on this dataset to generate additional images, and blending the generated images with the segmented object images using data augmentation methods. The approach has the potential to improve model performance and reduce the need for manual data labeling.

Prerequisites:
  pip requirements:
    pycocotools
    Pillow
    scikit-image

  Visual Studio and Microsoft C++ Build Tools for installing pycocotools in Windows
  
Steps:

python dataset_creator.py
python extractor.py
python filter.py

Some modifications are required which are explained inside the docs of py files.

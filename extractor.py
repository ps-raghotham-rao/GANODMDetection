import os
import numpy as np
import skimage.io as io
from skimage import exposure


from pycocotools.coco import COCO

#Extract the dataset. The path can be different verify once or else below code will fail.


# path to annotations file
ann_file = 'coco_dataset/annotations/instances_val2014.json'

# initialize COCO api for instance annotations
coco = COCO(ann_file)

# get category id for airplane
cat_ids = coco.getCatIds(catNms=['airplane'])

# get all image ids containing airplane instances
img_ids = coco.getImgIds(catIds=cat_ids)


# create folder for airplane images
airplane_dir = 'airplane_images'
if not os.path.exists(airplane_dir):
    os.makedirs(airplane_dir)

# loop over image ids
for img_id in img_ids:
    # load image
    img_info = coco.loadImgs(img_id)[0]
    img_file = os.path.join('coco_dataset/val2014', img_info['file_name'])
    img = io.imread(img_file)

    # load annotations
    ann_ids = coco.getAnnIds(imgIds=img_id, catIds=cat_ids)
    anns = coco.loadAnns(ann_ids)

    # loop over annotations and extract masks
    masks = []
    for ann in anns:
        mask = coco.annToMask(ann)
        masks.append(mask)

    # combine masks to get final mask
    mask = np.sum(masks, axis=0)

    # apply mask to image
    masked_img = img.copy()
    
    if len(img.shape) == 2:
        masked_img = np.where(mask == 0, 0, img)
    else:
        masked_img[:,:,0] = np.where(mask==0, 0, img[:,:,0])
        masked_img[:,:,1] = np.where(mask==0, 0, img[:,:,1])
        masked_img[:,:,2] = np.where(mask==0, 0, img[:,:,2])

    # apply contrast stretching
    # p2, p98 = np.percentile(masked_img, (2, 98))
    # masked_img = exposure.rescale_intensity(masked_img, in_range=(p2, p98))

    # save masked image
    io.imsave(os.path.join(airplane_dir, img_info['file_name']), masked_img)

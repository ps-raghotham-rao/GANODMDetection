import os
from PIL import Image

# set the path for the folder containing the images
folder_path = 'airplane_images'

# set the path for the folder to save the resized images
resized_folder_path = 'airplane_images1'

# create the resized folder if it does not exist
if not os.path.exists(resized_folder_path):
    os.makedirs(resized_folder_path)

# loop through all the files in the folder
for filename in os.listdir(folder_path):
    # check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # open the image and get its size
        img_path = os.path.join(folder_path, filename)
        with Image.open(img_path) as img:
            try:
                width, height = img.size
                # check if the image is close to the desired size
                if abs(width - 600) <= 200 and abs(height - 480) <= 200:
                    # resize the image to 600x480
                    new_img = img.resize((600, 480))
                    # save the resized image to the resized folder
                    resized_img_path = os.path.join(resized_folder_path, filename)
                    new_img.save(resized_img_path)
                    print(f"{filename} has been resized to 600x480 and saved to {resized_img_path}")
            except:
                print(f"Error processing {filename}")


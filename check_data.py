from PIL import Image
import os.path
import os
from os import listdir

from numpy import imag


def get_min_resolution():
    print("min")


def get_max_resolution():
    print("max")


def get_images_of_category(category, train_images, test_images, valid_images):
    folder_dir = "./flowers"
    valid_dir = folder_dir + "/valid/" + category
    test_dir = folder_dir + "/test/" + category
    train_dir = folder_dir + "/train/" + category
    images = []
    image_sizes = []
    for image in os.listdir(valid_dir):
        if image.endswith(".jpg"):
            img = Image.open(valid_dir + "/" + image)
            image_sizes.append(img.size)
        images.append(image)
        valid_images.append(image)
    for image in os.listdir(test_dir):
        if image.endswith(".jpg"):
            img = Image.open(test_dir + "/" + image)
            image_sizes.append(img.size)
        images.append(image)
        test_images.append(image)
    for image in os.listdir(train_dir):
        if image.endswith(".jpg"):
            img = Image.open(train_dir + "/" + image)
            image_sizes.append(img.size)
        images.append(image)
        train_images.append(image)
    min_tuple_x = min(image_sizes, key=lambda tup: tup[0])
    min_tuple_y = min(image_sizes, key=lambda tup: tup[1])
    max_tuple_x = max(image_sizes, key=lambda tup: tup[0])
    max_tuple_y = max(image_sizes, key=lambda tup: tup[1])
    return len(images), min_tuple_x, min_tuple_y, max_tuple_x, max_tuple_y


# get the path/directory

train_images = []
test_images = []
valid_images = []
for cnt in range(102):
    print("-" * 25)
    print("Category: ", cnt + 1)
    print(get_images_of_category(str(cnt + 1), train_images, test_images, valid_images))

total_images = len(train_images) + len(test_images) + len(valid_images)

print(len(train_images) / total_images)
print(len(test_images) / total_images)
print(len(valid_images) / total_images)

print(total_images)

# print(os.listdir(folder_dir))
# print(os.listdir(valid_dir))
# print(os.listdir(test_dir))
# print(os.listdir(train_dir))


# for images in os.listdir(folder_dir):

#     # check if the image ends with png
#     if images.endswith(".jpg"):
#         img = Image.open(folder_dir + "/" + images)
#         image_sizes.append(img.size)

# min_tuple = min(image_sizes, key=lambda tup: tup[0])
# max_tuple = max(image_sizes, key=lambda tup: tup[0])
# print(min_tuple)
# print(max_tuple)

# min_tuple = min(image_sizes, key=lambda tup: tup[1])
# max_tuple = max(image_sizes, key=lambda tup: tup[1])
# print(min_tuple)
# print(max_tuple)


# filename = os.path.join('')
# img = Image.open(filename)
# print img.size

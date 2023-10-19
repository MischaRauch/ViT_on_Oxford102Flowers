# Final Project for the Deep Learning course at Reykjavik University

## Introduction
This project is a comparison of vision transformers and CNN networks. The vision transformers follows the model described in [An image is worth 16X16 words:
Transformers for image recognition at scale](https://arxiv.org/pdf/2010.11929.pdf).

The 102 Oxford Flower dataset is a diverse and visually stunning collection of flower images, spanning over a hundred categories. Using the ViT architecture, we aim to develop a robust and accurate model for classifying these images into their respective flower species. The ViT model has shown remarkable results in various computer vision tasks, and we're excited to apply it to this dataset.

## Usage
The project has one python-file (check_data.py) and two python-notebooks. 

### check_data.py

The check_data.py provides a summary of the dataset (number of classes, elements per class, smalles and biggest image per class, total number of pictures and size of the train, test and validation-set).
Usage: ```python check_data.py ```

### Notebooks

The notebooks have been trained on dedicated GPUs and both of them use the GPU-optimization. To run it on CPU the code has to be adopted. Minimum requirement is GPU with at least 8GB of RAM. Running the notebooks without any changes trains the model for 500 epochs and stores the progress every 10 epochs. The total time for training is around 6 hours.

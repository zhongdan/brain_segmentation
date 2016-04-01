import numpy as np
import random
from glob import glob
from skimage import io
from sklearn.feature_extraction.image import extract_patches_2d

np.random.seed(5)



def generate_patches(img_path, patch_size=(65,65), num_patches = 10):
    '''
    Generates patches (num_chan, patch_h, patch_w) for an input image
    INPUT:  (1) string 'img_path': path to imput image (png, strip of slices)
            (2) tuple 'patch_size': dimensions of patches to be used in net
            (3) int 'num_patches': number of patches to be generated per slice.
    OUTPUT: (1) list of scan patches: (num_slices * num_patches, num_channels, patch_h, patch_w)
            (2) list of label patches: (num_slices * num_patches, patch_h, patch_w)
    '''
    patches = [] # (num_scans, num_patches, num_chan, patch_h, patch_w)
    patch_labels = [] # (num_scans, num_patches, patch_h, patch_w)
    patch_lst = [] # list of lists: patches for each slice (same idxs)
    slices = io.imread(img_path).reshape(5,240,240) # (chan + gt, h, w)
    for img in slices:
        patch_list.append(extract_patches_2d(img, patch_size, max_patches = num_patches, random_state=5)) #set rs for same patch ix among modes
    patches.append(zip(patch_list[0], patch_lst[1], patch_lst[2], patch_lst[3]))
    self.patch_labels.append(patch_list[-1])



    # for slice_strip in self.normed_slices: # slice = strip of 5 images
    #     slices = slice_strip.reshape(5,240,240)
        # for img in slices:
        #     # get list of patches corresponding to each image in slices
        #     patch_list.append(extract_patches_2d(img, patch_size, max_patches = num_patches, random_state=5)) #set rs for same patch ix among modes
        # self.patches.append(zip(patch_list[0], patch_list[1], patch_list[2], patch_list[3]))
        # self.patch_labels.append(patch_list[-1])

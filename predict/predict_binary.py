#coding:utf8
""""
    This is main procedure for remote sensing image semantic segmentation

"""
import cv2
import numpy as np
import os
import sys
import gc
import argparse
# from keras.preprocessing.image import img_to_array
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from PIL import Image
from keras.preprocessing.image import img_to_array

from keras import backend as K
K.set_image_dim_ordering('tf')
K.clear_session()

from base_predict_functions import orignal_predict, smooth_predict_for_binary
from ulitities.base_functions import load_img_normalization
from smooth_tiled_predictions import predict_img_with_smooth_windowing_multiclassbands
# from semantic_segmentation_networks import jaccard_coef,jaccard_coef_int

"""
   The following global variables should be put into meta data file 
"""
os.environ["CUDA_VISIBLE_DEVICES"] = "5"


target_class =1

window_size = 256
# step = 128

dict_network={0: 'unet', 1: 'fcnnet', 2: 'segnet'}
dict_target={0: 'roads', 1: 'buildings'}
FLAG_USING_NETWORK = 0  # 0:unet; 1:fcn; 2:segnet;

FLAG_TARGET_CLASS = 0  # 0:roads; 1:buildings

FLAG_APPROACH_PREDICT = 0 # 0: original predict, 1: smooth predict

# img_file = '../../data/test/GF2_yilong11.png'
# img_file = '../../data/test/sample1.png'
img_file = '../../data/test/sample1_nrg.png'

model_file = ''.join(['../../data/models/sat_urban_nrg/',dict_network[FLAG_USING_NETWORK], '_', dict_target[FLAG_TARGET_CLASS],'_binary2.h5'])
# model_file = '/home/omnisky/PycharmProjects/data/models/sat_urban_rgb/unet_roads_binary_jaccard_t2.h5'
print("model: {}".format(model_file))

if __name__ == '__main__':

    print("[INFO] opening image...")
    ret, input_img = load_img_normalization(img_file)
    if ret !=0:
        print("Open input file failed: {}".format(img_file))
        sys.exit(-1)

    abs_filename = os.path.split(img_file)[1]
    abs_filename = abs_filename.split(".")[0]
    print (abs_filename)

    """checke model file"""
    print("model file: {}".format(model_file))
    if not os.path.isfile(model_file):
        print("model does not exist:{}".format(model_file))
        sys.exit(-2)

    model = load_model(model_file)

    if FLAG_APPROACH_PREDICT==0:
        print("[INFO] predict image by orignal approach\n")
        result = orignal_predict(input_img, model, window_size)
        output_file = ''.join(['../../data/predict/original_predict_',abs_filename, '.png'])
        print("result save as to: {}".format(output_file))
        cv2.imwrite(output_file, result*100)

    elif FLAG_APPROACH_PREDICT==1:
        print("[INFO] predict image by smooth approach\n")
        result = predict_img_with_smooth_windowing_multiclassbands(
            input_img,
            model,
            window_size=window_size,
            subdivisions=2,
            real_classes=target_class,  # output channels = 是真的类别，总类别-背景
            pred_func=smooth_predict_for_binary
        )
        output_file = ''.join(['../../data/predict/', dict_network[FLAG_USING_NETWORK],'/mask_binary_',
                               abs_filename, '_', dict_target[FLAG_TARGET_CLASS],'.png'])
        print("result save as to: {}".format(output_file))

        cv2.imwrite(output_file, result)

    gc.collect()



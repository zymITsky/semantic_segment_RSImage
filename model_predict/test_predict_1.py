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
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder


from keras import backend as K
K.set_image_dim_ordering('tf')
K.clear_session()
from segmentation_models.losses import bce_jaccard_loss
from segmentation_models.metrics import iou_score

from base_predict_functions import orignal_predict_notonehot, smooth_predict_for_binary_notonehot
from ulitities.base_functions import load_img_normalization_by_cv2, load_img_by_gdal, UINT10,UINT8,UINT16
from predict_backbone import predict_img_with_smooth_windowing_multiclassbands

"""
   The following global variables should be put into meta data file 
"""
os.environ["CUDA_VISIBLE_DEVICES"] = "5"

target_class =1

window_size = 288
# step = 128

im_bands =3
im_type = UINT8  # UINT10,UINT8,UINT16
dict_network={0: 'unet', 1: 'fcnnet', 2: 'segnet'}
dict_target={0: 'roads', 1: 'buildings'}
FLAG_USING_NETWORK = 0  # 0:unet; 1:fcn; 2:segnet;

FLAG_TARGET_CLASS = 0  # 0:roads; 1:buildings

FLAG_APPROACH_PREDICT = 1 # 0: original predict, 1: smooth predict

# position = 'tongchuan_test' #  1)jian11_test, , 2)jiangyou, 3)yujiang_test,
# 4)cuiping, 5)shuangliu_1test, 6) tongchuan_test
# 7) lizhou_test, 8) jianyang, 9)yushui22_test, 10) sample1, 11)ruoergai_52test
# img_file = '../../data/test/sat_test/'+position+'_4bands1024.png'  # _rgb, _nrg, __4bands1024.
# img_file = '../../data/test/paper/images/'+position+'_4bands1024.png'  # _rgb, _nrg, _4bands1024.
img_file = '/home/omnisky/PycharmProjects/data/test/rice/normal/testsrc_1.png'

# model_file = ''.join(['../../data/models/sat_urban_4bands/',dict_network[FLAG_USING_NETWORK], '_',
#                       dict_target[FLAG_TARGET_CLASS],'_binary_notonehot_final.h5'])

model_file = '/home/omnisky/PycharmProjects/data/models/rice/PSPnet_test_resnet34_2019-03-27_14-45-13.h5'
# print("model: {}".format(model_file))

if __name__ == '__main__':

    print("[INFO] opening image...")

    input_img = load_img_by_gdal(img_file)
    if im_type == UINT8:
        input_img = input_img / 255.0
    elif im_type == UINT10:
        input_img = input_img / 1024.0
    elif im_type == UINT16:
        input_img = input_img / 65535.0

    input_img = np.clip(input_img, 0.0, 1.0)
    input_img = input_img.astype(np.float32)


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
        result = orignal_predict_notonehot(input_img,im_bands, model, window_size)
        output_file = ''.join(['../../data/predict/',dict_network[FLAG_USING_NETWORK],'/sat_4bands/original_pred_',
                               abs_filename, '_', dict_target[FLAG_TARGET_CLASS],'_notonehot.png'])
        print("result save as to: {}".format(output_file))
        cv2.imwrite(output_file, result*128)

    elif FLAG_APPROACH_PREDICT==1:
        print("[INFO] predict image by smooth approach\n")
        result = predict_img_with_smooth_windowing_multiclassbands(
            input_img,
            model,
            window_size=window_size,
            subdivisions=2,
            real_classes=target_class,  # output channels = 是真的类别，总类别-背景
            pred_func=smooth_predict_for_binary_notonehot
        )
        """for single class test"""
        result[result<128]=0
        result[result>=128]=1
        # output_file = '//home/omnisky/PycharmProjects/data/test/shuidao/GF2shuitian22_test_pred.png'

        # output_file = ''.join(['../../data/predict/', dict_network[FLAG_USING_NETWORK],'/sat_4bands/mask_binary_',
        #                        abs_filename, '_', dict_target[FLAG_TARGET_CLASS],'_notonehot.png'])

        # output_file = ''.join(['../../data/test/paper/pred/mask_binary_',
        #                        abs_filename, '_', dict_target[FLAG_TARGET_CLASS], '_notonehot.png'])
        output_file = '/home/omnisky/PycharmProjects/data/test/rice/newpred/test_1_pspnet_resnet34_cross.png'

        print("result save as to: {}".format(output_file))



        cv2.imwrite(output_file, result)

    gc.collect()



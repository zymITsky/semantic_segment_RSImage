# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrainBinaryCommon.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_train_binary_common(object):
    def setupUi(self, Dialog_train_binary_common):
        Dialog_train_binary_common.setObjectName("Dialog_train_binary_common")
        Dialog_train_binary_common.resize(529, 341)
        self.layoutWidget = QtWidgets.QWidget(Dialog_train_binary_common)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 521, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_network = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_network.setMinimumSize(QtCore.QSize(0, 63))
        self.groupBox_network.setMaximumSize(QtCore.QSize(16777215, 66))
        self.groupBox_network.setObjectName("groupBox_network")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_network)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.radioButton_unet = QtWidgets.QRadioButton(self.groupBox_network)
        self.radioButton_unet.setChecked(True)
        self.radioButton_unet.setObjectName("radioButton_unet")
        self.horizontalLayout_10.addWidget(self.radioButton_unet)
        self.radioButton_fcnnet = QtWidgets.QRadioButton(self.groupBox_network)
        self.radioButton_fcnnet.setObjectName("radioButton_fcnnet")
        self.horizontalLayout_10.addWidget(self.radioButton_fcnnet)
        self.radioButton_segnet = QtWidgets.QRadioButton(self.groupBox_network)
        self.radioButton_segnet.setObjectName("radioButton_segnet")
        self.horizontalLayout_10.addWidget(self.radioButton_segnet)
        self.horizontalLayout_7.addWidget(self.groupBox_network)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_7.addWidget(self.line_3)
        self.groupBox_network_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_network_3.setMinimumSize(QtCore.QSize(0, 63))
        self.groupBox_network_3.setMaximumSize(QtCore.QSize(16777215, 66))
        self.groupBox_network_3.setObjectName("groupBox_network_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.groupBox_network_3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.radioButton_cross_entropy = QtWidgets.QRadioButton(self.groupBox_network_3)
        self.radioButton_cross_entropy.setChecked(True)
        self.radioButton_cross_entropy.setObjectName("radioButton_cross_entropy")
        self.horizontalLayout_15.addWidget(self.radioButton_cross_entropy)
        self.radioButton_jaccard = QtWidgets.QRadioButton(self.groupBox_network_3)
        self.radioButton_jaccard.setObjectName("radioButton_jaccard")
        self.horizontalLayout_15.addWidget(self.radioButton_jaccard)
        self.radioButton_jaccard_crossentropy = QtWidgets.QRadioButton(self.groupBox_network_3)
        self.radioButton_jaccard_crossentropy.setObjectName("radioButton_jaccard_crossentropy")
        self.horizontalLayout_15.addWidget(self.radioButton_jaccard_crossentropy)
        self.horizontalLayout_7.addWidget(self.groupBox_network_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(55, 23))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lineEdit_basemodel = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_basemodel.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_basemodel.setObjectName("lineEdit_basemodel")
        self.horizontalLayout_6.addWidget(self.lineEdit_basemodel)
        self.pushButton_basemodel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_basemodel.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_basemodel.setObjectName("pushButton_basemodel")
        self.horizontalLayout_6.addWidget(self.pushButton_basemodel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.comboBox_gupid = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_gupid.setObjectName("comboBox_gupid")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_gupid)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spinBox_BS = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_BS.sizePolicy().hasHeightForWidth())
        self.spinBox_BS.setSizePolicy(sizePolicy)
        self.spinBox_BS.setMinimumSize(QtCore.QSize(47, 22))
        self.spinBox_BS.setMaximumSize(QtCore.QSize(16777215, 22))
        self.spinBox_BS.setMinimum(1)
        self.spinBox_BS.setMaximum(1000)
        self.spinBox_BS.setProperty("value", 16)
        self.spinBox_BS.setObjectName("spinBox_BS")
        self.horizontalLayout_5.addWidget(self.spinBox_BS)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spinBox_epoch = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_epoch.sizePolicy().hasHeightForWidth())
        self.spinBox_epoch.setSizePolicy(sizePolicy)
        self.spinBox_epoch.setMinimumSize(QtCore.QSize(47, 22))
        self.spinBox_epoch.setMaximumSize(QtCore.QSize(16777215, 22))
        self.spinBox_epoch.setMinimum(1)
        self.spinBox_epoch.setMaximum(1000)
        self.spinBox_epoch.setProperty("value", 3)
        self.spinBox_epoch.setObjectName("spinBox_epoch")
        self.horizontalLayout_5.addWidget(self.spinBox_epoch)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(55, 23))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_traindata_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_traindata_path.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_traindata_path.setObjectName("lineEdit_traindata_path")
        self.horizontalLayout.addWidget(self.lineEdit_traindata_path)
        self.pushButton_trainpath = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_trainpath.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_trainpath.setObjectName("pushButton_trainpath")
        self.horizontalLayout.addWidget(self.pushButton_trainpath)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.spinBox_bands = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_bands.sizePolicy().hasHeightForWidth())
        self.spinBox_bands.setSizePolicy(sizePolicy)
        self.spinBox_bands.setMinimumSize(QtCore.QSize(47, 22))
        self.spinBox_bands.setMaximumSize(QtCore.QSize(16777215, 22))
        self.spinBox_bands.setMinimum(1)
        self.spinBox_bands.setMaximum(1000)
        self.spinBox_bands.setProperty("value", 3)
        self.spinBox_bands.setObjectName("spinBox_bands")
        self.horizontalLayout_4.addWidget(self.spinBox_bands)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.comboBox_dtype = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_dtype.setObjectName("comboBox_dtype")
        self.comboBox_dtype.addItem("")
        self.comboBox_dtype.addItem("")
        self.comboBox_dtype.addItem("")
        self.comboBox_dtype.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_dtype)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(33, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox_windsize = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.spinBox_windsize.sizePolicy().hasHeightForWidth())
        self.spinBox_windsize.setSizePolicy(sizePolicy)
        self.spinBox_windsize.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_windsize.setMaximumSize(QtCore.QSize(50, 23))
        self.spinBox_windsize.setMaximum(1000)
        self.spinBox_windsize.setSingleStep(2)
        self.spinBox_windsize.setProperty("value", 256)
        self.spinBox_windsize.setObjectName("spinBox_windsize")
        self.horizontalLayout_4.addWidget(self.spinBox_windsize)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_3.addWidget(self.label_21)
        self.lineEdit_class_name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_class_name.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_class_name.setObjectName("lineEdit_class_name")
        self.horizontalLayout_3.addWidget(self.lineEdit_class_name)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_3.addWidget(self.label_19)
        self.spinBox_label_value = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_label_value.setMinimum(1)
        self.spinBox_label_value.setProperty("value", 1)
        self.spinBox_label_value.setObjectName("spinBox_label_value")
        self.horizontalLayout_3.addWidget(self.spinBox_label_value)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(55, 23))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_savemodel = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_savemodel.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_savemodel.setObjectName("lineEdit_savemodel")
        self.horizontalLayout_2.addWidget(self.lineEdit_savemodel)
        self.pushButton_savemodel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_savemodel.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_savemodel.setObjectName("pushButton_savemodel")
        self.horizontalLayout_2.addWidget(self.pushButton_savemodel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_train_binary_common)
        self.pushButton_basemodel.clicked.connect(Dialog_train_binary_common.slot_basemodel)
        self.pushButton_trainpath.clicked.connect(Dialog_train_binary_common.slot_traindatapath)
        self.pushButton_savemodel.clicked.connect(Dialog_train_binary_common.slot_savemodelpath)
        self.buttonBox.accepted.connect(Dialog_train_binary_common.slot_ok)
        self.buttonBox.rejected.connect(Dialog_train_binary_common.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_train_binary_common)

    def retranslateUi(self, Dialog_train_binary_common):
        _translate = QtCore.QCoreApplication.translate
        Dialog_train_binary_common.setWindowTitle(_translate("Dialog_train_binary_common", "Dialog"))
        self.groupBox_network.setTitle(_translate("Dialog_train_binary_common", "Network"))
        self.radioButton_unet.setText(_translate("Dialog_train_binary_common", "Unet"))
        self.radioButton_fcnnet.setText(_translate("Dialog_train_binary_common", "Fcnnet"))
        self.radioButton_segnet.setText(_translate("Dialog_train_binary_common", "Segnet"))
        self.groupBox_network_3.setTitle(_translate("Dialog_train_binary_common", "Target function"))
        self.radioButton_cross_entropy.setText(_translate("Dialog_train_binary_common", "Crossentropy"))
        self.radioButton_jaccard.setText(_translate("Dialog_train_binary_common", "Jaccard"))
        self.radioButton_jaccard_crossentropy.setText(_translate("Dialog_train_binary_common", "Jaccard+Cross"))
        self.label_4.setText(_translate("Dialog_train_binary_common", "base model:"))
        self.pushButton_basemodel.setText(_translate("Dialog_train_binary_common", "Open"))
        self.label_10.setText(_translate("Dialog_train_binary_common", "GPU ID:"))
        self.comboBox_gupid.setItemText(0, _translate("Dialog_train_binary_common", "0"))
        self.comboBox_gupid.setItemText(1, _translate("Dialog_train_binary_common", "1"))
        self.comboBox_gupid.setItemText(2, _translate("Dialog_train_binary_common", "2"))
        self.comboBox_gupid.setItemText(3, _translate("Dialog_train_binary_common", "3"))
        self.comboBox_gupid.setItemText(4, _translate("Dialog_train_binary_common", "4"))
        self.comboBox_gupid.setItemText(5, _translate("Dialog_train_binary_common", "5"))
        self.label_5.setText(_translate("Dialog_train_binary_common", "batch size:"))
        self.label_7.setText(_translate("Dialog_train_binary_common", "epoch:"))
        self.label.setText(_translate("Dialog_train_binary_common", "traindata path:"))
        self.pushButton_trainpath.setText(_translate("Dialog_train_binary_common", "Open"))
        self.label_8.setText(_translate("Dialog_train_binary_common", "bands:"))
        self.label_9.setText(_translate("Dialog_train_binary_common", "dtype:"))
        self.comboBox_dtype.setItemText(0, _translate("Dialog_train_binary_common", "uint8"))
        self.comboBox_dtype.setItemText(1, _translate("Dialog_train_binary_common", "uint10"))
        self.comboBox_dtype.setItemText(2, _translate("Dialog_train_binary_common", "uint16"))
        self.comboBox_dtype.setItemText(3, _translate("Dialog_train_binary_common", "float"))
        self.label_3.setText(_translate("Dialog_train_binary_common", "windsize :"))
        self.groupBox.setTitle(_translate("Dialog_train_binary_common", "Target information"))
        self.label_21.setText(_translate("Dialog_train_binary_common", "class name:"))
        self.lineEdit_class_name.setText(_translate("Dialog_train_binary_common", "Roads"))
        self.label_19.setText(_translate("Dialog_train_binary_common", "label value:"))
        self.label_6.setText(_translate("Dialog_train_binary_common", "model save path:"))
        self.pushButton_savemodel.setText(_translate("Dialog_train_binary_common", "Open"))


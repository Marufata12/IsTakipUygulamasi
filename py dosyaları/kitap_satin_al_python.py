# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kitap_satin_al.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(859, 461)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(160, 30, 461, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(60, 200, 47, 13))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(40, 20, 361, 221))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.id_label = QtWidgets.QLabel(self.widget)
        self.id_label.setObjectName("id_label")
        self.gridLayout.addWidget(self.id_label, 0, 0, 1, 1)
        self.id_line_edit = QtWidgets.QLineEdit(self.widget)
        self.id_line_edit.setObjectName("id_line_edit")
        self.gridLayout.addWidget(self.id_line_edit, 0, 1, 1, 1)
        self.kitap_adi_label = QtWidgets.QLabel(self.widget)
        self.kitap_adi_label.setObjectName("kitap_adi_label")
        self.gridLayout.addWidget(self.kitap_adi_label, 1, 0, 1, 1)
        self.kitap_adi_line_edit = QtWidgets.QLineEdit(self.widget)
        self.kitap_adi_line_edit.setObjectName("kitap_adi_line_edit")
        self.gridLayout.addWidget(self.kitap_adi_line_edit, 1, 1, 1, 1)
        self.ad_soyad_label = QtWidgets.QLabel(self.widget)
        self.ad_soyad_label.setObjectName("ad_soyad_label")
        self.gridLayout.addWidget(self.ad_soyad_label, 2, 0, 1, 1)
        self.ad_soyad_line_Edit = QtWidgets.QLineEdit(self.widget)
        self.ad_soyad_line_Edit.setObjectName("ad_soyad_line_Edit")
        self.gridLayout.addWidget(self.ad_soyad_line_Edit, 2, 1, 1, 1)
        self.adres_label = QtWidgets.QLabel(self.widget)
        self.adres_label.setObjectName("adres_label")
        self.gridLayout.addWidget(self.adres_label, 3, 0, 1, 1)
        self.adres_line_Edit = QtWidgets.QLineEdit(self.widget)
        self.adres_line_Edit.setObjectName("adres_line_Edit")
        self.gridLayout.addWidget(self.adres_line_Edit, 3, 1, 1, 1)
        self.fiyat_label = QtWidgets.QLabel(self.widget)
        self.fiyat_label.setObjectName("fiyat_label")
        self.gridLayout.addWidget(self.fiyat_label, 4, 0, 1, 1)
        self.fiyat_line_edit = QtWidgets.QLineEdit(self.widget)
        self.fiyat_line_edit.setObjectName("fiyat_line_edit")
        self.gridLayout.addWidget(self.fiyat_line_edit, 4, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(160, 330, 461, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.satin_al_buton = QtWidgets.QPushButton(self.frame_2)
        self.satin_al_buton.setGeometry(QtCore.QRect(130, 20, 201, 31))
        self.satin_al_buton.setObjectName("satin_al_buton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.id_label.setText(_translate("Form", "ID"))
        self.kitap_adi_label.setText(_translate("Form", "Kitap Adı"))
        self.ad_soyad_label.setText(_translate("Form", "Ad-Soyad"))
        self.adres_label.setText(_translate("Form", "Adres"))
        self.fiyat_label.setText(_translate("Form", "Fiyat"))
        self.satin_al_buton.setText(_translate("Form", "Satın Al"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

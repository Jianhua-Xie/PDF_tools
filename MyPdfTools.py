#!/usr/bin/env python
# coding=utf-8

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QMainWindow,QFileDialog

class MyPdf(QMainWindow):
    def __init__(self):
        super(MyPdf, self).__init__()
        print('创建一个pdf对象')

    def getfile(self):
        self.fileName, self.filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "PDF Files (*.pdf)")
        fileinfo = QFileInfo(self.fileName)
        self.file_path = fileinfo.absolutePath()
        if self.file_path != '':
            self.getNumPages()

    def getNumPages(self):
        fp_read_file = open(self.fileName, 'rb')
        self.pdf_input = PdfFileReader(fp_read_file)  # 将要分割的PDF内容格式话
        self.page_count = self.pdf_input.getNumPages()  # 获取PDF页数
        # print("该文件共有{}页".format(page_count))  # 打印页数

    def splitpdf(self, split_lists):
        for split_list in split_lists:
            pdf_output = PdfFileWriter()  # 实例一个 PDF文件编写器
            for i in range(split_list[0]-1, split_list[1]):
                pdf_output.addPage(self.pdf_input.getPage(i))
            with open(split_list[2], 'wb') as sub_fp:
                pdf_output.write(sub_fp)
        print('拆分文件完成')

    def merge(self, file_lists, new_filename):
        merger = PdfFileMerger()
        for file in file_lists:  # 从所有文件中选出pdf文件合并
            merger.append(open(file, 'rb'))
        with open(new_filename, 'wb') as fout:  # 输出文件为newfile.pdf
            merger.write(fout)
        print('合并文件完成')


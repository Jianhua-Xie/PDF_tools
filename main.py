import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QFileInfo, QPersistentModelIndex
from MyPdfTools import *
from CommonHelper import *

class MyMainWin(QMainWindow):
    def __init__(self):
        super(MyMainWin,self).__init__()

        self.mypdf = MyPdf()
        self.widget1 = Win1()
        self.widget2 = Win2()
        self.widget3 = Win3()

        self.init_ui()

        self.setStyleSheet("background-color:#FFFFFF;")

    def init_ui(self):
        '''
        初始化整体布局
        '''
        #设置主窗口标题
        self.setWindowTitle('PDF工具')
        #设置窗口尺寸
        self.resize(800,400)
        self.setMinimumSize(500,400)

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_layout = QGridLayout()  # 创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)  # 将主部件设置为网格布局

        self.main_layout.addWidget(self.widget1)
        self.main_layout.addWidget(self.widget2)
        self.main_layout.addWidget(self.widget3)

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        # self.widget1.show()
        # self.widget1.hide()
        self.widget2.hide()
        self.widget3.hide()

        # #添加切换窗口的槽函数
        self.widget1.button1.clicked.connect(lambda: self.JumpPage(self.widget1, self.widget2))
        self.widget1.button2.clicked.connect(lambda: self.JumpPage(self.widget1, self.widget3))
        self.widget2.button1.clicked.connect(lambda: self.JumpPage(self.widget2, self.widget1))
        self.widget3.button1.clicked.connect(lambda: self.JumpPage(self.widget3, self.widget1))
        #
        self.centerwin()


    def JumpPage(self, a, b):
        a.hide()
        b.show()

    def centerwin(self):
        # 获取屏幕坐标系
        screensize = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        winsize = self.geometry()

        print('屏幕宽度', screensize.width())
        new_x = (screensize.width() - winsize.width()) / 2
        new_y = (screensize.height() - winsize.height()) / 2

        self.move(new_x, new_y)

class Win1(QWidget):

    def __init__(self):
        super(Win1,self).__init__()
        self.init_ui()

        styleFile = './ui/style1.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        self.setStyleSheet(qssStyle)

    def init_ui(self):

        self.label1 = QLabel()
        self.label1.setPixmap(QPixmap("./ui/拆分pdf.PNG"))
        # self.label1.setScaledContents(True)  # 完全填充
        # # 设置居中对齐
        self.label1.setAlignment(Qt.AlignCenter)

        self.button1 = QPushButton()
        self.button1.setText('PDF拆分')
        self.button1.setMinimumSize(100,50)

        self.vbox1 = QVBoxLayout()
        self.vbox1.addWidget(self.label1)
        self.vbox1.addWidget(self.button1)

        self.label2 = QLabel()
        self.label2.setPixmap(QPixmap("./ui/合并pdf.PNG"))
        # self.label2.setScaledContents(True)  # 完全填充
        # 设置居中对齐
        self.label2.setAlignment(Qt.AlignCenter)

        self.button2 = QPushButton()
        self.button2.setText('PDF合并')
        self.button2.setMinimumSize(100, 50)

        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.label2)
        self.vbox2.addWidget(self.button2)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox1)
        self.hbox.addLayout(self.vbox2)
        self.setLayout(self.hbox)

class Win2(QWidget):

    def __init__(self):
        super(Win2,self).__init__()
        self.mypdf = MyPdf()
        self.init_ui()

        styleFile = './ui/style2.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        self.setStyleSheet(qssStyle)

    def init_ui(self):

        self.button2 = QPushButton(self)
        self.button2.setText('选择文件')
        self.button2.setProperty("level", "2")

        self.lineedit1 = QLineEdit()
        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.lineedit1)
        self.hbox1.addWidget(self.button2)

        self.button3 = QPushButton(self)
        self.button3.setText('PDF分割')
        self.button3.setProperty("level", "1")

        self.button1 = QPushButton(self)
        self.button1.setText('返回')
        self.button1.setProperty("level", "1")

        # 设置复选框
        self.radiobutton1 = QRadioButton(self)
        self.radiobutton1.setText('单页分割')

        self.radiobutton2 = QRadioButton(self)
        self.radiobutton2.setText('平均分割')

        self.lineedit21 = QLineEdit(self)
        self.label21 = QLabel(self)
        self.label21.setText('个文档')

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.lineedit21)
        self.hbox2.addWidget(self.label21)

        self.radiobutton3 = QRadioButton(self)
        self.radiobutton3.setText('固定页分割')

        self.label31 = QLabel(self, )
        self.label31.setText('每')

        self.lineedit31 = QLineEdit(self)

        self.label32 = QLabel(self)
        self.label32.setText('页一个文档')

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.label31)
        self.hbox3.addWidget(self.lineedit31)
        self.hbox3.addWidget(self.label32)

        self.radiobutton4 = QRadioButton(self)
        self.radiobutton4.setText('自定义分割')
        self.lineedit41 = QLineEdit(self)

        self.button41 = QPushButton(self)
        self.button41.setText('提取文件')
        self.button41.setProperty("level", "2")

        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.lineedit41)
        self.hbox4.addWidget(self.button41)

        # 设置网格布局
        self.fromlayout = QFormLayout()
        self.fromlayout.addRow(self.radiobutton1, )
        self.fromlayout.addRow(self.radiobutton2, self.hbox2)
        self.fromlayout.addRow(self.radiobutton3, self.hbox3)
        self.fromlayout.addRow(self.radiobutton4, self.hbox4)

        #********选择输出文件夹********
        self.label51 = QLabel('输出位置：')
        self.lineedit51 = QLineEdit()
        self.button51 = QPushButton('选择文件夹')
        self.button51.setProperty("level", "2")

        self.hbox5 = QHBoxLayout()
        self.hbox5.addWidget(self.label51)
        self.hbox5.addWidget(self.lineedit51)
        self.hbox5.addWidget(self.button51)

        # 整体垂直布局
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.fromlayout)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addWidget(self.button3)
        self.vbox.addWidget(self.button1)

        self.setLayout(self.vbox)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
        self.button41.clicked.connect(self.button41_clicked)
        self.button51.clicked.connect(self.button51_clicked)

        # 将单选框分组，连接到槽函数
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.radiobutton1, 1)
        self.bg1.addButton(self.radiobutton2, 2)
        self.bg1.addButton(self.radiobutton3, 3)
        self.bg1.addButton(self.radiobutton4, 4)
        self.bg1.buttonClicked.connect(self.rbclicked)

    def button2_clicked(self):
        '''选择文件'''
        self.mypdf.getfile()
        if self.mypdf.fileName != '':
            self.lineedit1.setText(self.mypdf.fileName)
            self.lineedit51.setText(self.mypdf.file_path)

    def rbclicked(self):
        #检测哪个单选框被按下
        self.rb_id = self.bg1.checkedId()
        # print(self.rb_id)

    def button3_clicked(self):
        split_lists = []
        new_file_path = self.lineedit51.text()
        print(new_file_path)
        if self.rb_id == 1:         #单页分割
            for i in range(1, self.mypdf.page_count + 1):
                ifilename = new_file_path + '/' + str(i) + '-' + str(i) + '.PDF'
                split_row_list = [i, i, ifilename]
                split_lists.append(split_row_list)
        elif self.rb_id == 2:           #平均分割
            k = int(self.lineedit21.text())                #份数
            ipage_count = self.mypdf.page_count//k         #每份页数
            for i in range(1, k+1):
                firstnum = 1 + (i-1) * ipage_count
                endnum = firstnum + ipage_count - 1
                ifilename = new_file_path + '/' + str(firstnum) + '-' + str(endnum) + '.PDF'
                split_row_list = [firstnum, endnum, ifilename]
                split_lists.append(split_row_list)
            if self.mypdf.page_count % k > 0:       #余数部分
                firstnum = endnum + 1
                endnum = self.mypdf.page_count
                ifilename = new_file_path + '/' + str(firstnum) + '-' + str(endnum) + '.PDF'
                split_row_list = [firstnum, endnum, ifilename]
                split_lists.append(split_row_list)
        elif self.rb_id == 3:  # 固定页分割
            ipage_count = int(self.lineedit31.text())  # 每份页数
            k = self.mypdf.page_count//ipage_count             #份数
            for i in range(1, k+1):
                firstnum = 1 + (i-1) * ipage_count
                endnum = firstnum + ipage_count - 1
                ifilename = new_file_path + '/' + str(firstnum) + '-' + str(endnum) + '.PDF'
                split_row_list = [firstnum, endnum, ifilename]
                split_lists.append(split_row_list)
            if self.mypdf.page_count % ipage_count > 0:  # 余数部分
                firstnum = endnum + 1
                endnum = self.mypdf.page_count
                ifilename = new_file_path + '/' + str(firstnum) + '-' + str(endnum) + '.PDF'
                split_row_list = [firstnum, endnum, ifilename]
                split_lists.append(split_row_list)
        elif self.rb_id == 4:  # 自定义分割 ‘1-5 测试1， 6-8 测试2’
            a = self.lineedit41.text().replace('，', ',')
            split_row_strs = []
            while True:
                k = a.find(',')
                if k != -1:
                    split_row_strs.append(a[:k].strip())
                    a = a[k + 1:]
                else:
                    split_row_strs.append(a.strip())
                    break
            for split_row_str in split_row_strs:
                    m = split_row_str.find(' ')
                    if m != -1:
                        ifilename = new_file_path + '/' + split_row_str[m+1:] + '.PDF'
                        split_row_str = split_row_str[:m]
                    else:
                        ifilename = new_file_path + '/' + split_row_str + '.PDF'
                    n = split_row_str.find('-')
                    firstnum = int(split_row_str[:n])
                    endnum = int(split_row_str[n+1:])
                    split_row_list = [firstnum, endnum, ifilename]
                    split_lists.append(split_row_list)

        for i in split_lists:
            print(i)

        self.mypdf.splitpdf(split_lists)

    def button41_clicked(self):
        self.txt_FileName, self.txt_filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "TXT Files (*.txt)")
        with open(self.txt_FileName, 'r', True, 'utf-8')as fp:
            txt = fp.readlines()
            str = ''
            for detail in txt:
                detail = detail.replace('\n', '')
                if str == '':
                    str = detail
                else:
                    str = str + ',' + detail
        self.lineedit41.setText(str)

    def button51_clicked(self):
        '''选择文件夹'''
        path = QFileDialog.getExistingDirectory()
        if path:
            self.lineedit51.setText(path)

class Win3(QWidget):

    def __init__(self):
        super(Win3,self).__init__()
        self.mypdf = MyPdf()
        self.init_ui()
        styleFile = './ui/style2.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        self.setStyleSheet(qssStyle)

    def init_ui(self):
        self.button1 = QPushButton(self)
        self.button1.setText('返回')
        self.button1.setProperty("level", "1")

        # 设置数据层次结构，4行4列
        self.model = QStandardItemModel(0, 2)
        # #设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['序号', '文件名称'])

        # 实例化表格视图，设置模型为自定义的模型
        self.tableView = QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使表宽度自适应
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)  # 第0列根据文字调节
        self.tableView.verticalHeader().setVisible(False)  # 隐藏列表头
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选中模式为选中行
        self.tableView.setStyleSheet("selection-background-color:rgb(91,155,213)")  # 高亮显示选中的行

        self.button11 = QPushButton(self)
        self.button11.setText('+')
        self.button12 = QPushButton(self)
        self.button12.setText('-')
        self.button13 = QPushButton(self)
        self.button13.setText('上移')
        self.button14 = QPushButton(self)
        self.button14.setText('下移')

        self.button11.setProperty("level", "2")
        self.button12.setProperty("level", "2")
        self.button13.setProperty("level", "2")
        self.button14.setProperty("level", "2")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.button11)
        self.hbox.addWidget(self.button12)
        self.hbox.addWidget(self.button13)
        self.hbox.addWidget(self.button14)

        self.button2 = QPushButton(self)
        self.button2.setText('合并PDF')
        self.button2.setProperty("level", "1")

        self.label1 = QLabel(self)
        self.label1.setText('输出文件名：')
        self.lineedit1 = QLineEdit(self)
        self.button3 = QPushButton(self)
        self.button3.setText('选择文件夹')
        self.button3.setProperty("level", "2")
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.label1)
        self.hbox2.addWidget(self.lineedit1)
        self.hbox2.addWidget(self.button3)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.tableView)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.button2)
        self.vbox.addWidget(self.button1)
        self.setLayout(self.vbox)

        self.button11.clicked.connect(self.button11_clicked)
        self.button12.clicked.connect(self.button12_clicked)
        self.button13.clicked.connect(self.button13_clicked)
        self.button14.clicked.connect(self.button14_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)

    def button11_clicked(self):
        '''添加文件'''
        self.mypdf.file_lists = QFileDialog.getOpenFileNames(self, "选择文件", "/", "PDF Files (*.pdf)")[0]
        # print(self.mypdf.file_lists)
        # print(range(len(self.mypdf.file_lists)))
        for i in range(len(self.mypdf.file_lists)):
            row = self.model.rowCount()
            self.model.insertRow(row)   #插入一行
            item = QStandardItem(str(row+1))
            self.model.setItem(row, 0, item)
            item = QStandardItem(self.mypdf.file_lists[i])
            self.model.setItem(row, 1, item)

    def button12_clicked(self):
        '''删除选中的行'''
        row = self.tableView.currentIndex().row()
        self.model.removeRow(int(row))

    def button13_clicked(self):
        '''向上移动行'''
        row = self.tableView.currentIndex().row()
        if row > 0 :
            str1 = self.model.item(row, 1).text()
            str2 = self.model.item(row-1, 1).text()

            self.model.setItem(row, 1,  QStandardItem(str2))
            self.model.setItem(row-1, 1,  QStandardItem(str1))
        self.tableView.selectRow(row-1)

    def button14_clicked(self):
        '''向下移动行'''
        maxrow = self.model.rowCount() - 1
        row = self.tableView.currentIndex().row()
        if row < maxrow:
            str1 = self.model.item(row, 1).text()
            str2 = self.model.item(row+1, 1).text()

            self.model.setItem(row, 1,  QStandardItem(str2))
            self.model.setItem(row+1, 1,  QStandardItem(str1))
        self.tableView.selectRow(row + 1)

    def button2_clicked(self):
        file_lists = []
        maxrow = self.model.rowCount()
        for row in range(maxrow):
            file_lists.append(self.model.item(row, 1).text())
        print(file_lists)
        newfilename = self.lineedit1.text()
        self.mypdf.merge(file_lists=file_lists, new_filename=newfilename)

    def button3_clicked(self):
        path = QFileDialog.getExistingDirectory()
        new_filename = path + '/' + '新合并文件.PDF'
        self.lineedit1.setText(new_filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = MyMainWin()
    mainwin.show()
    sys.exit(app.exec_())




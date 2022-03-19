import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5 import QtPrintSupport
from pyqtgraph import PlotWidget
import numpy as np
#from PyQt5.QtWidgets import QFileDialog
#from fpdf import FPDF
#import os


class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120):
		fig = Figure(dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()


class sinusoidal():
    def __init__(self,name='unknown',amplitude=0,phaseshift=0,frequency=1,type='none'):
        self.name=name
        self.phaseShift=phaseshift
        self.amplitude=amplitude
        self.frequency=frequency
        self.type=type
        self.time = np.arange(0.0, 1, 0.001)
        if self.type == 'sin':
            self.plot = self.amplitude * np.sin(
                (2 * np.pi * self.frequency * self.time) + (self.phaseShift * np.pi / 180))
        elif self.type == 'cos':
            self.plot = self.amplitude * np.cos(
                (2 * np.pi * self.frequency * self.time) + (self.phaseShift * np.pi / 180))
        else:
            self.plot=0

    def plotting(self,widget):
        widget.plot(self.time,self.plot)

    def addPlots(self,plot2):
        self.plot=self.plot+plot2

    def getPlot(self):
        return self.plot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 877)
        self.Main_centralwidget_for_layout = QtWidgets.QWidget(MainWindow)
        self.Main_centralwidget_for_layout.setObjectName("Main_centralwidget_for_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Main_centralwidget_for_layout)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_horizontally_From_mid = QtWidgets.QSplitter(self.Main_centralwidget_for_layout)
        self.splitter_horizontally_From_mid.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_horizontally_From_mid.setObjectName("splitter_horizontally_From_mid")
        self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic = QtWidgets.QFrame(self.splitter_horizontally_From_mid)
        self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic.setObjectName("frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_for_mainGraph_and_illustrator_dynamic = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_mainGraph_and_illustrator_dynamic.setObjectName("verticalLayout_for_mainGraph_and_illustrator_dynamic")
        self.frame_mainGraph = QtWidgets.QFrame(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.frame_mainGraph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mainGraph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mainGraph.setObjectName("frame_mainGraph")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_mainGraph)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_For_Main_graph = QtWidgets.QLabel(self.frame_mainGraph)
        self.label_For_Main_graph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_For_Main_graph.setObjectName("label_For_Main_graph")
        self.gridLayout_3.addWidget(self.label_For_Main_graph, 0, 0, 1, 1)
        self.signalWidget_mainGraph = PlotWidget(self.frame_mainGraph)
        self.signalWidget_mainGraph.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.signalWidget_mainGraph.setObjectName("signalWidget_mainGraph")
        self.gridLayout_3.addWidget(self.signalWidget_mainGraph, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 313, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(454, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.verticalLayout_for_mainGraph_and_illustrator_dynamic.addWidget(self.frame_mainGraph)
        self.frame_for_ilustrator = QtWidgets.QFrame(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.frame_for_ilustrator.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_ilustrator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_ilustrator.setObjectName("frame_for_ilustrator")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_for_ilustrator)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.label_for_spectroGram = QtWidgets.QLabel(self.frame_for_ilustrator)
        self.label_for_spectroGram.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_spectroGram.setObjectName("label_for_spectroGram")
        self.gridLayout.addWidget(self.label_for_spectroGram, 0, 0, 1, 1)
        self.signalWidget2_ilustrator = PlotWidget(self.frame_for_ilustrator)
        self.signalWidget2_ilustrator.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.signalWidget2_ilustrator.setObjectName("signalWidget2_ilustrator")
        self.gridLayout.addWidget(self.signalWidget2_ilustrator, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 228, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.verticalLayout_for_mainGraph_and_illustrator_dynamic.addWidget(self.frame_for_ilustrator)
        self.verticalLayout_2.addLayout(self.verticalLayout_for_mainGraph_and_illustrator_dynamic)
        self.horizontalSlider_for_ilustrator = QtWidgets.QSlider(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.horizontalSlider_for_ilustrator.setMaximum(10)
        self.horizontalSlider_for_ilustrator.setPageStep(1)
        self.horizontalSlider_for_ilustrator.setSliderPosition(0)
        self.horizontalSlider_for_ilustrator.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_for_ilustrator.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_for_ilustrator.setTickInterval(1)
        self.horizontalSlider_for_ilustrator.setObjectName("horizontalSlider_for_ilustrator")
        self.verticalLayout_2.addWidget(self.horizontalSlider_for_ilustrator)
        self.splitter_for_generated_and_summation = QtWidgets.QSplitter(self.splitter_horizontally_From_mid)
        self.splitter_for_generated_and_summation.setOrientation(QtCore.Qt.Vertical)
        self.splitter_for_generated_and_summation.setObjectName("splitter_for_generated_and_summation")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_for_generated_and_summation)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_GeneratedSinusoidal = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_GeneratedSinusoidal.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_GeneratedSinusoidal.setObjectName("gridLayout_GeneratedSinusoidal")
        self.frame_for_generated_sinusoidal = QtWidgets.QFrame(self.layoutWidget)
        self.frame_for_generated_sinusoidal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_generated_sinusoidal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_generated_sinusoidal.setObjectName("frame_for_generated_sinusoidal")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_for_generated_sinusoidal)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_For_generatedSinusoidal = QtWidgets.QLabel(self.frame_for_generated_sinusoidal)
        self.label_For_generatedSinusoidal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_For_generatedSinusoidal.setObjectName("label_For_generatedSinusoidal")
        self.gridLayout_4.addWidget(self.label_For_generatedSinusoidal, 0, 0, 1, 1)
        self.Widget_Plotter = PlotWidget(self.frame_for_generated_sinusoidal)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Widget_Plotter.setPalette(palette)
        self.Widget_Plotter.setStyleSheet("background-color: rgb(173, 198, 224);")
        self.Widget_Plotter.setObjectName("Widget_Plotter")
        self.gridLayout_4.addWidget(self.Widget_Plotter, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(405, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 198, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 1, 1, 1, 1)
        self.gridLayout_GeneratedSinusoidal.addWidget(self.frame_for_generated_sinusoidal, 0, 0, 1, 1)
        self.gridLayout_For_generating_sinusoidal = QtWidgets.QGridLayout()
        self.gridLayout_For_generating_sinusoidal.setObjectName("gridLayout_For_generating_sinusoidal")
        self.label_plotName = QtWidgets.QLabel(self.layoutWidget)
        self.label_plotName.setObjectName("label_plotName")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.label_plotName, 0, 0, 1, 1)
        self.lineEdit_plotName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_plotName.setObjectName("lineEdit_plotName")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.lineEdit_plotName, 0, 1, 1, 1)
        self.label_frequency = QtWidgets.QLabel(self.layoutWidget)
        self.label_frequency.setObjectName("label_frequency")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.label_frequency, 0, 2, 1, 1)
        self.LineEdit_ferquency = QtWidgets.QLineEdit(self.layoutWidget)
        self.LineEdit_ferquency.setObjectName("LineEdit_ferquency")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.LineEdit_ferquency, 0, 3, 1, 1)
        self.radioButton_sine = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_sine.setObjectName("radioButton_sine")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.radioButton_sine, 0, 4, 1, 1)
        self.label_magnitude = QtWidgets.QLabel(self.layoutWidget)
        self.label_magnitude.setObjectName("label_magnitude")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.label_magnitude, 1, 0, 1, 1)
        self.lineEdit_magnitude = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_magnitude.setObjectName("lineEdit_magnitude")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.lineEdit_magnitude, 1, 1, 1, 1)
        self.label_phaseShift = QtWidgets.QLabel(self.layoutWidget)
        self.label_phaseShift.setObjectName("label_phaseShift")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.label_phaseShift, 1, 2, 1, 1)
        self.lineEdit_phaseShift = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_phaseShift.setAutoFillBackground(False)
        self.lineEdit_phaseShift.setInputMask("")
        self.lineEdit_phaseShift.setFrame(True)
        self.lineEdit_phaseShift.setDragEnabled(True)
        self.lineEdit_phaseShift.setObjectName("lineEdit_phaseShift")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.lineEdit_phaseShift, 1, 3, 1, 1)
        self.radioButton_cosine = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_cosine.setObjectName("radioButton_cosine")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.radioButton_cosine, 1, 4, 1, 1)
        self.add = QtWidgets.QPushButton(self.layoutWidget)
        self.add.setObjectName("add")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.add, 2, 0, 1, 5)
        self.gridLayout_GeneratedSinusoidal.addLayout(self.gridLayout_For_generating_sinusoidal, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_for_generated_and_summation)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_for_sinusoidalSummation = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_for_sinusoidalSummation.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_for_sinusoidalSummation.setObjectName("gridLayout_for_sinusoidalSummation")
        self.verticalLayout_mainGraphButtons = QtWidgets.QVBoxLayout()
        self.verticalLayout_mainGraphButtons.setObjectName("verticalLayout_mainGraphButtons")
        self.Button_open = QtWidgets.QPushButton(self.layoutWidget1)
        self.Button_open.setObjectName("Button_open")
        self.verticalLayout_mainGraphButtons.addWidget(self.Button_open)
        self.Generate_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.Generate_button.setObjectName("Generate_button")
        self.verticalLayout_mainGraphButtons.addWidget(self.Generate_button)
        self.Spare_button_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.Spare_button_2.setObjectName("Spare_button_2")
        self.verticalLayout_mainGraphButtons.addWidget(self.Spare_button_2)
        self.Spare_button_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.Spare_button_3.setObjectName("Spare_button_3")
        self.verticalLayout_mainGraphButtons.addWidget(self.Spare_button_3)
        self.Spare_button_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.Spare_button_4.setObjectName("Spare_button_4")
        self.verticalLayout_mainGraphButtons.addWidget(self.Spare_button_4)
        self.Spare_button_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.Spare_button_5.setObjectName("Spare_button_5")
        self.verticalLayout_mainGraphButtons.addWidget(self.Spare_button_5)
        self.Spare_button_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.Spare_button_6.setObjectName("Spare_button_6")
        self.verticalLayout_mainGraphButtons.addWidget(self.Spare_button_6)
        self.checkBox_showhide = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_showhide.setChecked(True)
        self.checkBox_showhide.setTristate(False)
        self.checkBox_showhide.setObjectName("checkBox_showhide")
        self.verticalLayout_mainGraphButtons.addWidget(self.checkBox_showhide)
        self.gridLayout_for_sinusoidalSummation.addLayout(self.verticalLayout_mainGraphButtons, 0, 0, 1, 1)
        self.widget_singleuse_as_backGround_for_summation = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_singleuse_as_backGround_for_summation.setObjectName("widget_singleuse_as_backGround_for_summation")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_singleuse_as_backGround_for_summation)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_For_summation = QtWidgets.QLabel(self.widget_singleuse_as_backGround_for_summation)
        self.label_For_summation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_For_summation.setObjectName("label_For_summation")
        self.gridLayout_5.addWidget(self.label_For_summation, 0, 0, 1, 1)
        self.Widget_Adder = PlotWidget(self.widget_singleuse_as_backGround_for_summation)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 198, 224))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Widget_Adder.setPalette(palette)
        self.Widget_Adder.setStyleSheet("background-color: rgb(173, 198, 224);")
        self.Widget_Adder.setObjectName("Widget_Adder")
        self.gridLayout_5.addWidget(self.Widget_Adder, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 233, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(346, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 2, 0, 1, 1)
        self.gridLayout_for_sinusoidalSummation.addWidget(self.widget_singleuse_as_backGround_for_summation, 0, 1, 1, 1)
        self.gridLayout_For_sunusoidalSummation = QtWidgets.QGridLayout()
        self.gridLayout_For_sunusoidalSummation.setObjectName("gridLayout_For_sunusoidalSummation")
        self.Button_confirmation = QtWidgets.QPushButton(self.layoutWidget1)
        self.Button_confirmation.setObjectName("Button_confirmation")
        self.gridLayout_For_sunusoidalSummation.addWidget(self.Button_confirmation, 1, 0, 1, 2)
        self.Combobox_signal = QtWidgets.QComboBox(self.layoutWidget1)
        self.Combobox_signal.setObjectName("Combobox_signal")
        self.gridLayout_For_sunusoidalSummation.addWidget(self.Combobox_signal, 0, 0, 1, 1)
        self.Button_delete = QtWidgets.QPushButton(self.layoutWidget1)
        self.Button_delete.setObjectName("Button_delete")
        self.gridLayout_For_sunusoidalSummation.addWidget(self.Button_delete, 0, 1, 1, 1)
        self.gridLayout_for_sinusoidalSummation.addLayout(self.gridLayout_For_sunusoidalSummation, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.splitter_horizontally_From_mid)
        MainWindow.setCentralWidget(self.Main_centralwidget_for_layout)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1146, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #buttons
        
        self.checkBox_showhide.stateChanged.connect(lambda: self.IsChecked())
        self.Button_confirmation.clicked.connect(lambda: self.signalConfirm())

        self.Generate_button.clicked.connect(self.plotS)
        self.radioButton_sine.clicked.connect(lambda:self.radiostate())
        self.radioButton_cosine.clicked.connect(lambda:self.radiostate())
        self.add.clicked.connect(self.adder_to_summation)
        #self.Button_confirmation.clicked.connect(self.adder_to_mainGraph) 
        self.Button_delete.clicked.connect(self.deletePlot)
        
        self.s='none'
        self.sinArr=[]
        
        
        
        
         #Functions
        
        
    def radiostate(self):
            if self.radioButton_cosine.isChecked() ==True :
                self.s='cos'

            else:
                self.s='sin'
                
    def IsChecked(self):
            if self.checkBox_showhide.isChecked()==False:
                #self.Hide_channel(1)
                #self.signalWidget2_ilustrator.hide() 
                self.frame_for_ilustrator.hide()
                
            else:
                #self.signalWidget2_ilustrator.show()  
                self.frame_for_ilustrator.show()
                


    def plotS(self):
        self.Widget_Plotter.clear()
        name=self.lineEdit_plotName.text()
        freq=int(self.LineEdit_ferquency.text())
        mag=int(self.lineEdit_magnitude.text())
        pS=int(self.lineEdit_phaseShift.text())
        Sinu=sinusoidal(name,mag,pS,freq,self.s)
        Sinu.plotting(self.Widget_Plotter)

    def adder_to_summation(self):
        name = self.lineEdit_plotName.text()
        freq = int(self.LineEdit_ferquency.text())
        mag = int(self.lineEdit_magnitude.text())
        pS = int(self.lineEdit_phaseShift.text())
        Sinu = sinusoidal(name, mag, pS, freq,self.s)
        self.sinArr.append(Sinu)
        self.Combobox_signal.addItem(Sinu.name)
        self.adderPLot()

    
    def adderPLot(self):
        self.Widget_Adder.clear()
        Sinu=sinusoidal()
        for i in range(len(self.sinArr)):
            Sinu.addPlots(self.sinArr[i].getPlot())

        Sinu.plotting(self.Widget_Adder)
         
    def adder_to_mainGraph(self):
        #name = self.lineEdit_plotName.text()
        #freq = int(self.LineEdit_ferquency.text())
        #mag = int(self.lineEdit_magnitude.text())
        #pS = int(self.lineEdit_phaseShift.text())
        #Sinu = sinusoidal(name, mag, pS, freq,self.s)
        #self.sinArr.append(Sinu)
        #self.Combobox_signal.addItem(Sinu.name)
       # Sinu.plotting(self.signalWidget_mainGraph)
        self.adderPLot()

    def deletePlot(self):
        index=self.Combobox_signal.currentIndex()
        self.sinArr.remove(self.sinArr[index])
        self.Combobox_signal.removeItem(index)
        self.adderPLot()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_For_Main_graph.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Main Graph</span></p></body></html>"))
        self.label_for_spectroGram.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\"> illustrator</span></p></body></html>"))
        self.label_For_generatedSinusoidal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">generated sinusoidal</span></p></body></html>"))
        self.label_plotName.setText(_translate("MainWindow", "Plot Name"))
        self.label_frequency.setText(_translate("MainWindow", "frequency"))
        self.radioButton_sine.setText(_translate("MainWindow", "Sine"))
        self.label_magnitude.setText(_translate("MainWindow", "Amplitude"))
        self.label_phaseShift.setText(_translate("MainWindow", "phase shift"))
        self.radioButton_cosine.setText(_translate("MainWindow", "cosine"))
        self.add.setText(_translate("MainWindow", "add to summation"))
        self.Button_open.setText(_translate("MainWindow", "Open"))
        self.Generate_button.setText(_translate("MainWindow", "Generate"))
        self.Spare_button_2.setText(_translate("MainWindow", "clear"))
        self.Spare_button_3.setText(_translate("MainWindow", "spare 3"))
        self.Spare_button_4.setText(_translate("MainWindow", "spare 4"))
        self.Spare_button_5.setText(_translate("MainWindow", "spare 5"))
        self.Spare_button_6.setText(_translate("MainWindow", "spare 6"))
        self.checkBox_showhide.setText(_translate("MainWindow", "Show"))
        self.label_For_summation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">sinusoidal summation </span></p></body></html>"))
        self.Button_confirmation.setText(_translate("MainWindow", "Add signal to illustrator"))
        self.Button_delete.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

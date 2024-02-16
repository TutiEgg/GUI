#IMPORTS.
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PySide2 import QtWebEngineWidgets
from bokeh.plotting import *

from bokeh.layouts import column, grid
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure, output_file, show


import functions
from ui_main import Ui_MainWindow

from ui_function import *
import ui_settings
import ui_parameter_settings

import numpy as np
import itertools
import os
import sys

from functools import partial
from inspect import signature
from ui_dialog import Ui_Dialog


# DIALOGBOX CLASS WHICH MAKE THE DIALOGBOX WHEN CALLED.
# ------> DIALOG BOX CLASS : DIALOGBOX CONTAINING TWO BUTTONS, ONE MESSEAGE BAR, ONE ICON HOLDER, ONE HEADING DEFINING

class dialogUi(QDialog):
    """
    Custom Window
    """
    def __init__(self, parent=None):
        super(dialogUi, self).__init__(parent)
        self.d = Ui_Dialog()
        self.d.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # REMOVING WINDOWS TOP BAR AND MAKING IT FRAMELESS (AS WE HAVE AMDE A CUSTOME FRAME IN THE WINDOW ITSELF)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # MAKING THE WINDOW TRANSPARENT SO THAT TO GET A TRUE FLAT UI

        #############################################################################################                        -------(C1)
        # -----> MINIMIZE BUTTON OF DIALOGBOX
        self.d.bn_min.clicked.connect(lambda: self.showMinimized())
        self.d.bn_min.setIcon(QtGui.QIcon("images/minimize.png"))

        # -----> CLOSE APPLICATION FUNCTION BUTTON
        self.d.bn_close.clicked.connect(lambda: self.close())
        self.d.bn_close.setIcon(QtGui.QIcon("images/close.png"))

        # -----> THIS FUNCTION WILL CHECKT WEATHER THE BUTTON ON THE DIALOGBOX IS CLICKED, AND IF SO, DIRECTS TO THE FUNCTINON : diag_return()

        ##############################################################################################

        ##################################################################################################                        ------(C2)
        # ---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER DIALOGBOX TOPBAR
        self.dragPos = self.pos()  # INITIAL POSOTION OF THE DIALOGBOX

        def movedialogWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.d.frame_top.mouseMoveEvent = movedialogWindow  # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE DIALOGBOX DURING MOUSE DRAG
        ################

    # ----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #################################################################################################

    #################################################################################################                        ------(C3)
    # THE DIALOG BOX IS ABLE TO CHANGE THE STATE OF THE TEXT SHOWN, BUTTON NAMES E.T.C
    # -------> SETTING THE DIALOGBOX CONFIGRATION: TEXT IN BUTTON, LABEL, HEADING
    def dialogConstrict(self, heading, message, btn1=None, btn2=None, btn1_func=None, btn2_func=None, icon=None):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)

        self.d.bn_west.setText(btn1)
        self.d.bn_east.setText(btn2)

        if btn1_func:
            self.d.bn_west.clicked.connect(btn1_func)
        if btn2_func:
            self.d.bn_east.clicked.connect(btn2_func)

        if heading:
            self.d.lab_heading.setText(heading)
        else:
            self.d.lab_heading.setText("Error")
        if icon:
            pixmap2 = QtGui.QPixmap(icon)
            self.d.lab_icon.setPixmap(pixmap2)
        else:
            pixmap2 = QtGui.QPixmap("images/close.png")
            self.d.lab_icon.setPixmap(pixmap2)
        if btn1:
            self.d.bn_west.setText(btn1)
        else:
            self.d.bn_west.setText("Aktion1")

        if btn2:
            self.d.bn_east.setText(btn2)
        else:
            self.d.bn_east.setText("Aktion2")


        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)


#-----> MAIN APPLICATION CLASS
class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.web_view = self.ui.widget
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "main.html"))
        local_url = QtCore.QUrl.fromLocalFile(file_path)
        self.web_view.setUrl(QtCore.QUrl(local_url))

        # Placeholder of settings_obj, only one Object can exist at the time
        self.settings_obj = None
        # Imported Data
        self.data_dict = {}
        # Processed Data dict
        self.processed_signals_dict = {}

        #----> SET WINDOW TITLE
        applicationName = "Aktuelle Technologien"
        self.setWindowTitle(applicationName)
        UIFunction_main.labelTitle(self, applicationName)
        ###############################

        #-----> INITIAL STACKED WIDGET PAGE WIDGET AND TAB
        UIFunction_main.initStackTab(self)
        ############################################################

        # ----> CERTAIN TOOLS LIKE DRAG, MAXIMISE, MINIMISE, CLOSE AND HIDING OF THE WINDOWS TOPBAR
        UIFunction_main.constantFunction(self)

        # ----> EXECUTING THE ERROR BOX MENU : THIS HELP TO CALL THEM WITH THE FUNCTIONS.
        # THIS CODE INITIALISED TD THE ERRORBOX, MAKES AN OBJECT OF THE CORRESPONDING CLASS, SO THAT ITS CALLABLE
        self.dialog = dialogUi()

        # ----> CREATE LAYOUT FOR TOPBAR AND NAVIGATION
        UIFunction_main.layout_top_sidebar(self)

        #----> TOODLE THE MENU HERE
        self.ui.toodle.clicked.connect(lambda: UIFunction_main.toodleMenu(self, 160, True))
        #############################################################

        # Add ROW_DELETED-Event for imported data_list
        self.ui.list_import.model().rowsRemoved.connect(lambda: self.update_visualization())

        #----> MENU BUTTON PRESSED EVENTS
        # Navigation
        self.ui.bn_navi_main.clicked.connect(lambda: UIFunction_main.buttonPressed(self, 'bn_navi_main'))
        self.ui.bn_navi_cut.clicked.connect(lambda: UIFunction_main.buttonPressed(self, 'bn_navi_cut'))
        self.ui.bn_navi_vis.clicked.connect(lambda: UIFunction_main.buttonPressed(self, 'bn_navi_vis'))
        # Settings
        self.ui.bn_settings.clicked.connect(lambda: self.create_settings_object())
        # Import Data
        self.ui.btn_import.clicked.connect(lambda: UIFunction_main.update_imported_files(self))
        # Export Data
        self.ui.btn_export.clicked.connect(lambda: UIFunction_main.export_checked_files(self))
        #############################################################

        #---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER APPNAME LABEL
        self.dragPos = self.pos()
        def moveWindow(event):

            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunction_main.returStatus(self) == 1:
                UIFunction_main.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Widget to move
        self.ui.lab_appname.mouseMoveEvent = moveWindow
        self.ui.lab_tab.mouseMoveEvent = moveWindow
        self.ui.lab_user.mouseMoveEvent = moveWindow
        self.ui.frame_spacer.mouseMoveEvent = moveWindow

        # JUST for experimentation with bokeh
        self.bokeh_exp()

    def get_data_info(self, data, path=None):
        # Get Sample_length
        info_dict = {}
        info_dict["len"] = len(data)

        if path:
            info_dict["Size"] = os.path.getsize(path)
            info_dict["last_modified"] = os.path.getmtime(path)
            info_dict["creation_date"] = os.path.getctime(path)


        return info_dict
    
    def update_processed_list(self, new_processed_signals):
        # TODO new_processed_signals should include information of settings too and other informations
        UIFunction_main.update_processed_list(self, new_processed_signals)

    def update_visualization(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "main.html"))
        local_url = QtCore.QUrl.fromLocalFile(file_path)
        self.web_view.setUrl(QtCore.QUrl(local_url))
        plot_list = []

        tools = ["pan", "box_select", "box_zoom", "tap", "wheel_zoom", "undo", "redo", "reset", "save"]

        mixed_signal_list = []

        for list_widget in [self.ui.list_import,  self.ui.list_saved]:
            for index in range(list_widget.count()):
                item = list_widget.item(index)
                customWidget = list_widget.itemWidget(item)
                mixed_signal_list.append(customWidget)

        # Get Data from list
        for customWidget in mixed_signal_list:
            
            data_dict = customWidget.data_dict
            info_dict = customWidget.data_info
            vis = customWidget.vis_bool
            print(vis, customWidget.name)
    
            if vis:
                x_list = []
                y_list = []
                out = dict(itertools.islice(data_dict.items(), 100))

                count = 0
                for x, val in out.items():

                    x_list.append(float(x))
                    y_list.append(val[1])
                    count += 1


                s = figure(tools=tools)
                s.circle(x_list, y_list, color="navy", alpha=0.5)
                s.line(x_list, y_list, color="navy", alpha=0.5)
                # s.circle(x, y1, color="navy", size=8, alpha=0.5)
                plot_list.append(s)

        l = grid(plot_list)
        save(l)
     
    #----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    #############################################################

    def create_settings_object(self):
        print(self.settings_obj)
        if not self.settings_obj:
            sett = SettingsWindow(parent=self)
            self.settings_obj = sett
            self.settings_obj.show()

    # -----> FUNCTION WHICH OPENS THE ERROR BOX AND DISPLAYS IT
    def dialogexec(self, heading, message, icon=None, btn1=None, btn2=None, btn1_func=None, btn2_func=None):
        dialogUi.dialogConstrict(self.dialog, heading, message, icon, btn1, btn2, btn1_func, btn2_func)
        self.dialog.exec_()

    def bokeh_exp(self):
        """
        This Function showcases the functionality of bokeh

        """
        tools = 'pan'

        def bollinger():
            # Define Bollinger Bands.
            upperband = np.random.randint(100, 150 + 1, size=100)
            lowerband = upperband - 100
            x_data = np.arange(1, 101)

            # Bollinger shading glyph:
            band_x = np.append(x_data, x_data[::-1])
            band_y = np.append(lowerband, upperband[::-1])

            p = figure(x_axis_type='datetime', tools=tools)
            p.patch(band_x, band_y, color='#7570B3', fill_alpha=0.2)

            p.title.text = 'Bollinger Bands'
            p.title_location = 'left'
            p.title.align = 'left'
            p.width = 800
            p.height = 600
            p.grid.grid_line_alpha = 0.4
            return [p]

        def slider():
            x = np.linspace(0, 10, 100)
            y = np.sin(x)

            source = ColumnDataSource(data=dict(x=x, y=y))

            plot = figure(
                y_range=(-10, 10), tools='', toolbar_location=None,
                title="Sliders example")
            plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

            amp_slider = Slider(start=0.1, end=10, value=1, step=.1, title="Amplitude")
            freq_slider = Slider(start=0.1, end=10, value=1, step=.1, title="Frequency")
            phase_slider = Slider(start=0, end=6.4, value=0, step=.1, title="Phase")
            offset_slider = Slider(start=-5, end=5, value=0, step=.1, title="Offset")

            callback = CustomJS(
                args=dict(source=source, amp=amp_slider, freq=freq_slider, phase=phase_slider, offset=offset_slider),
                code="""
                            const data = source.data;
                            const A = amp.value;
                            const k = freq.value;
                            const phi = phase.value;
                            const B = offset.value;
                            const x = data['x']
                            const y = data['y']
                            for (let i = 0; i < x.length; i++) {
                                y[i] = B + A*Math.sin(k*x[i]+phi);
                            }
                            source.change.emit();
                        """)

            amp_slider.js_on_change('value', callback)
            freq_slider.js_on_change('value', callback)
            phase_slider.js_on_change('value', callback)
            offset_slider.js_on_change('value', callback)

            widgets = column(amp_slider, freq_slider, phase_slider, offset_slider)
            return [widgets, plot]

        def linked_panning():
            N = 100
            x = np.linspace(0, 4 * np.pi, N)
            y1 = np.sin(x)
            y2 = np.cos(x)
            y3 = np.sin(x) + np.cos(x)

            s1 = figure(tools=tools)
            s1.circle(x, y1, color="navy", alpha=0.5)
            s2 = figure(tools=tools, x_range=s1.x_range, y_range=s1.y_range)
            s2.circle(x, y2, color="firebrick", alpha=0.5)
            s3 = figure(tools='pan, box_select', x_range=s1.x_range)
            s3.circle(x, y3, color="olive", alpha=0.5)

            print(x, y1)
            return [s1, s2, s3]

        l = grid([
            bollinger(),
            slider(),
            linked_panning(),
        ], sizing_mode='stretch_both')

        show(l)


class SettingsWindow(QMainWindow):
    """
    Settings Window
    """
    def __init__(self, parent=None):
        # Init
        self.parent = parent
        super(SettingsWindow, self).__init__(parent)
        self.ui = ui_settings.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Add all selectable FUnctions here
        self.functions_dict = {
            "lowpass_filter": partial(functions.lowpass_filter),
            "highpass_filter": partial(functions.highpass_filter),
        }

        self.qlistwidget = self.ui.list_data_processing
        self.sett_func = UIFunction_settings(self.ui, self.parent) # self.parent = main_window

        self.ui.list_selected.setAcceptDrops(True)
        self.ui.list_selected.setDragEnabled(True)
        self.ui.list_selected.setDefaultDropAction(Qt.MoveAction)
        self.initialize_gui()

    def initialize_gui(self):

        for funct in self.functions_dict:
            customWidget = CustomWidgetItem(name=funct, info=str(signature(self.functions_dict[funct])),
                                            add=self.ui.list_selected)
            item = QListWidgetItem()
            item.setSizeHint(customWidget.sizeHint())
            self.qlistwidget.addItem(item)
            self.qlistwidget.setItemWidget(item, customWidget)

            customWidget.qlistwidget = item

    def closeEvent(self, event):
        """
        On window close, delete Object clean and reset placeholder

        Args:
            event: closeEvent
        """
        setattr(self.parent, "settings_obj", None)
        self.deleteLater()
        event.accept()

    def visualization_status(self, customWidget):
        """
        Changes icon of visualization status

        Args:
            customWidget (CustomWidget): object
        """
        customWidget.vis_bool = not customWidget.vis_bool
        print(customWidget.vis_bool)

        if self.vis_bool:
            self.vis_button.setIcon(QtGui.QIcon("images/eye_open.png"))
        else:
            self.vis_button.setIcon(QtGui.QIcon("images/eye_closed.png"))

        self.update_visualization()


class ParameterWindow(QMainWindow):
    """
    ParameterWindow
    """

    def __init__(self, func_name, parent=None):
        try:
            # Init
            self.parent = parent
            self.func_name = func_name
            super(ParameterWindow, self).__init__(parent)
            self.ui = ui_parameter_settings.Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()

            self.parameter_dict = {}

            self.ui.btn_save_settings.clicked.connect(lambda: self.get_settings())
        
            self.initialize_gui()
        except Exception as e:
            print("Error occurred during initialization:", e)

    def initialize_gui(self):
        func = getattr(functions, self.func_name)
        sig = signature(func)
        # Create Parameter_dict

        for idx, (parameter_name, param) in enumerate(sig.parameters.items()):
            param_type = param.annotation
            
            label = QLabel(parameter_name, self)
            # Check what type parameter is
            if param_type is float:
                self.ui.grid_parameter.addWidget(label, idx, 0)
                var= QLineEdit()
                onlyFloat = QtGui.QDoubleValidator()
                onlyFloat.setRange(0.0, 100.0)
                var.setValidator(onlyFloat)
                self.ui.grid_parameter.addWidget(var, idx, 1)
                self.parameter_dict[parameter_name] = var
            elif param_type is int:
                self.ui.grid_parameter.addWidget(label, idx, 0)
                var = QLineEdit()
                onlyInt = QtGui.QIntValidator()
                onlyInt.setRange(0, 100)
                var.setValidator(onlyInt)
                self.ui.grid_parameter.addWidget(var, idx, 1)
                self.parameter_dict[parameter_name] = var

            elif param_type is str:
                self.ui.grid_parameter.addWidget(label, idx, 0)
                var = QLineEdit()
                self.ui.grid_parameter.addWidget(var, idx, 1)
                self.parameter_dict[parameter_name] = var

    def closeEvent(self, event):
        """
        On window close, delete Object clean

        Args:
            event: closeEvent
        """
        self.deleteLater()
        event.accept()

    def get_settings(self):
        """
        Get Parameter_settings given by userinputs
        """
        parameter_value_dict = {}
        for param in self.parameter_dict:
            print(self.parameter_dict[param].validator())
            if self.parameter_dict[param].validator() == None:
                parameter_value_dict[param] = self.parameter_dict[param].text()
            elif type(self.parameter_dict[param].validator()) is QtGui.QIntValidator:
                parameter_value_dict[param] = int(float(self.parameter_dict[param].text()))
            elif type(self.parameter_dict[param].validator()) is QtGui.QDoubleValidator:
                parameter_value_dict[param] = float(self.parameter_dict[param].text())
            
        self.parent.save_parameter_settings(parameter_value_dict)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

############################################################################################################################################################
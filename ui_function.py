# Imports

from main import *
import functions as func

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
import os
import json
from datetime import datetime
from inspect import signature
from functools import partial
from inspect import signature

from concurrent.futures import ThreadPoolExecutor, as_completed

GLOBAL_STATE = 0  # Check value if window is fullscreen or not
GLOBAL_TITLE_BAR = True # Check value if window is fullscreen or not
init = False # innition of window

class CustomWidgetItem(QWidget):
    """
    Custom Widget
    """
    def __init__(self, name,  info, vis=None, check=None, settings=None, add=None, delete=None, parent=None):
        """
        Initialize CustomWidget
        Adds an Item to CustomWidget, depending on which params are given (not None)

        Args:
            name (str): Name of Widget
            info (dict/object): TODO: Informations about widget (signal) or new window with information listet
            vis (main, optional): object of main_window. Defaults to None.
            check (boolean, optional): boolean. Defaults to None.
            settings (boolean, optional): If settings are avaiable for widget. Defaults to None.
            add (boolean, optional): Whether an Add-Button should be included or not. Defaults to None.
            delete (boolean, optional): Adds delete Button on True. Defaults to None.
            parent (self.parent, optional): paren_object. Defaults to None.
        """
        super(CustomWidgetItem, self).__init__(parent)

        self.data_dict = {}
        self.data_info = {}
        self.vis = vis
        self.name = name

        self.parameter_sett_obj = None
        self.parameter_sett_dict = None

        self.vis_bool = True # Set Visualization boolean
        self.export_state = True # Set Export boolean

        # Set Layout
        idx_list = [] #List of all stretches for each element in Layout
        layout = QHBoxLayout()
        self.qlistwidget = None

        # 1. Label
        self.label = QLabel(self.name, self)
        layout.addWidget(self.label)
        idx_list.append(10)

        # 2. Info-Button. -> Opens Infogui (dialoggui)
        self.info_button = QPushButton("", self)
        self.info_button.setStyleSheet("background:rgb(51,51,51)")
        self.info_button.setIcon(QtGui.QIcon("images/help.png"))
        #self.info_button.setIconSize(QSize(50, 50))
        self.info_button.clicked.connect(lambda: self.open_info())
        layout.addWidget(self.info_button)
        idx_list.append(2)
        # 3. Visibility Icon. -> True or False
        if vis:
            self.vis_button = QPushButton("", self)
            self.vis_button.setStyleSheet("background:rgb(51,51,51)")
            self.vis_button.setIcon(QtGui.QIcon("images/eye_open.png"))
            # self.settings_button.setIconSize(QSize(50, 50))
            self.vis_button.clicked.connect(lambda: self.visualization_status())
            layout.addWidget(self.vis_button)
            idx_list.append(1)

        # 4. Checkbox. -> True or False
        if check:
            self.checkbox = QCheckBox("", self)
            self.checkbox.setChecked(True)
            layout.addWidget(self.checkbox)

            self.checkbox.stateChanged.connect(self.checkbox_changed)
            idx_list.append(1)

        # 5. Settings-Button. -> Opens Parametergui
        if settings:
            self.settings_button = QPushButton("", self)
            self.settings_button.setStyleSheet("background:rgb(51,51,51)")
            self.settings_button.setIcon(QtGui.QIcon("images/settings.png"))
            #self.settings_button.setIconSize(QSize(50, 50))
            self.settings_button.clicked.connect(lambda: self.open_parameter_settings())
            layout.addWidget(self.settings_button)
            idx_list.append(1)

        # 6. Add-Button. -> Adds function to operation_list
        if add:
            self.add_button = QPushButton("", self)
            self.add_button.setStyleSheet("background:rgb(51,51,51)")
            self.add_button.setIcon(QtGui.QIcon("images/plus.png"))
            #self.add_button.setIconSize(QSize(50, 50))
            self.add_button.clicked.connect(lambda: self.add_item(name, info, add))
            layout.addWidget(self.add_button)
            idx_list.append(1)

        # 7. Delete-Button. -> Removes it from list
        if delete:
            self.del_button = QPushButton("", self)
            self.del_button.setStyleSheet("background:rgb(51,51,51)")
            self.del_button.setIcon(QtGui.QIcon("images/minus.png"))
            #self.del_button.setIconSize(QSize(50, 50))
            self.del_button.clicked.connect(self.delete_item)
            layout.addWidget(self.del_button)
            idx_list.append(1)

            
        # Set Layout Stretch
        for idx, value in enumerate(idx_list):
            layout.setStretch(idx, value)

        self.setLayout(layout)

    def open_parameter_settings(self):
        """
        Opens Parameter settings gui
        """
        self.parameter_sett_obj = ParameterWindow(func_name=self.name, parent=self)
        print(self.parameter_sett_obj.func_name)
        
    def save_parameter_settings(self, param_dict):
        """
        Saves all user_inputs from parameter_settings_gui

        Args:
            param_dict (dict): input given in dict-format
        """
        self.parameter_sett_dict = param_dict

    def visualization_status(self):
        """
        Sets visualization status
        """
        self.vis_bool = not self.vis_bool
        print(self.vis_bool)

        if self.vis_bool:
            self.vis_button.setIcon(QtGui.QIcon("images/eye_open.png"))
        else:
            self.vis_button.setIcon(QtGui.QIcon("images/eye_closed.png"))

        self.vis.update_visualization()

    def checkbox_changed(self, state):
        """
        Changes Checkbox status

        Args:
            state (event): 
        """
        if state == Qt.Checked:
            self.export_state = True
        else:
            self.export_state = False

    def add_item(self, name, info, qlistwidget):
        """
        Adds items to List with all choosen Operations

        Args:
            name (str): name
            info (dict): dict with signal infos
            qlistwidget (Qlistwidget): object
        """
        
        customWidget = CustomWidgetItem(name=name, info=info, settings=True, delete=True)
        item = QListWidgetItem()
        item.setSizeHint(customWidget.sizeHint())
        qlistwidget.addItem(item)
        qlistwidget.setItemWidget(item, customWidget)

        customWidget.qlistwidget = item

    def set_data_info(self, info):
        """
        Setter for self.data_info

        Args:
            info (dict): information of signal
        """
        self.data_info = info

    def set_data_dict(self, data):
        """
        Setter for self.data_dict

        Args:
            data (dict): content_data of signal
        """
        self.data_dict = data

    def delete_item(self):
        """
        Delete this CustomObject
        """

        list_widget = self.qlistwidget.listWidget()
        index = list_widget.row(self.qlistwidget)
        list_widget.takeItem(index)

        self.vis.update_visualization()

class UIFunction_main(MainWindow):
    """
    Function which handles all Functionalitys of the MainWindow (backend)
    """

    #----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE 
    def initStackTab(self):
        global init
        if init==False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
            self.ui.lab_tab.setText("Main")
            self.ui.frame_main.setStyleSheet("background:rgb(91,90,90)")
            init = True
    ################################################################################################

    #------> SETING THE APPLICATION NAME
    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)
    ################################################################################################

    #----> MAXIMISE/RESTORE FUNCTION
    # This Function maximises mainwindow on Button press or doubleclick on frame
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore") 
            self.ui.bn_max.setIcon(QtGui.QIcon("images/restore.png"))
            self.ui.frame_drag.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.bn_max.setToolTip("Maximize")
            self.ui.bn_max.setIcon(QtGui.QIcon("images/maximize.png"))
            self.ui.frame_drag.show()
    ################################################################################################

    # ----> RETURN STATUS MAX OR RESTROE
    def returStatus(self):
        return GLOBAL_STATE

    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # ------> TOODLE MENU FUNCTION
    def toodleMenu(self, maxWidth, clicked):

        # ------> clear bg
        for each in self.ui.frame_bottom_west.findChildren(QFrame): 
            each.setStyleSheet("background:rgb(51,51,51)")

        if clicked:
            currentWidth = self.ui.frame_bottom_west.width() # read current widget
            minWidth = 80 # min widget
            if currentWidth == 80:
                extend = maxWidth
                # ----> MAKE THE STACKED WIDGET PAGE TO ABOUT MAIN PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_main)
                self.ui.lab_tab.setText("About > Main")
                self.ui.page_main.setStyleSheet("background:rgb(91,90,90)")
            else:
                extend = minWidth
                # -----> REVERT THE ABOUT Main PAGE TO NORMAL MAIN PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
                self.ui.lab_tab.setText("Main")
                self.ui.page_main.setStyleSheet("background:rgb(91,90,90)")
            # animation
            self.animation = QPropertyAnimation(self.ui.frame_bottom_west, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(minWidth)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    ################################################################################################

    # -----> DEFAULT ACTION FUNCTION
    def constantFunction(self):
        # -----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction_main.maximize_restore(self))

        # ----> REMOVE NORMAL TITLE BAR
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.lab_appname.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        # SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        # DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        # -----> MINIMIZE BUTTON FUNCTION
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        # -----> MAXIMIZE/RESTORE BUTTON FUNCTION
        self.ui.bn_max.clicked.connect(lambda: UIFunction_main.maximize_restore(self))

        # -----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: self.close())
    ################################################################################################################

    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        # ------> THIS LINE CLEARS THE BG OF PREVIOUS TABS
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName=='bn_navi_main':
            if self.ui.frame_bottom_west.width()==80  and index!=0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
                self.ui.lab_tab.setText("Main")
                self.ui.page_main.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160  and index!=1:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_main)
                self.ui.lab_tab.setText("About > Main")
                self.ui.page_main.setStyleSheet("background:rgb(91,90,90)")

        elif buttonName=='bn_navi_vis':
            if self.ui.frame_bottom_west.width()==80 and index!=5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_vis)
                self.ui.lab_tab.setText("Visualization")
                self.ui.page_vis.setStyleSheet("background:rgb(91,90,90)")

            elif self.ui.frame_bottom_west.width()==160 and index!=4:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_vis)
                self.ui.lab_tab.setText("About > Visualization")
                self.ui.page_vis.setStyleSheet("background:rgb(91,90,90)")

        elif buttonName=='bn_navi_cut':
            if self.ui.frame_bottom_west.width()==80  and index!=7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_cutting)
                self.ui.lab_tab.setText("Cut")
                self.ui.page_cutting.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160  and index!=3:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_cutting)
                self.ui.lab_tab.setText("About > Cut")
                self.ui.page_cutting.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

           ########################################################################################################################

    # TODO: Seperate Front-end-layout to seperate File
    def layout_top_sidebar(self):
        self.ui.bn_settings.setIcon(QtGui.QIcon("images/settings.png"))
        self.ui.bn_min.setIcon(QtGui.QIcon("images/minimize.png"))
        self.ui.bn_max.setIcon(QtGui.QIcon("images/maximize.png"))
        self.ui.bn_close.setIcon(QtGui.QIcon("images/close.png"))

        self.ui.bn_navi_cut.setIcon(QtGui.QIcon("images/cut.png"))
        self.ui.bn_navi_cut.setIconSize(QSize(30, 30))
        self.ui.bn_navi_main.setIcon(QtGui.QIcon("images/main.png"))
        self.ui.bn_navi_main.setIconSize(QSize(30, 30))
        self.ui.bn_navi_vis.setIcon(QtGui.QIcon("images/visualization.png"))
        self.ui.bn_navi_vis.setIconSize(QSize(30, 30))
        self.ui.toodle.setIcon(QtGui.QIcon("images/help.png"))
        self.ui.toodle.setIconSize(QSize(50,50))

    def update_processed_list(self, new_processed_signals):
        """
        Updates saved_list on main_window with CustomWidgets (ListItems)

        Args:
            new_processed_signals (dict): data of new generated data
        """
        # TODO: ADD Check for same name isntead of giving datetime to name
 
        date_time = datetime.now().strftime("%Y%m%d-%H%M%S")
        for idx, (signal_id, signal_data) in enumerate(new_processed_signals.items()):
            name = "{}_processed_{}".format(signal_id, date_time)
            customWidget = CustomWidgetItem(name, vis=self, check=True ,info="", delete=True)
            item = QListWidgetItem()
            item.setSizeHint(customWidget.sizeHint())
            #item.setToolTip(path)

            self.ui.list_saved.addItem(item)
            self.ui.list_saved.setItemWidget(item, customWidget)

            self.processed_signals_dict[name] = signal_data["processed_data"]

            # Get Data
            # customWidget.set_data_info(self.get_data_info(data, path))
            customWidget.set_data_dict(signal_data["processed_data"])

            customWidget.qlistwidget = item

        self.update_visualization()

    def update_imported_files(self):
        """
        Updates all new Imported files in import_list
        """
        # Get all Data_names which are already imported
        data_exist_list = []
        for x in range(self.ui.list_import.count()):
            item = self.ui.list_import.item(x)
            customWidget = self.ui.list_import.itemWidget(item)
            data_exist_list.append(customWidget.name)
        # Placeholder for Error Message (So it Stacks and outputs only one Big Message)
        error_placeholder = []

        list_file_paths = func.open_file_browser()
        # Iterate over every element in list
        if list_file_paths:
            for path in list_file_paths:
                # Get last part of Path
                name = os.path.basename(os.path.normpath(path))


                if name not in data_exist_list:
                    customWidget = CustomWidgetItem(name, vis=self ,info="", delete=True)
                    item = QListWidgetItem()
                    item.setSizeHint(customWidget.sizeHint())
                    item.setToolTip(path)

                    self.ui.list_import.addItem(item)
                    self.ui.list_import.setItemWidget(item, customWidget)

                    # Get Data
                    data = func.read_files(path)
                    customWidget.set_data_info(self.get_data_info(data, path))
                    customWidget.set_data_dict(data)

                    customWidget.qlistwidget = item
                else:
                    error_placeholder.append(r"Die Datei {} wurde schon importiert!".format(name))

            if error_placeholder:
                error_msg = '\n'.join(error_placeholder)
                self.dialogexec("FEHLER", error_msg)


        # Update Visualization (bokeh)
        self.update_visualization()

    def get_data_info(self, data, path=None):
        # Get Sample_length
        info_dict = {}
        info_dict["len"] = len(data)

        if path:
            info_dict["Size"] = os.path.getsize(path)
            info_dict["last_modified"] = os.path.getmtime(path)
            info_dict["creation_date"] = os.path.getctime(path)

    def export_checked_files(self):
        """
        Export all checked files
        """
        selected_folder = QFileDialog.getExistingDirectory(self, "Ordner auswählen")
        if selected_folder: 
            for filename, content in self.processed_signals_dict.items():
                file_path = os.path.join(selected_folder, str(filename))

                with open(file_path, 'w') as f:
                    json.dump(content, f)

    def delete_from_selected_list(self, label):
        """
        Deletes Item from selected_list

        Args:
            label (_type_): _description_
        """
        index = self.ui.list_import.row(label)
        self.ui.list_import.takeItem(index)
        path = self.ui.list_import.item(index).toolTip()
        # Get last part of Path
        name = os.path.basename(os.path.normpath(path))
        self.data_dict.pop(name)
        self.update_visualization()

class UIFunction_settings(QWidget):
    """
    Function which handles all Functionalitys of the SettingsWindow (backend)

    """
    def __init__(self, ui, parent=None):
        super(UIFunction_settings, self).__init__(parent)
        self.ui = ui # Settings_UI
        self.ui.btn_settings_start.clicked.connect(lambda: self.start_process())
        self.parent = parent # parent_object (MainWindow)
 
    def apply_filters_sequentially(self, signal_data, filter_functions):
        # Filter sequentally
        current_data = signal_data
        for filter_function, params in filter_functions:
            current_data = filter_function(current_data, **params)
        return current_data

    def save_to_json(self, data, filename):
        
        # Save json FOR TESTS
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(ROOT_DIR)
        path = os.path.join(project_dir, "temp_processed_files", filename)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)

    def process_signal(self, signal_id, signal_data, filter_functions, json=False):
        # Preprocessing of one single File per Thread
        processed_signal = self.apply_filters_sequentially(signal_data, filter_functions)
        if json:
            self.save_to_json(processed_signal, f'processed_signal_{signal_id}.json')
        
        return signal_id, processed_signal, signal_data

    def start_process(self):
        # Creates a filterlist of functions
        filter_functions = []
        for i in range(self.ui.list_selected.count()):
            item = self.ui.list_selected.item(i)
            custom_widget = self.ui.list_selected.itemWidget(item)
            param_dict = custom_widget.parameter_sett_dict
            function_name = custom_widget.label.text()
            function = getattr(func, function_name)  # Holen der Funktion anhand des Namens
            filter_functions.append((function, param_dict))

        # Signal Dictionary
        signals_dict = {}
        for x in range(self.parent.ui.list_import.count()):
            item = self.parent.ui.list_import.item(x)
            customWidget = self.parent.ui.list_import.itemWidget(item)
            signals_dict[x] = customWidget.data_dict

        # Verarbeiten der Signale nebenläufig mit einer begrenzten Anzahl gleichzeitiger Tasks
        
        max_workers = 5  # Maximale Anzahl gleichzeitig laufender Verarbeitungen
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Einreichen der Tasks
            futures = [executor.submit(self.process_signal, signal_id, signal_data, filter_functions) for signal_id, signal_data in signals_dict.items()]
            processed_signals = {}
            # Ergebnisse sammeln, sobald sie verfügbar sind
            for future in as_completed(futures):
                signal_id, processed_signal, original_signal = future.result()
                signal_dict = {}
                signal_dict["original_data"] = original_signal
                signal_dict["processed_data"] = processed_signal
                processed_signals[signal_id] = signal_dict
            self.parent.update_processed_list(processed_signals)
        

        













###############################################################################################################################################################
# Imports

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import sys
import csv
import json
import os
import time

import numpy as np
from scipy.signal import butter, filtfilt
import scipy.io.wavfile
import pandas as pd


def highpass_filter_thread_test(data: dict, cutoff: float, sample_rate: float, poles: int) -> dict:

    print("highpass stage 1")
    time.sleep(1)

    b, a = butter(poles, cutoff / (0.5 * sample_rate), btype='high', analog=False)

    all_values = np.concatenate([values for values in data.values()])

    filtered_values = filtfilt(b, a, all_values)

    time.sleep(1)
    print("highpass stage 2")
    filtered_data = {}
    index = 0
    for timestamp, values in data.items():
        length = len(values)
        filtered_data[timestamp] = filtered_values[index:index+length].tolist()
        index += length

    time.sleep(1)
    print("highpass stage 3")
    return filtered_data

def highpass_filter(data: dict, cutoff: float, sample_rate: float, poles: int) -> dict:

    #TODO: default_values in Param
    
        #cutoff = 100.0
    
        #sample_rate = 100.0
    
        #poles = 2
    
    
     # Create Highpass-Filter
    b, a = butter(poles, cutoff / (0.5 * sample_rate), btype='high', analog=False)

    all_values = np.concatenate([values for values in data.values()])
    filtered_values = filtfilt(b, a, all_values)
    filtered_data = {}
    index = 0
    for timestamp, values in data.items():
        length = len(values)
        filtered_data[timestamp] = filtered_values[index:index+length].tolist()
        index += length

    return filtered_data

def lowpass_filter(data: dict, cutoff: float, sample_rate: float, poles: int) -> dict:
    #TODO: default_values in Param
    
        #cutoff = 100.0
    
        #sample_rate = 100.0
    
        #poles = 2
   
    
    # Create Lowpass-Filters
    b, a = butter(poles, cutoff / (0.5 * sample_rate), btype='low', analog=False)

    all_values = np.concatenate([values for values in data.values()])
    filtered_values = filtfilt(b, a, all_values)
    filtered_data = {}
    index = 0
    for timestamp, values in data.items():
        length = len(values)
        filtered_data[timestamp] = filtered_values[index:index+length].tolist()
        index += length

    return filtered_data

def open_file_browser():
    """
    Opens a file_browser where the user can choose Signal_data to import (multiple are possible at the same time)

    Returns:
        _type_: _description_
    """
    file_dialog = QFileDialog()
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_dialog.setDirectory(os.path.join(ROOT_DIR, "files"))
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    file_dialog.setNameFilter("*.csv *.json")

    if file_dialog.exec():
        file_paths = file_dialog.selectedFiles()
        return file_paths
    return None

def read_files(path):
    path_end = path.split(".")
    data_dict = {}
    if path_end[-1] == "json":
        with open(path, 'r') as f:
            data_dict = json.load(f)
    if path_end[-1] == "csv":
        data = pd.read_csv(path)
        # Convert the DataFrame to a Dictionary
        data_dict = data.to_dict()
    return data_dict




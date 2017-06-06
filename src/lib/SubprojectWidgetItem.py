

from PyQt5.QtWidgets import *
import datetime

from .SubprojectWidget import * 

class SubprojectWidgetItem(QListWidgetItem):
    
    def setSubproject(self, subproject):
        self.subproject = subproject
        self.setText(subproject.getName())

    def getSubproject(self):
        return subproject

    def show_details(self):
        widget = SubprojectWidget()
        widget.setSubproject(self.subproject)
        widget.show()

    def __init__(self):
        super(SubprojectWidgetItem, self).__init__()

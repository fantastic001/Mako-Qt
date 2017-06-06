

from PyQt5.QtWidgets import *
import datetime

from .SubprojectWidgetItem import * 

class ProjectWidget(QWidget):
    
    def setProject(self, project):
        self.project = project 
        self.label.setText("Project: %s" % project.getName())
        self.items.clear()
        for subproject in project.getSubprojects():
            item = SubprojectWidgetItem()
            item.setSubproject(subproject)
            self.items.addItem(item)
    
    def itemChanged(self, item):
        item.show_details()

    def __init__(self):
        super(ProjectWidget, self).__init__()
        layout = QVBoxLayout()
        self.label = QLabel("")
        layout.addWidget(self.label)
        self.items = QListWidget() 

        layout.addWidget(self.items)
        self.setLayout(layout)
        self.items.itemDoubleClicked.connect(self.itemChanged)

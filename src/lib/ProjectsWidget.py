


from PyQt5.QtWidgets import *
import datetime

from .ProjectWidget import * 
from .ProjectWidgetItem import * 
from .SubprojectWidget import * 

class ProjectsWidget(QWidget):
    
    def setDatabase(self, db):
        self.db = db
        self.label.setText("Projects")
        self.items.clear()
        for project in db.downloadProjects():
            item = ProjectWidgetItem()
            item.setProject(project)
            self.items.addItem(item)
    
    def itemChanged(self, item):
        self.current_project.setProject(item.getProject())
    def __init__(self):
        super(ProjectsWidget, self).__init__()
        layout = QVBoxLayout()
        self.label = QLabel("")
        layout.addWidget(self.label)
        self.items = QListWidget() 

        layout.addWidget(self.items)

        self.current_project = ProjectWidget()
        layout.addWidget(self.current_project)
        self.setLayout(layout)
        self.items.itemDoubleClicked.connect(self.itemChanged)

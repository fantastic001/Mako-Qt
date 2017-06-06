

from PyQt5.QtWidgets import *
import datetime

from .SubprojectWidgetItem import * 
from .Database import * 

from mako.lib.schedule import * 

class ProjectWidget(QWidget):
    
    def setProject(self, project):
        self.project = Database.getProjectByName(project.getName())
        project = self.project
        self.label.setText("Project: %s" % project.getName())
        self.items.clear()
        for subproject in project.getSubprojects():
            item = SubprojectWidgetItem()
            item.setSubproject(subproject)
            self.items.addItem(item)
    
    def add_subproject(self):
        name,ok = QInputDialog.getText(self, "Create new subproject", "Enter subproject's name ")
        if not ok:
            return
        projects = Database.getDatabase().downloadProjects()
        for proj in projects:
            if proj.getName() == self.project.getName():
                proj.addSubproject(ScheduleSubproject(name))
        Database.getDatabase().uploadProjects(projects)
        self.setProject(self.project)

    def itemChanged(self, item):
        item.show_details()

    def __init__(self):
        super(ProjectWidget, self).__init__()
        layout = QVBoxLayout()
        self.label = QLabel("")
        add_button = QPushButton("+")
        add_button.clicked.connect(self.add_subproject)
        layout.addWidget(add_button)
        layout.addWidget(self.label)
        self.items = QListWidget() 

        layout.addWidget(self.items)
        self.setLayout(layout)
        self.items.itemDoubleClicked.connect(self.itemChanged)

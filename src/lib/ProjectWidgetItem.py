

from PyQt5.QtWidgets import *
import datetime

from .ProjectWidget import * 

class ProjectWidgetItem(QListWidgetItem):
    
    def setProject(self, project):
        self.project = project
        self.setText(project.getName())

    def getProject(self):
        return self.project

    def show_details(self):
        widget = ProjectWidget()
        widget.setProject(self.project)
        widget.show()

    def __init__(self):
        super(ProjectWidgetItem, self).__init__()

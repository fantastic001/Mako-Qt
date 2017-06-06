
from PyQt5.QtWidgets import *
import datetime

class SubprojectWidget(QWidget):
    
    def setSubproject(self, subproject):
        self.subproject = subproject 
        self.label.setText("Subproject: %s" % subproject.getName())
        self.items.clear()
        tasks = subproject.getAllTasks()
        for task in tasks:
            to_add = True
            if self.done_checkbox.isChecked() and task.isDone():
                to_add = False 
            if self.current_month_checkbox.isChecked() and not (task.getDueDate().month == datetime.date.today().month and datetime.date.today().year == task.getDueDate().year):
                to_add = False
            if to_add:
                self.items.addItem(task.getText())

    def __init__(self):
        super(SubprojectWidget, self).__init__()
        layout = QVBoxLayout()
        self.label = QLabel("")
        layout.addWidget(self.label)
        checkboxes = QHBoxLayout()
        self.done_checkbox = QCheckBox("Shhow only undone tasks")
        self.done_checkbox.clicked.connect(lambda: self.setSubproject(self.subproject))
        self.current_month_checkbox = QCheckBox("Show only tasks this month")
        self.current_month_checkbox.clicked.connect(lambda: self.setSubproject(self.subproject))
        checkboxes.addWidget(self.done_checkbox)
        checkboxes.addWidget(self.current_month_checkbox)
        layout.addLayout(checkboxes)
        self.items = QListWidget() 

        layout.addWidget(self.items)
        self.setLayout(layout)

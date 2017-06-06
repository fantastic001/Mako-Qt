
import sys
from PyQt5.QtWidgets import QApplication

from lib.ProjectsWidget import * 
from lib.Database import * 

from mako.lib import * 
from mako.desktop import * 
import os

app = QApplication(sys.argv)

db = MakoDesktopDatabase(os.environ["HOME"] + "/.mako/db/")

widget = ProjectsWidget()
widget.setDatabase(db)
widget.show()

#window = MainWindow()
#window.show()

sys.exit(app.exec_())



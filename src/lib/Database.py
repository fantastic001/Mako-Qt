
from mako.desktop import * 

class Database:

    def getDatabase():
        return MakoDesktopDatabase(os.environ["HOME"] + "/.mako/db")

    def getProjectByName(name):
        projects = Database.getDatabase().downloadProjects()
        for p in projects:
            if p.getName() == name:
                return p 

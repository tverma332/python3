class Tomcat(object):
    def __init__(self , home , ver):
        self.home = home
        self.version = ver
        return None
    def display(self):
        print("This is form tomcat class")
        print(self.home)
        print(self.version)

class Apache(object):
    def __init__(self , home , ver):
        self.home = home
        self.version = ver
        return None
    def display(self):
        print("This is form apache class")
        print(self.home)
        print(self.version)

tom_ob = Tomcat('/home/tomcat9' , '7.97')
apa_ob = Apache('/etc/httpd' , '2.4')

tom_ob.display()
apa_ob.display()
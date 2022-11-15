import npyscreen

# TUI that gets IP address, netmask, and gateway from the user
class connectTUI(npyscreen.Form):
        def create(self):
                ip = self.add(npyscreen.TitleText, name = "Management IP Address: ")
                netmask = self.add(npyscreen.TitleText, name = "Netmask: ")
                username = self.add(npyscreen.TitleText, name = "Administrator Username: ")
                password = self.add(npyscreen.TitleText, name = "Password: ")
        def afterEditing(self):
                self.parentApp.setNextForm(podMAN)


class Application(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', connectTUI, name='Pod Manager')
        
        
if __name__ == '__main__':
    TestApp = Application().run()
    print ("Program Complete")
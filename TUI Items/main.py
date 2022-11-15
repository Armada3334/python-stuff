import npyscreen

# TUI that gets IP address, netmask, and gateway from the user
class myFunctionSelector(npyscreen.Form):
        def create(self):
                ip = self.add(npyscreen.TitleText, name = "IP Address: ")
                netmask = self.add(npyscreen.TitleText, name = "Netmask: ")
        def afterEditing(self):
                self.parentApp.setNextForm(None)


class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', myFunctionSelector, name='Select Function')

if __name__ == '__main__':
    TestApp = MyApplication().run()
    print ("Program Complete")
# Creating Package Manager Class

# In the below, pm passes value to the Packamanager Class and will get printed using get_details

class PackageManager:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def get_details(self):
        print('name :', self.name)
        print('varion :', self.version)

pm = PackageManager('cpan', '2.2.18')
pm.get_details()

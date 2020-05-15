
class Engineer :
    def __init__(self , licence_no):
        self.licence_no = licence_no
    def design_project(self):
        print("I am designing a project")

class SeniorEngineer(Engineer):
    def __init__(self, licence_no ,num_projects):
        super().__init__(licence_no)
        self.num_projects = num_projects
    def deal_project(self):
        print("I have got project to do.")
        self.num_projects += 1
class SeniorComputerEngineer(SeniorEngineer):
    def __init__(self , licence_no ,num_projects ,curr_project):
        super().__init__(licence_no,num_projects)
        self.curr_project = curr_project

rituja = Engineer('RS0597')
rituja.design_project()

isha = SeniorEngineer('ID0903', 4)
isha.deal_project()
print('Isha has handled ' + str(isha.num_projects) + ' projects')

aarya = SeniorComputerEngineer('AP0611',6,'Web App')
print('Aarya is currently working on  '   +aarya.curr_project)
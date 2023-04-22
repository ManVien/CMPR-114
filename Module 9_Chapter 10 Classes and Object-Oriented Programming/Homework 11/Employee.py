# Employee Class
class Employee:
    # The __init__ method initializes the attributes
    def __init__(self, name, ID, department, title):
        self.__name = name
        self.__ID_number = ID
        self.__department = department
        self.__job_title = title

    # mutator method
    def set_name(self, name):
        self.__name = name
     
    def set_id_number(self, ID):
        self.__ID_number = ID

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, title):
        self.__job_title = title

    # accessor method
    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__ID_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return self.get_name() + "\t" + str(self.get_id_number()) + "\t\t" + \
          self.get_department() + "\t" + self.get_job_title()
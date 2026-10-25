# Multiple inheritance: PhDStudent inherits from both Student and Faculty.
class Student:
    def __init__(self, sid, deptid):
        self.sid = sid
        self.deptid = deptid

    def get_info(self):
        return "StudentID:{} DepartmentID:{}".format(self.sid, self.deptid)


class Faculty:
    def __init__(self, eid, deptid):
        self.eid = eid
        self.deptid = deptid

    def get_info(self):
        return "EmployeeID:{} DepartmentID:{}".format(self.eid, self.deptid)


class PhDStudent(Student, Faculty):
    def __init__(self, sid, eid, deptid):
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)

    def get_info(self):
        return "StudentID:{} EmployeeID:{} DepartmentID:{}".format(
            self.sid, self.eid, self.deptid
        )

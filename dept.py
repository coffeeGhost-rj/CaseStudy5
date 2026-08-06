
class Department:
    # Class variable shared across all instances
    deptcount = 100

    def __init__(self, deptname, loc):
        # Fixed: Match the method's exact variable name case
        self.setDeptName(deptName=deptname)
        self.setLoc(loca=loc)
        Department.deptcount += 1
        self.deptID = Department.deptcount

    # Fixed typo in method name for consistency
    def setDeptName(self, deptName):
        if len(deptName.strip()) == 0:  # .strip() prevents entering just spaces
            raise ValueError("Enter a valid Dept Name.")
        else:
            self.deptname = deptName

    def setLoc(self, loca):
        if len(loca.strip()) == 0:
            raise ValueError("Enter a valid Location.")
        else:
            self.loc = loca

    def showDeptDetails(self):
        return f"Dept ID: {self.deptID}, Dept Name: {self.deptname}, Dept Location: {self.loc}"

class Address:
    def __init__(self, street, city, pincode):
        # self.street = street
        # self.city = city
        # self.pincode = pincode
        self.setAddress(street, city, pincode)
        
    def setAddress(self, street, city, pincode):
        if len(street)==0:
            raise ValueError("this area cannot be blank.")
        else:
            self.street = street
        if len(city)==0 and city.isdigit():
            raise ValueError("city cannot be a number.")
        else:
            self.city = city
        if len(pincode)>=7 and len(pincode)<=5 and pincode.isalpha():
            raise ValueError("enter a proper pincode.")
        else:
            self.pincode = pincode
            
    def showAdd(self):
        """
        Purpose: self
 street, city, pincode    """
        return f"Address : {self.street, self.city, self.pincode}"
    # end def
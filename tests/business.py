#this is the business class handling all business logic

######################################
#           BUSINESS CLASS
######################################

class Business():
    """class that handles bussiness logic ie. create business,view own businesses,view all businesses,
    delete a business and update business the functions in this class include
    createBusiness, checkBusinessExists, updateBusiness, deleteBusiness, getOwnBusinesses, getAllBusinesses"""
    
    def __init__(self, busId, userId, busName, busLocation, busCategory, busDescription):
        # initialise the variables here. business id,user id, business name, business location,
        #  business category,business description.
        self.busId=busId
        self.userId=userId
        self.busName = busName
        self.busLocation=busLocation
        self.busCategory=busCategory
        self.busDescription = busDescription
        self.businessList = []

    def createBusiness(self, busId, userId, busName, busLocation, busCategory, busDescription):
        """function for creating a new business. funtion returns a boolean true if a business has been created and false 
        if business is not created."""
        #global businessList
        result = None
        oldBizListLength = len(self.businessList) # length of busines ltist before manipulation.
        #create the list below with precise indexing as illustrated below
        # [0] = userId, [1] = busName, [2] = busLocation, [3] = busCategory, [4] = busDescription
        self.businessList.append({busId:[userId, busName, busLocation, busCategory, busDescription]})
        
        if len(self.businessList) > oldBizListLength:
            result = True #incase creating a business is successful return true.
        else:
            result = False #incase creating a business failes return False.
        
        return result


    def checkBusinessExists(self, busId):
        """function to check whether a business Exists or not. function return a boolean true if business exists and
        false if it does not exist."""
        result = None #this is our retun value
        for bus in self.businessList:
            if busId not in bus.keys():
                result = True #business id /key exists
            else:
                result = False#busId doesnt exist

        return result

    def updateBusiness(self, busId, userId, busName, busLocation, busCategory, busDescription):
        """this function is for updating business details. function returns a boolean true is business was updated 
        and false for otherwise"""        
        oldList=[] #this will hold the old details of the business
        newList=[] #this will hold the new details of the business
        result = None #variable to test whether business has been updated or not.
        for xt in self.businessList:
            for key, val in xt.items():
                if key == busId:
                    oldList.append([x for x in val]) #oldlist going to be used for comparison
                    xt[key]=[busId, userId, busName, busLocation, busCategory, busDescription]
                    newList.append([x for x in xt[key]]) #new list going to be used for comparison
                    if oldList[0] == newList[0] and oldList[1] == newList[1] and oldList[2] == newList[2] \
                        and oldList[3] == newList[3] and oldList[4] == newList[4]:
                        result = False
                    else:
                        result = True
        return result
    
    def deleteBusiness(self, busId):
        """this fuinction is responsible for deleting a business"""
        pass


    def getOwnBusinesses(self, userId):
        """function checks for a peron's own created businesses. function returns 
        a list of businesses attached to the passed userId"""        
        foundrows=[] #we will store our found records in this list
        #result = False
        for x in self.businessList:
            for val in x.values():
                if val[0] == userId:
                    foundrows.append(x)
                    # if len(foundrows) > 0: 
                    #     result = True # This means we atleast found one row matching that userId.
                    # else:
                    #     result = False # This means we no business matching that userId.
        return foundrows

        
    def getAllBusinesses(self):
        """this function return all businesses that ar available. 
        the function returns a list of all businesses registered."""
        foundBusinesses = []
        if len(self.businessList) > 0: # make sure atleast there are some records
            for x in self.businessList: # x represents each individual business
                foundBusinesses.append(x)

        return foundBusinesses
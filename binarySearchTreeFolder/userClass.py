class User:
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email
        print("user created!")
    
    def introduce_yourself(self,guest_name):
        print("Hi {}, I'm {}! Contact at {} . ".format(guest_name,self.name,self.email))
        
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

class UserDataBase:
    def __init__(self):
        self.users = []
        
    def insert(self,user):
        i = 0
        while i< len(self.users):
            # find the first username greater than the new user's name
            if self.users[i].username > user.username:
                break
            i +=1
        self.users.insert(i,user)
    
    def find(self,username):
        for user in self.users:
            if user.username == username:
                return user
    def update(self,user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
    
    def list_all(self):
        return self.users
    
            
     


        
user = User("james123","James Corden", "john@doe.com")
user3 = User("blank","blanky", "Blank@james.com")
user3.introduce_yourself('Dav')

database = UserDataBase()

hemanth = User("hemanth", "CordsBowl", "jodog@dd.com")
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
siddhant = User("Telemis", "siddhantluvr123", "siddyoi@dd.com")

print(aakash)
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(user)
database.insert(user3)
database.list_all()
user = database.find("siddhant")

print(database.list_all())
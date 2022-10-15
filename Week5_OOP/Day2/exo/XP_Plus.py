#Exercise1
class Family:

    def __init__(self,last_name):
        self.last_name = last_name
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]

    def born(self, **kwargs):
        info = {
        }
        for i in kwargs:
            info.update({i : kwargs[i]})
        self.members.append(info)

    def is_18(self,name):
        for memb in self.members:
            if name == memb['name']:
                if memb['age'] > 18:
                    return True
                else:
                    return False
        return False

    def family_presentation(self):
        print(self.last_name)
        i = 1
        for memb in self.members:
            print(i,":",memb['name'])
            i+=1

famill = Family("Traore")
famill.born(name = 'isaac', age = 20, gender = 'Male', is_child=True)
famill.born(name = 'July', age = 2, gender = 'Female', is_child=True)
print(famill.is_18('Sarah'))
print(famill.is_18('July'))
famill.family_presentation()

#Exercise2

class TheIncredibles(Family):
    def __init__(self,lastname):
        super().__init__(lastname)
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
             'incredible_name': 'MikeFly'},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
             'incredible_name': 'SuperWoman'}
        ]
    def use_power(self, name):
        for memb in self.members:
            if name == memb['name']:
                if memb['age'] > 18:
                    print(f"{memb['power']}")
                else :
                    raise Exception(f"{name} don't have 18 yo yet")
            else:
                print(f"{name} is not member")

    def incredible_presentation(self):
        super().family_presentation()
        print('\nEach members of this family with his power : ')
        i = 1
        for memb in self.members:
            print(i,':',memb['power'])
            i += 1

famill = TheIncredibles("YAO")
famill.born(name = 'Jack', age = 5, gender = 'Male', is_child=True, power = 'Unknown Power', incredible_name= 'Baby')
famill.born(name = 'Marie', age = 15, gender = 'Female', is_child=True, power = 'Speak to animals', incredible_name= 'SuperWoman')
famill.incredible_presentation()



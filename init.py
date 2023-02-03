class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday


user = User("Olamide Aworetan", "19990719")  # date format yymmdd

print(user.name)
print(user.birthday)

while True:
    try:
        number = int(input('please enter a number :'))
        break

    except ValueError:
        print('You didn\'t enter a number')

    except:
        print('An unknown error occured')

print('Thank you for entering a number')



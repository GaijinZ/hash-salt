import hashlib
import uuid


def register(username, password):
    password_encode = password.encode('utf-8')
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(password_encode + salt.encode('utf-8')).hexdigest()
    if username == '' or hashed_password == '':
        return 'Username or password cannot be empty'
    elif username == ' ' or hashed_password == ' ':
        return 'Username or password cannot be empty'
    else:
        with open('users.txt', 'a') as f:
            f.write(f'{username}:{hashed_password}:{salt}\n')
            print(f'An account for {username} has been created.')


def login(username, password):
    with open('users.txt', 'r') as f:
        for line in f.readlines():
            log_info = line.rstrip().split(':')
            salt = log_info[2]
            hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
            if username in log_info[0] and hashed_password in log_info[1]:
                print(f'Logged in as {username} \n')
                return True
        print('No user in database\n')
        return check_database()


def check_database():
    while True:
        print('Choose a option: \n '
              '1 - to register\n '
              '2 - to login \n'
              'Choose any number to exit\n')
        choice = input("Your choice: ")
        if choice == '1':
            print('Enter username and password to register:')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            register(username, password)
        elif choice == '2':
            print('Enter yor username and password to login:')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            login(username, password)
            logout = input('Press 3 to logout:\n')
            if logout == '3':
                print('Logged out')
                break
            else:
                print('No function under this number')
        else:
            print('Wrong button')
            break


check_database()

# modules
import os
import webbrowser
from time import sleep
from colorama import Fore


# big space
def space():
    for space_ in range(100):
        print()

# line brack
def brack():
    print()
    print(Fore.RED + '_' * 50)
    print()
    sleep(0.500)

# user data entry
class ude:
    # help
    def help(self):
        brack()
        print(Fore.LIGHTBLUE_EX + '   Help Center')
        print()

        print(Fore.LIGHTGREEN_EX + "   This tool can save and review people's information.")
        print()

        print(Fore.LIGHTYELLOW_EX + "   :Personal information can be saved by 'Add User'.")
        print(Fore.LIGHTYELLOW_EX + "   :You can view and delete saved information using the name given to the 'search tag'.")
        print(Fore.LIGHTYELLOW_EX + "   :You have to enter the number of data you want to save to the 'data counter'.")
        print()

        print(Fore.LIGHTYELLOW_EX + "   :You can view the list of people's names currently saved through 'User List'.")
        print()

        print(Fore.LIGHTYELLOW_EX + "   :If you want to see the details of a previously saved person, you can go through 'View User' and give the relevant tag to the relevant person's data and view the information.")
        print()

        print(Fore.LIGHTYELLOW_EX + "   :If you want to remove the details of a previously saved person, you can go through 'Delete User' and remove the information by giving the relevant tag to the relevant person's data.")
        print()

        print(Fore.LIGHTYELLOW_EX + "   :You can access my GitHub account via 'Go'.")
        print()

        sleep(1)
        print()
        go_back = input(Fore.LIGHTCYAN_EX + '   [~]  ' + Fore.LIGHTYELLOW_EX + 'Go to home.? (Yes or No): ')

        if go_back == 'yes' or go_back == 'Yes' or go_back == 'YES':
            sleep(0.200)
            space()
            ude().home()

        elif go_back == 'no' or go_back == 'No' or go_back == 'NO':
            sleep(0.500)
            print(Fore.LIGHTRED_EX + '   :End user data entry...')
            sleep(0.500)
            exit()

        else:
            sleep(0.200)
            space()
            ude().home()

    # delete user
    def delete(self):
        brack()
        print(Fore.LIGHTBLUE_EX + '   Delete User Data')
        print()

        delete_tag = input(Fore.LIGHTCYAN_EX + '   [~]  ' + Fore.LIGHTYELLOW_EX + 'Enter Delete tag: ')
        if delete_tag in os.listdir('.save'):
            sleep(0.500)
            print(Fore.LIGHTRED_EX + '   :Deleting...')
            os.remove(f'.save/{delete_tag}/.data.json')
            os.rmdir(f'.save/{delete_tag}')
            sleep(1)
            print(Fore.LIGHTGREEN_EX + f"   '{delete_tag}' This tag all data delete done..!")
            sleep(3)
            space()
            ude().home()

        else:
            sleep(0.500)
            print(Fore.LIGHTRED_EX + f"   '{delete_tag}' This tag not exists")
            sleep(3)
            space()
            ude().home()

    # view user
    def view(self):
        brack()
        print(Fore.LIGHTBLUE_EX + '   View User Data')
        print()

        search_tag = input(Fore.LIGHTCYAN_EX + '   [~]  ' + Fore.LIGHTYELLOW_EX + 'Enter Search tag: ')
        if search_tag in os.listdir('.save'):
            print()
            with open(f'.save/{search_tag}/.data.json', 'r') as file:
                for data in file.readlines():
                    print(Fore.GREEN + '   :'+data.replace('\n', ''))

            sleep(1)
            print()
            go_back = input(Fore.LIGHTCYAN_EX + '   [~]  ' + Fore.LIGHTYELLOW_EX + 'Go to home.? (Yes or No): ')

            if go_back == 'yes' or go_back == 'Yes' or go_back == 'YES':
                sleep(0.200)
                space()
                ude().home()

            elif go_back == 'no' or go_back == 'No' or go_back == 'NO':
                sleep(0.500)
                print(Fore.LIGHTRED_EX + '   :End user data entry...')
                sleep(0.500)

            else:
                sleep(0.200)
                space()
                ude().view()

        else:
            print(Fore.RED + '   :This search tag not exists')
            sleep(2)
            space()
            ude().view()

    # user list
    def list(self):
        brack()
        print(Fore.LIGHTBLUE_EX + '   All User List')
        print()
        count = 1

        user = os.listdir('.save')
        for user_name in user:
            print(Fore.LIGHTCYAN_EX + f'   [{count}]  ' + Fore.LIGHTYELLOW_EX + user_name)
            count += 1


        sleep(1)
        print()
        go_back = input(Fore.LIGHTCYAN_EX + '   [~]  ' + Fore.LIGHTYELLOW_EX + 'Go to home.? (Yes or No): ')

        if go_back == 'yes' or go_back == 'Yes' or go_back == 'YES':
            sleep(0.200)
            space()
            ude().home()

        elif go_back == 'no' or go_back == 'No' or go_back == 'NO':
            sleep(0.500)
            print(Fore.LIGHTRED_EX + '   :End user data entry...')
            sleep(0.500)

        else:
            sleep(0.200)
            space()
            ude().list()

    # add user
    def add(self):
        brack()
        print(Fore.LIGHTBLUE_EX + '   Enter Your Details')
        print()
        search_tag = input(Fore.LIGHTCYAN_EX + '   [~]  ' + Fore.LIGHTYELLOW_EX + 'Search Tag: ')
        if len(search_tag) == 0:
            print(Fore.RED + '   :Search tag is empty')
            sleep(2)
            space()
            ude().add()

        elif search_tag in os.listdir('.save'):
            print(Fore.LIGHTRED_EX + '   :This tag already exists')
            sleep(2)
            space()
            ude().add()

        else:
                data_count = str(input(Fore.LIGHTCYAN_EX + '   [~]  ' + Fore.LIGHTYELLOW_EX + 'Data Count: '))

                if data_count == '0':
                    print(Fore.LIGHTRED_EX + '   :Zero value not valid')
                    sleep(2)
                    space()
                    ude().add()

                elif len(data_count) == 0:
                    print(Fore.LIGHTRED_EX + '   :Data count is empty')
                    sleep(2)
                    space()
                    ude().add()

                else:
                    try:
                        dc = int(data_count)
                        # create folder
                        os.mkdir(f'.save/{search_tag}')
                        print()
                        for add_data in range(dc):
                            data = input(Fore.BLUE + '   : ')

                            with open(f'.save/{search_tag}/.data.json', 'a') as file:
                                file.write(f'{data}\n')

                        print()
                        print(Fore.LIGHTGREEN_EX + '   :All data is save done..!')
                        sleep(2)
                        space()
                        ude().home()

                    except:
                        print(Fore.LIGHTRED_EX + '   :Please enter numbers only')
                        sleep(2)
                        space()
                        ude().add()

    # home screen
    def home(self):
        space()
        # banner
        sleep(0.700)
        print(Fore.LIGHTYELLOW_EX + "  _   _                 ____        _          _____       _                         ")
        print(" | | | |___  ___ _ __  |  _ \\  __ _| |_ __ _  | ____|_ __ | |_ _ __ _   _           ")
        print(Fore.LIGHTBLUE_EX + " | | | / __|/ _ \\ '__| | | | |/ _` | __/ _` | |  _| | '_ \\| __| '__| | | |         ")
        print(" | |_| \\__ \\  __/ |    | |_| | (_| | || (_| | | |___| | | | |_| |  | |_| |         ")
        print(Fore.LIGHTYELLOW_EX + "  \\___/|___/\\___|_|    |____/ \\__,_|\\__\\__,_| |_____|_| |_|\\__|_|   \\__, |    ")
        print(Fore.LIGHTYELLOW_EX + "                                                                    |___/            ")

        # tool created by akiyah
        sleep(0.300)
        print(Fore.RED + '  \033[4m' + 'Tool created by akiyah' + '\033[0m')
        print()
        print()

        # add user
        sleep(0.300)
        print(Fore.LIGHTCYAN_EX + '   [01]  ' + Fore.LIGHTYELLOW_EX + 'Add User')
        print(Fore.LIGHTCYAN_EX + '   [02]  ' + Fore.LIGHTYELLOW_EX + 'User List')
        print(Fore.LIGHTCYAN_EX + '   [03]  ' + Fore.LIGHTYELLOW_EX + 'View User')
        print(Fore.LIGHTCYAN_EX + '   [04]  ' + Fore.LIGHTYELLOW_EX + 'Delete User')
        print(Fore.LIGHTCYAN_EX + '   [05]  ' + Fore.LIGHTYELLOW_EX + 'Help')
        print(Fore.LIGHTCYAN_EX + '   [06]  ' + Fore.LIGHTYELLOW_EX + 'Exit')
        print()
        print(Fore.LIGHTCYAN_EX + '   [00]  ' + Fore.LIGHTYELLOW_EX + 'Go')
        print()
        print()

        # user input option
        user_input = input(Fore.LIGHTCYAN_EX + '   [~]  ' + Fore.LIGHTYELLOW_EX + 'Select an option: ')



        # input process
        if user_input == '1' or user_input == '01' or user_input == 'Add User' or user_input == 'Add user' or user_input == 'add user' or user_input == 'ADD USER':
            ude().add()

        elif user_input == '2' or user_input == '02' or user_input == 'User List' or user_input == 'User list' or user_input == 'user list' or user_input == 'USER LIST':
            ude().list()

        elif user_input == '3' or user_input == '03' or user_input == 'View User' or user_input == 'View user' or user_input == 'view user' or user_input == 'VIEW USER':
            ude().view()

        elif user_input == '4' or user_input == '04' or user_input == 'Delete User' or user_input == 'Delete user' or user_input == 'delete user' or user_input == 'DELETE USER':
            ude().delete()

        elif user_input == '5' or user_input == '05' or user_input == 'Help' or user_input == 'help' or user_input == 'HELP':
            ude().help()


        elif user_input == '6' or user_input == '06' or user_input == 'Exit' or user_input == 'exit' or user_input == 'EXIT':
            sleep(0.500)
            print(Fore.LIGHTRED_EX + '   :End user data entry...')
            sleep(0.500)

        elif user_input == '0' or user_input == '00' or user_input == 'Go' or user_input == 'go' or user_input == 'GO':
            webbrowser.open('https://github.com/akalankar')
            space()
            ude().home()

        elif len(user_input) == 0:
            print(Fore.LIGHTRED_EX + '   :Please select an any option')
            sleep(2)
            space()
            ude().home()

        else:
            print(Fore.LIGHTRED_EX + '   :You select option is incorrect')
            sleep(2)
            space()
            ude().home()



if __name__ == '__main__':
    if '.save' in os.listdir():
        ude().home()
    else:
        os.mkdir('.save')
        ude().home()

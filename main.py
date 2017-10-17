import global_list
import window
import common
import sys

if __name__ == '__main__':
    # window.CreatWindow()
    
    common.LoadPassword()
    # global_list.PassWordList = []
    print(global_list.PassWordList)

    passwordline = {'catagory':'one',
                    'name':'fun',
                    'web':'www.google.com',
                    'account':'funsimple',
                    'password':'forever'}
    common.SavePassword(passwordline)
    print(global_list.PassWordList)

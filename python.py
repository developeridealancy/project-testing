import os
import time 
def pull_changes_from_server():
    '''this function is use to pull changes from the remote server'''

    response = os.system("git fetch origin")
    if response == 128 :
        print('internet connection error, Problem in getting new updates .1')
        return
    if response is not 0:
        print('Problem in getting new updates .1')
        return

    response = os.system(f"git merge origin/master")
    if response is not 0:
        print('Problem in getting new updates .2')
        return
    # if every thing set return no problem
    print('_______________Finish___________________')

pull_changes_from_server()
time.sleep(60)
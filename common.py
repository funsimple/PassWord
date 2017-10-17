import global_list
import pickle
def SavePassword(passwordline):
    GetNameList()
    if passwordline['name'] in global_list.NameList:
        pass
    else:
        global_list.PassWordList.append(passwordline)
    with open('passwordline.pw', 'wb') as f:
        pickle.dump(global_list.PassWordList,f)

def LoadPassword():
    with open('passwordline.pw', 'rb') as f:
        if(len(f.read()) != 0):
            f.seek(0)
            global_list.PassWordList = pickle.load(f)

def GetNameList():
    global_list.NameList = []
    for passwordline in global_list.PassWordList:
        global_list.NameList.append(passwordline['name'])


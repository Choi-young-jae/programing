__author__ = 'user'

def CreateHexList(): # 각 자릿수해 해당하는 자리에 각각의 숫자를 넣는다
    hexList = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return hexList

def ChangeDecToHex(decnumber,hexList):
    printList = [] # 출력될 문자를 저장할 리스트를 생성
    while(True):
        if(decnumber<=0):
            break
        printList.append(hexList[decnumber%16])
        decnumber //=16
    printList.append("Ox")
    return printList
def Transfome(decnumber):
    #print(hex(decnumber))
    hexList = CreateHexList()
    changenumber = ChangeDecToHex(int(decnumber),hexList)
    changenumber.reverse()
    for hexnum in changenumber:
        print(hexnum,end="")
    print()
    while(True):
        yesno = input("continue ? (yes or no)")
        if(yesno=='no'):
            return 'no'
        elif(yesno !='yes'):
            print("Wrong input. pleas reinput")
        else:
            return 'yes'
if __name__ == "__main__":
    while(True):
        try:
            decnumber = int(input("input the decnumber"))
        except ValueError:
            print("Plese input number, not literal")
        else:
            yesno = Transfome(decnumber)
            if(yesno=='no'):
                break




	

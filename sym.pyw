from imagesearch import *
import time
from tkinter import *
from plyer import notification

root = Tk()
root.iconbitmap(default = './symbol.ico')
root.title("심알바")
root.geometry("250x200")
root.resizable(True, True)

def start__sym():
    print("심알리미 시작")
    sym__cool = int(cool.get("1.0", END))
    print(sym__cool)
    run__sym(sym__cool)

def run__sym(cool):
    while True:
        pos = imagesearch("./sym.png")
        if pos[0] != -1:
            print("홀심 매칭 성공")
            print("position : ", pos[0], pos[1])
            pos = 0
            print("cool만큼 잡니다zzz")
            time.sleep(cool+1)

            notification.notify(
                title='심알바',
                message='심이 끝났습니다',
                app_icon='./symbol.ico',
                app_name="SymAlba",
                timeout=5,
            )
        else:
            print("image not found")

label1 = Label(root, text = "※사용법※\n1. 5시방향 단축키 슬롯에서 심 없는지 확인\n2. 심쿨 입력\n3. 시작\n\n※주의사항※\n스킬창 열어 심 보이는경우 그것도 인식됨\n프로그램 종료시 강제종료\nexe,png,ico 파일이 같이있어야 동작")
label1.pack()

cool = Text(root, width=6, height= 1)
cool.insert(END, "쿨입력")
cool.pack()

ok__btn = Button(root, text="시작", command=start__sym)
ok__btn.pack()

root.mainloop()


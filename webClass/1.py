from tkinter import *

def fact(e=99):
    n = int(en_input.get())
    res=1;
    for i in range(1,n+1):
        res = res * i;
    lbl_result.configure(text=str(res))        
    #return res;

#x = int(input())
#print(fact(x))

w = Tk()
w.title('팩토리얼 계산 프로그램')

en_input = Entry(w)
en_input.bind('<Return>',fact)
#btn_ok = Button(w,text='계산')
lbl_result = Label(w,text='여기에 답 표시')

en_input.pack()
#btn_ok.pack(fill='x')
lbl_result.pack()

w.mainloop()

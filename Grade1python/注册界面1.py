from tkinter import *
def helloButton():
    n1=e1.get()
    n2=e2.get()
    n3=e3.get()
    n4=e4.get()
    t1=len(n1)
    t2=len(n2)
    t3=len(n3)
    t4=len(n4)
    if n1!=''and n2!=''and n3!=''and n4!='':
        e1.delete(0,t1)
        e2.delete(0,t2)
        e3.delete(0,t3)
        e4.delete(0,t4)
        print('新注册了一个用户：')
        print('用户名是：',n1)
        print('密码是:',n2)
        print('电子邮箱地址是：',n3)
        print('手机号是：',n4)
        l5['text']=''
        l5['bg']='SystemButtonFace'
    else:
        l5['text']='有项目未填写！'
        l5['bg']='red'
top = Tk()
top.title('注册界面')
height=369
l1=Label(top,text='用户名').grid(row=0)
e1=Entry(top)
e1.grid(row=0,column=1)
l2=Label(top,text='密码').grid(row=1)  
e2=Entry(top,show='*')
e2.grid(row=1,column=1)
l3=Label(top,text='电子邮箱').grid(row=2)  
e3=Entry(top)
e3.grid(row=2,column=1)
l4=Label(top,text='手机号').grid(row=3)  
e4=Entry(top)
e4.grid(row=3,column=1)
l5=Label(top,text='')
l5.place(x=60,y=95)
l6=Label().grid()
l7=Label().grid()
l8=Label().grid()
Button(top,text = '提交',anchor='c',width=6,height=1,command = helloButton).place(x=75,y=118)
top.mainloop()

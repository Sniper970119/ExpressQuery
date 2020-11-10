# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃CREATE BY SNIPER┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛

"""
import tkinter as tk
import tkinter
import time
from tkinter import *
from tkinter import ttk
from get_info import get_data


class View(tk.Tk):
    def __init__(self):
        super(View, self).__init__()
        self.kuaidi_list = ['顺丰', '中通', '申通', '韵达', '圆通']
        self.company_res = []
        self.cno_res = []
        self.time_list = []
        self.loc_list = []
        # self.overrideredirect(True)
        self.attributes("-alpha", 0.5)  # 窗口透明度60 %
        self.geometry("300x200+-300+50")
        self.wm_attributes('-topmost', 1)
        self.tm_cur = tk.StringVar()
        self.tm_cur.set('120')
        self.first = True

        def click_btn1():
            # root.geometry("500x500+000+50")
            global company_res, cno_res
            sub = Toplevel()
            sub.title('快递信息')
            sub.geometry("230x200+500+50")
            nub_label = Label(sub, text='快递个数：')
            nub_label.place(x=0, y=20, anchor='nw')
            nub_combobox = ttk.Combobox(sub, width=5)
            nub_combobox['value'] = [i + 1 for i in range(7)]
            nub_combobox.place(x=60, y=20, anchor='nw')

            def click_nub_combobox(event):
                # global company_res, cno_res
                nub = int(nub_combobox.get())
                length = str(100 * nub + 100)
                sub.geometry("230x" + str(length) + "+500+50")
                base_line = 100
                company_list = []
                cno_list = []
                for i in range(nub):
                    temp_label1 = Label(sub, text='公司')
                    temp_label1.place(x=0, y=60 + base_line * i, anchor='nw')
                    temp_label2 = Label(sub, text='单号')
                    temp_label2.place(x=0, y=90 + base_line * i, anchor='nw')
                    company_list.append(ttk.Combobox(sub, width=10))
                    company_list[i]['value'] = self.kuaidi_list
                    company_list[i].current(0)
                    company_list[i].place(x=60, y=60 + base_line * i, anchor='nw')
                    cno_list.append(Entry(sub, width=15))
                    cno_list[i].place(x=60, y=90 + base_line * i, anchor='nw')

                def click_btn2():
                    # global company_res, cno_res
                    for i in range(len(company_list)):
                        self.company_res.append(company_list[i].get())
                        self.cno_res.append(cno_list[i].get())
                    length = len(self.company_res) * 150 + 100
                    self.geometry("300x" + str(length) + "+-300+50")
                    self.refresh_data()
                    # self.refresh_time()
                    sub.destroy()

                btn2 = tkinter.Button(sub, text='确定', command=click_btn2)
                btn2.place(x=150, y=17, anchor='nw')

            nub_combobox.bind("<<ComboboxSelected>>", click_nub_combobox)

        btn1 = tkinter.Button(self, text='输入快递信息', command=click_btn1)
        btn1.place(x=200, y=20, anchor='nw')

        self.mainloop()

    def change_root(self):
        base_line = 100
        # print(len(self.company_res))

        for i in range(len(self.company_res)):
            res = get_data(self.company_res[i], self.cno_res[i])[-1]
            temp_label1 = Label(self, text='公司:' + str(self.company_res[i]))
            temp_label1.place(x=0, y=60 + base_line * i, anchor='nw')
            temp_label2 = Label(self, text='单号:' + str(self.cno_res[i]))
            temp_label2.place(x=100, y=60 + base_line * i, anchor='nw')
            self.time_list.append(StringVar())
            self.time_list[i].set('更新时间:' + str(res[0]))
            self.loc_list.append(StringVar())
            self.loc_list[i].set('最新动态:' + str(res[1]))
            if self.first:
                temp_label3 = Label(self, textvariable=self.time_list[i])
                temp_label3.place(x=00, y=80 + base_line * i, anchor='nw')
                temp_label4 = Label(self, textvariable=self.loc_list[i])
                temp_label4.place(x=00, y=100 + base_line * i, anchor='nw')
            # self.time_list.append(StringVar())
            # temp_label3 = Label(self, text='更新时间:' + str(res[0]))
            # self.time_list[i].place(x=00, y=80 + base_line * i, anchor='nw')
            # temp_label4 = Label(self, textvariable='最新动态:' + str(res[1]))
            # temp_label4.place(x=00, y=100 + base_line * i, anchor='nw')

    def refresh_data(self):
        # print('refresh_data')
        self.change_root()
        self.after(2000 * 60, self.refresh_data)

    def refresh_time(self):
        # print('refrash time')
        nub = int(self.tm_cur.get())
        tm_label = Label(self, text='刷新倒计时：')
        tm_label.place(x=150, y=150 + 100 * len(self.company_res), anchor='nw')

        tm = Label(self, textvariable=self.tm_cur)
        tm.place(x=220, y=150 + 100 * len(self.company_res), anchor='nw')
        if nub - 1 == 0:
            nub = 120
        nub -= 1
        self.tm_cur.set(str(nub))
        self.after(1000, self.refresh_time)


if __name__ == '__main__':
    View()

# encoding: utf-8
"""
运行之后会出一个窗口，按钮点击会改变复选菜单的被选中状态，复选菜单是否被选中看前面是否有√。
点击复选菜单会打印被选中状态，注意点击之后是先变更状态后打印状态。
"""

from tkinter import *


def change_check_button_state(evet):
    """改变复选菜单的被选中状态"""
    if var.get() == 0:
        var.set(1)
    else:
        var.set(0)


def print_check_button_state():
    """打印复选菜单是否被选中"""
    print("check button state: {}".format(var.get()))

# 主窗口
root = Tk()
root.wm_minsize(200, 100)

# 菜单栏
menu = Menu(root)
# 一级菜单，就是记事本中的"文件","编辑","格式"
menu_check = Menu(menu)
# ********** 注意：这个 var 对象是重点 **********
var = IntVar()
# 添加复选菜单
menu_check.add_checkbutton(label="check1", command=print_check_button_state, variable=var)
# 设置一级菜单
menu.add_cascade(label="check", menu=menu_check)
# 设置菜单栏
root["menu"] = menu

btn = Button(root, text="change check state")
btn.bind("<Button-1>", change_check_button_state)
btn.pack()

# 主循环
root.mainloop()
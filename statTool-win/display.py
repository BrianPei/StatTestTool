# coding:utf-8

from driver import *
from reporter import *
from Tkinter import *
from ConfigParser import *
import sys
import os
import threading
import tkMessageBox

reload(sys)
sys.setdefaultencoding('utf8')

driver = Driver()
reporter = Reporter()

config_path = os.path.join(
    os.path.split(os.getcwd())[0], 'config', 'config.ini')
conf = ConfigParser()
conf.read(config_path)


def load_actions():
    return conf.options('actions')


def run(event):
    driver.clear_stat()
    action_selected = []
    excute_count = int(count_win.get())
    for x in action_list.curselection():
        action_name = action_list.get(x)
        action_ID = conf.get('actions', (action_name))
        action_selected.append(action_ID)
    runner = threading.Thread(
        target=excute, args=(
            action_selected, excute_count))
    runner.setDaemon(True)
    reporter.set_start_time()
    runner.start()
    runner.join()
    tkMessageBox.showinfo('message', '运行完毕')


def excute(actions, count):
    global flag
    for x in actions:
        print x
        action = getattr(driver, x)
        action(count)
    reporter.set_end_time()
    driver.teardown()


def show_result(event):
    result_list.delete(0, END)
    for key in driver.stat_count:
        result_list.insert(END, "%d: %d" % (key, driver.stat_count[key]))


def update_result(event):
    reporter.sort_params(driver.stat_count)
    reporter.post_data()


# 定义主界面标题和窗口大小
root = Tk(className='数据统计自动化测试工具')
root.geometry('800x600')

# 生成按钮
button_frame = Frame(root)
button_frame.pack(side=TOP, pady=30)

run_button = Button(button_frame, width=20, text='运行')
run_button.bind('<Button-1>', run)
run_button.pack(side=LEFT, padx=20)
show_button = Button(button_frame, width=20, text='显示结果')
show_button.bind('<Button-1>', show_result)
show_button.pack(side=LEFT, padx=20)
update_button = Button(
    button_frame, width=20, text='上传数据')
update_button.bind('<Button-1>', update_result)
update_button.pack(side=RIGHT, padx=20)

# 动作列表
action_frame = Frame(root)
action_frame.pack(side=LEFT, padx=50, ipady=20)

action_label = Label(action_frame, text='事件列表')
action_label.pack()

action_list = Listbox(
    action_frame, selectmode=MULTIPLE, height=25, width=35)
# 读取配置文件中的action列表并显示
actions = load_actions()
for action in actions:
    action_list.insert(END, action)
# action_list.selection_set(0, action_list.size())
action_list.pack()

# 操作次数设定
count_frame = Frame(root)
count_frame.pack(side=LEFT, padx=10, ipady=220)
count_label = Label(count_frame, text='请输入运行次数')
count_win = Entry(count_frame, width=10)
count_label.pack()
count_win.pack()

# 结果列表
result_frame = Frame(root)
result_frame.pack(side=RIGHT, padx=50, ipady=20)

result_label = Label(result_frame, text='结果列表')
result_label.pack()

result_list = Listbox(result_frame, height=25, width=35)
result_list.pack()

# 显示界面
root.mainloop()

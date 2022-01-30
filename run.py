import win32api
import win32con
import win32gui
import win32process
import time
import json
import os

config = ["{\"video_dir\": \"\"}"]
if not os.path.exists("config.json"):
    print("找不到config.json。正在创建...")
    with open("config.json", mode="w") as newconf:
        newconf.writelines(config)
try:
    with open("config.json", encoding="utf-8") as conf:
        a = json.load(conf)
        videodir = a["video_dir"]
except:
    print("无法读取config.json.")
    pass

param = f"{videodir} -noborder -x 1920 -y 1080 -loop 0"


def hide(hwnd, hwnds):
    hdef = win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None)  # 枚举窗口寻找特定类
    if hdef != 0:
        workerw = win32gui.FindWindowEx(0, hwnd, "WorkerW", None)  # 找到hdef后寻找WorkerW
        win32gui.ShowWindow(workerw, win32con.SW_HIDE)  # 隐藏WorkerW
        while True:
            time.sleep(100)  # 进入循环防止壁纸退出
    else:
        return


os.popen(f"ffplay {param}")
time.sleep(0.5)
print("aaaa")
progman = win32gui.FindWindow("Progman", "Program Manager")  # 寻找Progman
win32gui.SendMessageTimeout(progman, 0x52C, 0, 0, 0, 1000)  # 发送0x52C消息
videowin = win32gui.FindWindow("SDL_app", None)  # 寻找ffplay 播放窗口
win32gui.SetParent(videowin, progman)  # 设置子窗口
win32gui.EnumWindows(hide, None)  # 枚举窗口，回调hide函数

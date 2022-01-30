# PyWallpaperEngine

Windows动态壁纸的Python实现。仅支持Windows操作系统。

## 使用
安装`pywin32`模块：  
```
pip install pywin32
```
前往[ffmpeg 官网](https://ffmpeg.org)等地方下载`ffplay.exe`并放入`run.py`所在目录或PATH目录。  
然后使用python3运行。初次运行后，在`config.json`中的`video_dir`键的值输入视频路径（需要2个反斜杠）。  
再次运行后即可看到动态壁纸。关闭控制台窗口即可终止。
# 特别鸣谢
代码修改自 Bilibili [@偶尔有点小迷糊](https://space.bilibili.com/39665558) 。
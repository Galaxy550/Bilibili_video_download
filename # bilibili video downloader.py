# bilibili video downloader 最终模式。

pattern=int(input("输入想要选择的模式:1.本地模式 2.在线模式: "))

import os
import sys

# 获取脚本所在的绝对路径（无论从哪里运行）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 输出文件固定放在脚本旁边
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "output.mp4")



if pattern==1:
    import re

    file=input("请输入包含视频信息的文件路径: ")
    with open(rf"{file}", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 匹配 Video
    video_pattern = r'"baseUrl":"(https://upos[^"]+)"'
    # 2. 匹配 Audio
    audio_pattern = r'"audio".*?"baseUrl":"(https://[^"]+)"'

    # 提取并处理转义字符
    video_urls = [u.replace(r'\/', '/') for u in re.findall(video_pattern, content)]
    audio_urls = [u.replace(r'\/', '/') for u in re.findall(audio_pattern, content)]



    print("--- 视频链接 ---")
    for url in video_urls: print(url)

    print("\n--- 音频链接 ---")
    for url in audio_urls: print(url)


    import subprocess
    quality=int(input("请输入视频画质质量(1-8),数字越大越模糊:"))
    if 1<=quality<=8:
        headers = (
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\r\n"
        "Referer: https://www.bilibili.com/\r\n"
        )
        output = os.path.join(SCRIPT_DIR, "output.mp4")
        # 构造命令
        # 注意：-headers 参数必须放在 -i 的前面！
        cmd = [
            'ffmpeg',
            '-headers', headers,
            '-i', video_urls[quality-1],
            '-headers', headers,
            '-i', audio_urls[0],
            '-c', 'copy',
            '-y',  # 覆盖已存在的文件
            output
        ]

        # 执行
        subprocess.run(cmd)
        # 伪装的请求头
    else:
        print("无效的输入，请输入 1-8 之间的数字。")

elif pattern==2:

    import json
    import requests

    # 1. 提取参数的部分
    js_file = input("请输入包含视频信息的 JSON 文件路径: ")
    with open(rf"{js_file}", 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 提取必要信息
    aid = data['data']['aid']
    cid = data['data']['cid']
    bvid = data['data']['bvid']

    print(f"提取成功 -> aid: {aid}, cid: {cid}, bvid: {bvid}")

    # 2. 定义函数
    def get_video_stream(aid, cid, bvid, sessdata):
        url = "https://api.bilibili.com/x/player/playurl"
        
        
        params = {
            "aid": aid,
            "cid": cid,
            "bvid": bvid,
            "qn": "80",                
            "platform": "html5",
            "otype": "json"
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": f"https://www.bilibili.com/video/{bvid}/",
            "Cookie": f"SESSDATA={sessdata}"
        }
        
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    # 3. 接收用户输入并调用
    sessdata = input("请输入你的 SESSDATA(从浏览器 cookie 中获取),这是敏感信息，不要泄露给他人！: ") #

    # 在这里调用函数并传入你刚才提取的 aid, cid, bvid
    result_data = get_video_stream(aid, cid, bvid, sessdata)

    # 4. 打印结果看看是否成功
    if result_data['code'] == 0:
        print("请求成功！视频流信息如下：")
        video_url = result_data['data']["durl"][0]["url"]
        print(f"视频链接: {video_url}")

        # 5. 使用 ffmpeg 下载视频
        import subprocess
        headers = (
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\r\n"
            "Referer: https://www.bilibili.com/\r\n"
        )
        output = os.path.join(SCRIPT_DIR, "output.mp4")
        cmd=["ffmpeg","-headers", headers, "-i", video_url, "-c", "copy","-y", output]
        subprocess.run(cmd)

    else:
        print(f"请求失败，错误代码: {result_data['code']}, 错误信息: {result_data.get('message')}")
    
else:
    print("无效的输入，请输入 1 或 2。")

import platform



#窗口显示

def pause():
    """按任意键退出，兼容 Windows/Linux/Mac"""
    print("\n✅ 运行完成！按任意键退出...")
    
    if platform.system() == "Windows":
        import msvcrt
        msvcrt.getch()
    else:
        # Linux/Mac 用 input，因为 getch 需要额外安装
        input()

# 程序最后调用
pause()    
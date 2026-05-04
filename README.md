# Bilibili_video_download
Bilibili 视频下载工具 | 支持本地解析与在线 API 两种模式，自动提取视频/音频流并合并
# 🎬 Bilibili Video Downloader

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

一个简单易用的 **Bilibili 视频下载工具**，支持**本地 JSON 解析**和**在线 API 获取**两种工作模式，自动提取视频/音频流并通过 `ffmpeg` 合并输出。

---

## ✨ 功能特性

| 功能 | 说明 |
|:---|:---|
| 🔄 **双模式支持** | 本地模式：从reqable抓取的文件提取直链；在线模式：通过 B站 API 获取视频流 |
| 🎵 **音视频自动合并** | 高清视频（mp4文件）自动分离下载视频 + 音频并合并 |
| 🎨 **画质可选** | 本地模式支持多清晰度选择（1-N，数字越大画质越低） |
| 📁 **智能输出** | 自动处理文件名冲突，输出文件固定保存在脚本目录 |
| 🖥️ **跨平台** | 支持 Windows / Linux / macOS（Windows 推荐双击运行） |

---

## 📦 环境要求

- **Python** 3.8 或更高版本
- **ffmpeg**（必须安装并添加到系统 PATH）

### 安装 ffmpeg

| 平台 | 方式 |
|:---|:---|
| **Windows** | [官网下载](https://ffmpeg.org/download.html) → 解压 → 添加到 PATH |
| **macOS** | `brew install ffmpeg` |
| **Linux** | `sudo apt install ffmpeg` |

验证安装：
```bash
ffmpeg -version

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/galaxy550/bilibili-video-downloader.git
cd bilibili-video-downloader
```

### 2. 安装依赖

- 需自行安装好 [ffmpeg](https://ffmpeg.org/download.html) 并添加到系统 PATH

```bash
pip install requests
```

### 3. 运行程序

```bash
python bilibili_downloader.py
```

或 **直接双击** `bilibili_downloader.py` 运行（Windows）

---

## 使用说明

启动后选择模式：

```
输入想要选择的模式: 1.本地模式 2.在线模式:
```

### 模式 1：本地模式

适用于已有 B站视频 **抓包数据** 的情况（如从浏览器开发者工具复制）。

1. 在 [Reqable](https://reqable.com/) 中将包含视频信息的 JSON 保存为文本文件
2. 输入文件路径
3. 选择画质质量（`1-N`，1 为最高清）
4. 等待下载完成

### 模式 2：在线模式

通过 B站 API 直接获取视频流。

1. 输入视频的BV号
2. 输入浏览器 Cookie 中的 `SESSDATA`（用于获取高清/会员视频）
3. 自动解析并下载

#### 如何获取 SESSDATA？

1. 登录 [Bilibili](https://www.bilibili.com)
2. 按 `F12` 打开开发者工具 → **Application/应用** → **Cookies**
3. 找到 `SESSDATA` 字段，复制其值

> ⚠️ **注意**：SESSDATA 是敏感信息，请勿分享给他人！

---

## 输出文件

- **默认输出**：`output.mp4`（保存在脚本同级目录）
- **若文件已存在**：会自动覆盖！！！

---


本工具仅供学习交流使用，请勿用于侵犯版权或违反 B站用户协议的行为。下载的视频版权归 Bilibili 及原作者所有。

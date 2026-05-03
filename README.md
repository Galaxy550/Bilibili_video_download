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
| 🔄 **双模式支持** | 本地模式：从 JSON 文件提取直链；在线模式：通过 B站 API 获取视频流 |
| 🎵 **音视频自动合并** | 高清视频（DASH 格式）自动分离下载视频 + 音频并合并 |
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

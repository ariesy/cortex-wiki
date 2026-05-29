---
pageType: entity
entityType: project
id: entity.project.bilibili-all-in-one
updatedAt: "2026-05-29"
---

# bilibili-all-in-one

> B站内容创作自动化技能，支持视频下载/字幕/上传发布

**类型:** Skill  
**状态:** active  
**ID:** `skill_bilibili_all_in_one`  
**来源:** 2026-04-18配置使用

---

## 基本信息

| 项目 | 内容 |
|------|------|
| **位置** | `~/.openclaw/skills/bilibili-all-in-one` |
| **技术栈** | bilibili-api-python, httpx |
| **状态** | 已配置 |

---

## 账号信息

| 项目 | 内容 |
|------|------|
| **账号** | siruisprime |
| **UID** | 156608903 |
| **等级** | 4（正式会员） |
| **AppID** | wxda9df95ffd06d8e8 |

---

## 功能模块

| 模块 | 功能 |
|------|------|
| 🔥 Hot Monitor | 热门视频监控 |
| ⬇️ Downloader | 视频下载 |
| 👀 Watcher | 观看追踪 |
| 📝 Subtitle | 字幕下载 |
| ▶️ Player | 播放/弹幕 |
| **📤 Publisher** | **视频上传发布** ✅ 已配置 |

---

## 已上传视频

| 标题 | BV号 | 日期 |
|------|------|------|
| 梦游的小黄鸭 - 原创儿歌 | BV1VxdnBHExL | 2026-04-18 |
| 梦游的小黄鸭 - 原创儿童儿歌 | BV1h8dnBUEZ9 | 2026-04-18 |

---

## 已知Bug

| Bug | 说明 | 状态 |
|-----|------|------|
| `bug_bilibili_audio_uploader` | AudioUploader库bug (AttributeError) | known_issue，需用publisher |

---

*来源: memory/2026-04-18-bilibili-upload-config.md*
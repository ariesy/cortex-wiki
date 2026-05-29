---
pageType: entity
entityType: bug
id: entity.bug.bilibili-audio-uploader
updatedAt: "2026-05-29"
relationships:
  - targetId: entity.project.bilibili-audio-uploader
    targetTitle: "bilibili-audio-uploader"
    kind: affects
    weight: 0.8
---


# bilibili-api-python AudioUploader bug

> AudioUploader库存在AttributeError，需使用publisher替代

**类型:** Bug  
**ID:** `bug_bilibili_audio_uploader`  
**状态:** known_issue  
**来源:** bilibili上传调研

---


## 问题描述

使用 `bilibili_api.audio_uploader` 进行音频上传时出现错误：

```
AttributeError: 'AudioUploaderEvents' object has no attribute 'upper'
```

---

## 根因

`AudioUploaderEvents.PRE_COVER` 被当作字符串使用时，库本身存在bug。

---

## 临时解决方案

使用 `publisher`（视频上传接口）而非 `audio_uploader` 进行上传。

---

## 验证状态

✅ MP4视频上传已成功：
- 梦游的小黄鸭 - 原创儿童儿歌 (BV1h8dnBUEZ9)

❌ 音频上传因库bug暂不可用

---

*来源: memory/2026-04-18-bilibili-upload-config.md*
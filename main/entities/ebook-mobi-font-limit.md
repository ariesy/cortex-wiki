---
pageType: entity
entityType: bug
id: entity.bug.ebook-mobi-font-limit
updatedAt: "2026-05-29"
relationships:
  - targetId: entity.project.ebook-mobi-font-limit
    targetTitle: "ebook-mobi-font-limit"
    kind: affects
    weight: 0.8
---


# MOBI格式字体大小48px硬限制

> entity_type: bug

**类型:** Bug  
**ID:** `bug_ebook_mobi_font_limit`  
**状态:** fixed ✅  
**日期:** 2026-05-20  
**来源:** MEMORY.md

---


## 问题描述

MOBI格式对字体大小有48px硬限制，AZW3分页混乱。

---

## 解决方案

改用 **PDF格式** 输出，使用 weasyprint 转换。

---

## 最终排版参数（Paperwhite 2）

| 参数 | 数值 |
|------|------|
| 页面尺寸 | 90.8mm × 122.6mm |
| 屏幕分辨率 | 758×1024px |
| 汉字区域 | 145pt高，字体90pt |
| 下方左右分栏 | 左词/右句 |
| 颜色 | 全纯黑，无灰度 |

---

*来源: MEMORY.md*

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->

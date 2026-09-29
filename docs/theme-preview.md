---
title: 主题样式预览
---

# 主题样式预览

本页用于检查亮色 / 暗色两种模式下的整体效果。**请点击右上角主题切换按钮，分别核对两种模式。** 确认模板无需调整后，可删除本文件。

## 排版基础

一段中英混排的正文示例。VitePress is a Static Site Generator built on Vite. 这里的行高、字距与两端对齐均由 `base.css` 控制。行内代码如 `npm run dev` 会使用品牌色与软背景。

### 三级标题

> 引用块：这里展示了 blockquote 的圆角与软背景样式。

## 链接与强调

一个[站内链接](/about/)，以及**加粗**、*斜体*、~~删除线~~。

## 代码块

```ts
// docs/.vitepress/theme/styles/vars.css
:root {
  --vp-c-brand-1: #4653d6; /* 亮色主品牌色 */
}

.dark {
  --vp-c-brand-1: #8f9bff; /* 暗色下提亮 */
}
```

```python
def hello(name: str) -> str:
    """Python 代码块示例"""
    return f"Hello, {name}!"
```

## 表格

| 模块 | 文件 | 职责 |
| ---- | ---- | ---- |
| 设计令牌 | `vars.css` | 品牌 / 背景 / 文字 / 边框，亮暗两套 |
| 基础排版 | `base.css` | 正文行高、选中态、滚动条 |
| 首页 | `home.css` | Hero 渐变标题、卡片悬浮 |
| 组件 | `components.css` | 导航毛玻璃、代码块、表格斑马纹 |

## 自定义容器

::: info 说明
信息容器：一般性提示。
:::

::: tip 提示
提示容器使用品牌色淡底。
:::

::: warning 注意
警告容器。
:::

::: danger 危险
危险容器。
:::

## 列表

- 无序列表项一
- 无序列表项二
  - 嵌套项

1. 有序列表项一
2. 有序列表项二

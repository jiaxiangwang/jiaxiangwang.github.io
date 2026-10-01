import { defineConfig } from 'vitepress'
import { sidebar } from './sidebar'
import { mathjax3 } from './math'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: 'zh-CN',
  title: 'Jasper的个人笔记',
  description: 'not just the code, but the reasons behind it. code. eat. sleep. loop',
  cleanUrls: true,
  lastUpdated: true,
  markdown: {
    config(md) {
      md.use(mathjax3 as any)
    },
  },
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/logo.png' }],
    // 全站不被搜索引擎收录
    ['meta', { name: 'robots', content: 'noindex, nofollow, noarchive, noimageindex' }],
    // 防闪现：HTML 到达即隐藏 #app（内联样式，不等外部 CSS），
    // AccessGate 挂载后移除 gate-hold 类揭示页面（登录遮罩本身就是不透明的）
    ['script', { id: 'gate-hold' }, `document.documentElement.classList.add('gate-hold')`],
    ['style', { id: 'gate-hold-style' }, `html.gate-hold #app{visibility:hidden}`],
  ],

  themeConfig: {
    logo: '/logo.png',
    // 添加内容目录后，运行 `python3 scripts/vp_sidebar.py` 生成 sidebar.ts
    sidebar,
    nav: [
      { text: '首页', link: '/' },
      { text: 'CFA 2027', items: [
        { text: '学习中心', link: '/cfa/' },
        { text: 'Review Course', link: '/cfa/review/' },
        { text: 'Question Bank', link: '/cfa/questions/' },
      ] },
      { text: '关于', link: '/about/' },
    ],
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索文档', buttonAriaLabel: '搜索文档' },
          modal: {
            noResultsText: '未找到相关结果',
            resetButtonTitle: '清除查询条件',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' },
          },
        },
      },
    },
    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    lastUpdated: { text: '最后更新于' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
    footer: {
      message: 'Powered by VitePress',
      copyright: 'Copyright © 2020-present Jiaxiang',
    },
  },
})

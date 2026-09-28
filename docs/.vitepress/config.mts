import { defineConfig } from 'vitepress'
import { sidebar } from './sidebar'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: 'zh-CN',
  title: 'Jasper的个人笔记',
  description: 'not just the code, but the reasons behind it. code. eat. sleep. loop',
  cleanUrls: true,
  head: [['link', { rel: 'icon', type: 'image/png', href: '/logo.png' }]],

  themeConfig: {
    logo: '/logo.png',
    nav: [
      { text: '前端', link: '/front-end/javascript/' },
      { text: '后端', link: '/back-end/node/' },
      { text: '机器学习', link: '/machine-learning/machine/' },
      { text: '其他', link: '/other/http/' },
      { text: '关于', link: '/about/' },
    ],
    sidebar,
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

//
// 自定义主题入口 —— 继承 VitePress 默认主题，在其上叠加自定义样式。
// 修改样式请编辑 styles/ 下对应文件：
//   vars.css       设计令牌（品牌色、背景、文字、边框、字体，亮/暗两套）
//   base.css       全局基础（正文排版、选中态、滚动条）
//   home.css       首页（hero 渐变标题、光晕、feature 卡片）
//   components.css 组件（导航毛玻璃、代码块、表格、引用、容器块等）
//   question.css   题库（题号徽章、选项条、Case 卡片）
//
// 登录门禁：AccessGate 挂在 Layout 的 layout-top 插槽；
// 防闪现脚本在 config.mts 的 head 里注入（#app 先隐藏，登录后揭示）。
// 凭证与校验逻辑在 gate.ts（只存哈希，明文密码不入仓库）。
//
import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import AccessGate from './AccessGate.vue'
import './styles/vars.css'
import './styles/base.css'
import './styles/home.css'
import './styles/components.css'
import './styles/question.css'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, { 'layout-top': () => h(AccessGate) }),
}

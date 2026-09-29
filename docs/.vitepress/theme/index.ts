//
// 自定义主题入口 —— 继承 VitePress 默认主题，在其上叠加自定义样式。
// 修改样式请编辑 styles/ 下对应文件：
//   vars.css       设计令牌（品牌色、背景、文字、边框、字体，亮/暗两套）
//   base.css       全局基础（正文排版、选中态、滚动条）
//   home.css       首页（hero 渐变标题、光晕、feature 卡片）
//   components.css 组件（导航毛玻璃、代码块、表格、引用、容器块等）
//
import DefaultTheme from 'vitepress/theme'
import './styles/vars.css'
import './styles/base.css'
import './styles/home.css'
import './styles/components.css'
import './styles/question.css'

export default {
  extends: DefaultTheme,
}

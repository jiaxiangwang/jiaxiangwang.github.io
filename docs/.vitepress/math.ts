// MathJax3 markdown-it 插件封装：兼容 CJS default 与 ESM 具名导出两种形态
import mjx from 'markdown-it-mathjax3'

const plugin: any = typeof mjx === 'function' ? mjx : (mjx as any).default

export const mathjax3 = (md: any) => {
  plugin(md)
}

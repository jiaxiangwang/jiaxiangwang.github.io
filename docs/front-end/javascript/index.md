---
title: 这本书的结构
---

# 这本书的结构

本书是Professional Javascript for Web Delopers, 4th Edition的翻译，包括以下章节：

1. **JavaScript 是什么？** -- 解释 JavaScript 的起源: 它从何而来，是如何演变的，如今是什么样的。引入的概念包括JavaScript和ECMAScript之间的关系，文档对象模型（DOM）和浏览器对象模型（BOM）。 还包括对欧洲计算机制造商协会（ECMA）和万维网联盟（W3C）有关标准的讨论。
2. **HTML 中的 Javascript** -- 实验如何将 JavaScript 和 HTML 结合起来创建动态的web页面。介绍了将JavaScript嵌入页面的各种方式，并包括有关JavaScript内容类型及其与`<script>`元素的关系的讨论。
3. **语言基础** -- 介绍基本的语言概念，包括语法和流控制语句。 解释 JavaScript 和其他基于C的语言在语法上的相似之处，并指出它们之前的差异。 引入了强制类型转换，因为它与内置运算符有关。 涵盖所有语言的原始类型，包括Symbol类型。
4. **变量，作用域和内存** -- 由于 JavaScript 变量是弱类型的特点，探讨了如何在 JavaScript 中处理变量。还讨论了原始值和引用值之间的差异，以及与变量相关的执行上下文的信息。另外，关于JavaScript 中的垃圾回收还讨论了当变量超出作用域时如何回收内存。
5. **基本引用类型** -- 涵盖有关 JavaScript 内置引用类型的所有详细信息，例如Date，Regexp，基本类型(primitives)和基本类型包装(primitive wrappers)。 每种参考类型都在理论上以及它们与浏览器实现之间的关系方面进行了讨论。
6. **集合引用类型** -- 使用Object、Array、Map、WeakMap、Set和WeakSet继续本书对内置引用类型的介绍。
7. **迭代器和生成器** -- 在最新版本的 ECMAScript 中引入了两个新的基本概念：迭代器和生成器。 讨论了每种语言的最基本行为以及如何将其与现有语言结构结合使用。
8. **对象，类和面向对象的编程** -- 介绍如何在 JavaScript 中使用类和面向对象的编程。 首先深入讨论 JavaScript 对象类型，然后继续介绍原型继承。 接下来是对ES6类的完整讨论，以及它们如何与原型继承密切相关。
9. **Proxies and Reflect** -- 引入了两个紧密相关的概念：Proxy和Reflect API，它们可用于拦截其他行为并将其填充到语言的基本操作中。
10. **函数(Functions)** -- 探索 JavaScript 最强大的方面之一：函数表达式。主题包括闭包、this对象、模块模式(module pattern)、创建私有对象成员、箭头函数、默认参数和扩展运算符(spread operators)。
11. **Promises 和异步编程** -- 引入了两个紧密相关的新异步编程结构：Promise 类型和async/await。 本章首先讨论异步JavaScript范式，然后继续介绍如何使用promise及其与异步函数的关系。
12. **浏览器对象模型** -- 介绍浏览器对象模型（BOM），它负责与浏览器本身进行交互。 包括每一个BOM对象，如window, document, location, navigator, 和 screen。
13. **客户端检测** -- 介绍检测客户端类型及具备的功能的各种方法。 包括能力检测和‘user-agent’字符串检测的不同的方式。 本章介绍了每种方法的利弊，以及实用性场景。
14. **文档对象模型** -- 介绍 JavaScript 中可用的文档对象模型（DOM）对象，如DOM Level 1中定义的那样。简要介绍XML及其与DOM的关系，有助于深入探讨整个DOM以及它如何允许开发人员操作页面。
15. **DOM扩展** -- 说明其他API以及浏览器本身如何通过更多功能扩展DOM。 主题包括Selectors API，Element Traversal API和HTML5扩展
16. **DOM级别2和3** -- 在前两章的基础上，解释了DOM级别2和3如何通过其他属性，方法和对象来增强DOM。 包括DOM4添加项，例如突变观察器（mutation observers）。
17. **事件** -- 解释 JavaScript 中事件的性质、事件的起源以及DOM如何重新定义事件的工作方式。
18. **Animation and Graphics with Canvas** -- 讨论`<canvas>`标记以及如何使用它创建动态图形。 涵盖了2D上下文和WebGL（3D）上下文，为您提供创建动画和游戏的良好起点。 包括WebGL1和WebGL2的内容。
19. **脚本表单(Scripting Forms)** -- 探索如何使用JavaScript增强表单交互并解决浏览器限制。讨论的重点是单个表单元素，如文本框和选择框，以及数据验证和操作。
20. **JavaScript APIs** -- 涵盖各种JavaScript API, 包括 Atomics, Encoding, File, Blob, Notifications, Streams, Timing, Web Components, 和 Web Cryptography.
21. **错误处理和调试** -- 讨论浏览器如何处理 JavaScript 代码中的错误，并提供几种处理错误的方法。 还针对每种浏览器讨论了调试工具和技术，包括简化调试过程的建议。
22. **JavaScript 中的 XML** -- 介绍用于读取和操作可扩展标记语言（XML）数据的 JavaScript 的功能。 解释了各种 Web 浏览器在支持和对象方面的差异，并提出了一些建议，以简化跨浏览器的编码。 本章还介绍了使用可扩展样式表语言转换（XSLT）来转换客户端上的XML数据。
23. **JSON** -- 介绍JSON数据格式，以替代XML。 讨论使用JSON时浏览器的JSON解析和序列化以及安全性注意事项。
24. **网络请求和远程资源** -- 探索浏览器请求数据和资源的所有最常见方式。包括传统XMLHttpRequest和现代Fetch API的覆盖范围。
25. **客户端存储** -- 讨论如何检测应用程序何时脱机，并提供了各种技术在客户端计算机上存储数据。 首先讨论最受支持的功能cookie，然后讨论诸如Web Storage和IndexedDB的较新功能。
26. **模块(Modules)** -- 讨论模块模式及其对代码库的影响。 在此之后，本章介绍了ES6之前的模块加载程序，例如CommonJS，AMD和UMD。 最后详细介绍了新的ES6模块模式以及如何正确使用它。
27. **Workers** -- 深入涵盖 workers，shared workers和service workers。 包括讨论 worker 在操作系统和浏览器级别上的行为方式，以及如何最佳使用各种类型的 worker 的策略。
28. **最佳实践** -- 探索在企业环境中使用JavaScript的方法。 讨论了具有更好可维护性的技术，包括编码技术，格式设置和常规编程实践。 本章还介绍了执行性能，并介绍了一些用于速度优化的技术。 最后，本章介绍了部署问题，包括如何创建构建过程。

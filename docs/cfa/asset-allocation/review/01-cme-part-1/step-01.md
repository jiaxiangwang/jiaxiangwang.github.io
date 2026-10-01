---
title: "Step 1 — 把经济观点变成可检验的 Capital Market Expectations"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "01 · CME 框架与预测偏差"
study: {"section": "Review Course", "module": "CME Part 1", "moduleLink": "/cfa/asset-allocation/review/01-cme-part-1/", "step": 1, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "Overview", "link": "/cfa/asset-allocation/review/01-cme-part-1/"}, "map": {"label": "Learning Map", "title": "CME Part 1", "link": "/cfa/asset-allocation/review/01-cme-part-1/"}, "next": {"label": "Next Step →", "title": "区分 Trend Growth 与周期增长", "link": "/cfa/asset-allocation/review/01-cme-part-1/step-02"}}
---

# 把经济观点变成可检验的 Capital Market Expectations

::: info 本步目标
能把市场观点放回 CME 工作流程，解释数据与模型为何会产生偏差，并写出可得分的改进建议。
:::

## Why · 为什么“看好股票”还不是可用的配置输入？

投资委员会需要决定股票配置多少，而“看好股票”没有给出预期回报、风险、相关性或投资期限，无法与债券、房地产比较。Capital Market Expectations (CME) 的价值，是把观点变成**服务特定投资决策的一组一致输入**。

先区分用途：Strategic Asset Allocation (SAA) 需要长期预期；Tactical Asset Allocation (TAA) 使用较短期观点。同一个统计模型即使拟合良好，若预测期限与决策期限不符，也可能没有配置价值。

## Core & Intuition · 先建立流程，再检查输入、方法与判断

把 CME 看成一个闭环：**明确需要什么预期 → 检查历史记录 → 选择预测方法 → 取得可靠数据 → 解读当前环境 → 形成一致预期 → 对照实际结果反馈**。最后一步使预测过程能被检验，而不是每次结果偏离后重新编故事。

闭环中有三类失真，必须先判断问题发生在哪里：

| 检查层 | 典型问题 | 为什么影响配置 |
| --- | --- | --- |
| 数据是否代表真实机会集？ | Survivorship bias；appraisal smoothing | 失败基金被漏掉，或价格更新过慢，会使回报/风险看起来更有利 |
| 关系是否有经济机制？ | Data-mining bias；regime change | 反复筛选会找到偶然显著关系；旧制度下有效的参数不一定适用于今天 |
| 判断是否独立于心理起点？ | Availability；anchoring；status quo | 鲜明经历、初始数字或原有配置，可能取代对新证据的判断 |

**Intuition：** 数据多不等于证据强。扩大样本能减少 sampling error，却可能把不同政策制度混在一起；增加解释变量能改善样本内拟合，却可能降低样本外可靠性。

预测工具也各有用途。Econometric / structural models 用方程维持变量间一致性，但有设定误差与 false precision；leading indicators 提供及时的转向线索，却可能出现 false signals；checklist 灵活，但主观性较高、跨时点一致性较弱。组合使用仍需要上述检查。

## Example · Wuyan 的报告缺少什么？

<p class="source-note">Source: Local 原版书 CME / No.2021052701000001 — adapted；答案为推导。</p>

Wuyan 为国内股票建立长期模型，已经研究历史数据、选择模型和数据来源，也解释了当前经济环境。报告却未明确列出投资决策需要的全部预期，也未描述如何形成最终结论和跟踪结果。

正确补充的顺序是：先定义所需 CME 与期限，再把分析汇总为一致的预测，最后比较 realized outcomes 与 forecasts 并反馈。不能只回答“使用更复杂模型”：模型属于流程中间的一环，不能代替目标定义或结果检验。

## CFA Language

遇到 **data-mining bias**，识别“反复搜索，直到显著”的过程；遇到 **availability bias**，识别鲜明经历使某些结果更容易被想起；遇到 **status quo bias**，识别无充分理由仍维持原决定。三者都能产生错误预测，但失真机制不同。

**Misinterpretation of correlation** 要区分同时变动、领先关系与因果关系。Nominal GDP 与 equity returns 同期相关，并不能单独证明 GDP 能预测未来回报。本 Step 的学习要求是 **Understand only**：重建推理流程，不需要额外数学公式。

## Connection

CME 输入会进入 [MVO](/cfa/asset-allocation/review/04-principles/step-01)，小的估计误差可能变成很大的权重变化；[稳健配置方法](/cfa/asset-allocation/review/04-principles/step-02) 处理这种敏感性，却不能让失真的源数据自动变好。[Variance–Covariance Matrix](/cfa/asset-allocation/review/02-cme-part-2/step-05) 则需要同样的数据质量检查。

## Exam Focus

- **Exam Trigger — Explain / Discuss：** 先点名偏差，再说明题干行为如何造成失真，最后说明对 CME 的影响。
- **Common Trap：** 只写“有 bias”或“相关不代表因果”，却不对应题干的反复筛选、鲜明经历或时间关系。
- **Boundary Condition：** 更长的样本只有在结构适用性得到检查后才有帮助；样本内显著也不能替代样本外验证。
- **Constructed Response：** “Repeated searches select chance relationships, so the apparent predictive power may not persist out of sample.” 这一句同时给出机制与后果。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other CME，No.2025060303000001 — adapted；答案为推导。</p>

An analyst finds a significant relation between soccer results and equity returns after extensive data searches, without an economic rationale. Which bias is **most likely**?


<div class="review-options">

A. Anchoring.

B. Status quo.

C. Data mining.



</div>

::: tip Answer & Reasoning
**Answer: C.** 多次搜寻后选中显著关系，而非由经济机制提出并验证假设。

**Exam Takeaway：** 先说明偏差怎样发生，再说明它怎样污染配置输入。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-framework)

</div>

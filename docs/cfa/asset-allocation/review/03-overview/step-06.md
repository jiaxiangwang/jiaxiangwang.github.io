---
title: "Step 6 — 用成本与风险偏离确定 Rebalancing Policy"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "06 · 再平衡的风险与成本取舍"
study: {"section": "Review Course", "module": "Overview of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/03-overview/", "step": 6, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "透过资产标签检查共同 Risk Factors", "link": "/cfa/asset-allocation/review/03-overview/step-05"}, "map": {"label": "Learning Map", "title": "Overview of Asset Allocation", "link": "/cfa/asset-allocation/review/03-overview/"}, "next": {"label": "Next Step →", "title": "Module Review", "link": "/cfa/asset-allocation/review/03-overview/review"}}
---

# 用成本与风险偏离确定 Rebalancing Policy

::: info 本步目标
能区分 calendar 与 corridor rebalancing，用成本和偏离风险解释 corridor 宽度，并保持与 TAA 的目的区分。
:::

## Why · 为什么每次权重漂移都交易，可能反而损害目标？

SAA 定义长期风险结构，价格变化会使实际权重 drift。恢复结构有价值，却要付 transaction costs、taxes 和可能放弃趋势的机会成本。每一点偏离都马上交易，可能使成本超过风险控制收益。

Rebalancing policy 要解决的是这个边际取舍：何时值得交易，交易到哪里，以及怎样处理无法及时卖出的资产。它不是看到上涨就自动卖出的简单口号。

## Core & Intuition · 触发规则与 Corridor Width 分开设计

**Calendar rebalancing** 按固定日期检查或交易，简单但检查间风险可漂移；**percentage-of-portfolio / corridor rebalancing** 在权重越界时触发，控制更直接但需要监控。两者可结合；触发后是否回到精确 target，应遵守具体政策，而不是默认。

设定宽度时区分两项边际代价：更宽减少交易，却允许更多风险偏离；更窄控制风险，却增加交易机会。

| 其他条件相同 | 典型方向 | 经济理由 |
| --- | --- | --- |
| 更高 transaction costs / realized-gains taxes | Wider | 每次纠偏更贵，减少触发次数 |
| 更高 risk aversion | Narrower | 对偏离原风险目标更不容忍 |
| 与组合其余资产更高 correlation | Wider | 一起变化，单类漂移对整体结构影响相对较小 |
| 更强 momentum belief | Wider | 更早逆向交易可能放弃趋势收益 |

**Intuition：** Low correlation 的资产更有分散价值，任其漂移更可能破坏原有风险结构，因此其他条件相同时，更值得较早纠偏。关于 volatility，需要分清 asset / rest-of-portfolio、absolute / proportional bands，以及题目是在最优化总成本与风险，还是仅减少交易次数；不能将不同口径的方向机械拼接。

> **Quick Recall：** 若题目只关注交易频率，且 corridor 按 target weight 比例设定，高波动资产用更宽范围能否减少交易？
>
> **Answer: Yes.** 它更少越界；若改为同时优化风险漂移和成本，需重新判断。[对应 Beade 练习](/cfa/asset-allocation/questions/2025072102000046#q-2025072102000046-2)。

## Example · Law：为什么建议 Global Equities 使用宽范围？

<p class="source-note">Source: Local Other AA / No.2025072102000041-8 — adapted；答案为推导。</p>

Raye 使用 cost–benefit approach，建议 global equities 有更宽范围。选项给出更高 risk aversion、更高 transaction costs 或更低 correlation。

只有更高交易成本直接支持 wider corridor。Risk aversion 更高使风险偏离更不可接受；较低 correlation 提高维持分散结构的价值，方向都更接近 narrower。这样作答是把每项条件放回同一个边际框架，不是背三条互不相连的方向。

## CFA Language

**Policy weight** 是战略目标；**actual weight** 是当前持仓；**rebalancing corridor** 是允许偏离的范围。越界是风险控制触发，**TAA** 则依据短期观点主动偏离；相同交易可以有不同目的。

本步是 **Understand only**。需懂 absolute percentage-point band 与 proportional band 的口径差异，但本地范围没有要求加入复杂的最优宽度推导。Taxable accounts 可因实现利得税而使用更宽范围，或用现金流、其他账户调整；仍需控制整个投资者的经济风险。

## Connection

Rebalancing 落实 [SAA Governance](/cfa/asset-allocation/review/03-overview/step-01)。[Taxes / Asset Location](/cfa/asset-allocation/review/05-constraints/step-04) 改变交易成本，[Liquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02) 决定能否交易，[TAA](/cfa/asset-allocation/review/05-constraints/step-05) 则需要单独的主动观点与授权。

## Exam Focus

- **Exam Trigger — Most / least accurate：** 把每项条件写成“交易成本↑ → 更宽”或“偏离代价↑ → 更窄”。
- **Common Trap：** 用减少交易次数的直觉回答总成本—风险最优问题；把 rebalancing sell-down 自动称作 TAA。
- **Boundary Condition：** Illiquid assets 不能保证越界时及时出售；税务范围更宽也不自动取消 IPS 上限。现金流和 commitments 应提前规划。
- **Constructed Response：** “Higher transaction costs justify a wider corridor because frequent risk corrections become more expensive.” 同时给出方向与机制。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000009 — adapted；答案为推导。</p>

Which condition supports a **narrower** rebalancing range?


<div class="review-options">

A. Higher taxes.

B. Stronger momentum beliefs.

C. Lower correlation with other assets.



</div>

::: tip Answer & Reasoning
**Answer: C.** A/B 支持更宽；C 使保持分散化更有价值。

**Exam Takeaway：** 先辨认目的，再用交易成本与风险偏离的边际取舍解释范围。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-rebalancing)

</div>

---
title: "Step 4 — 区分 PPP 长期锚与 Capital Flows 短期力量"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "04 · PPP、资本流动与汇率方向"
study: {"section": "Review Course", "module": "CME Part 2", "moduleLink": "/cfa/asset-allocation/review/02-cme-part-2/", "step": 4, "total": 5}
studyNav: {"previous": {"label": "← Previous", "title": "把租金、Cap Rate 与估值平滑串起来", "link": "/cfa/asset-allocation/review/02-cme-part-2/step-03"}, "map": {"label": "Learning Map", "title": "CME Part 2", "link": "/cfa/asset-allocation/review/02-cme-part-2/"}, "next": {"label": "Next Step →", "title": "让 Variance–Covariance Matrix 反映真实风险", "link": "/cfa/asset-allocation/review/02-cme-part-2/step-05"}}
---

# 区分 PPP 长期锚与 Capital Flows 短期力量

::: info 本步目标
能先确认报价方向，再区分相对通胀的长期锚、资本流动的短期作用，以及 overshooting 后的调整。
:::

## Why · 为什么高利率国家的货币未必升值？

高利率可能来自货币紧缩，也可能来自高通胀、预期贬值或危机风险补偿。只凭名义利差判断货币，会把投资者要求的补偿误当作无风险收益机会。

Currency CME 要先明确 base currency 与 quotation，再识别所问期限。贸易和价格相对调整较慢，资本可以迅速移动；长期 purchasing-power 判断与短期资金流判断因此可能同时指向不同方向。

## Core & Intuition · 报价 → 长期锚 → 短期力量 → 风险条件

先约定 $S$ 是每 1 单位外币需要多少本币：$S$ 上升表示本币贬值。反向报价的升跌符号相反，所有百分比判断都应从这一步开始。

接着区分两种解释：**trade / PPP approach** 检查相对物价、竞争力与外部余额；**capital-flow approach** 检查资产收益、增长、资本开放与政策可信度。Relative PPP 认为更高通胀最终需要货币贬值来抵消，但短期流入可暂时支持该货币。

**Intuition：** 商品价格调整与资金调仓的速度不同。金融市场开放带来大量即时流入时，货币可以涨过新的长期均衡；此后商品、回报差与资金流逐渐调整，汇率从 overshot level 回落。这不是否认新均衡可以比原来更强。

外部融资也要看组成。Direct investment / private equity 通常比短期可交易债务难以迅速撤出；依赖短期外债、hot money 或期限错配，会增加突然资本外逃的脆弱性。不能用 current-account deficit 的单个数字替代完整判断。

## Example · Fip：报价不变时，相对 PPP 是什么状态？

<p class="source-note">Source: Local 原版书 CME / No.2020012102000009 — adapted；答案为推导。</p>

一个国家的通胀连续三年约比对方高 5 个百分点，但名义汇率保持不变。本国商品相对变贵，所以本币相对 PPP **overvalued**；纠正方向是本币贬值，而不是升值。

用小幅变化近似，累计差约 15%。若简化为每年 price-ratio factor 1.05，$S$ 应上升 $(1.05)^3-1=15.76\%$。但每一单位本币的外币价值是其倒数，下降幅度并不是同一个正负号转换。考试若要求精确值，应使用题干给出的两国实际通胀路径与报价。

## CFA Language & Formula

::: info Formula · Know how to use
Relative PPP 在“本币 / 外币”报价下，把价格比变化接到汇率：

$$\%\Delta S\approx\pi_{domestic}-\pi_{foreign}$$

本国通胀更高 → $S$ 上升 → 本币贬值。对于复利口径，用对应期间价格比：

$$\frac{S_T}{S_0}\approx\prod_{t=1}^{T}\frac{1+\pi_{d,t}}{1+\pi_{f,t}}$$

输入需为同一期间的本国与外国通胀；若 quotation 反向，应先取倒数再解释变化。
:::

**Overvalued** 是相对所用价值锚的水平判断；**appreciation / depreciation** 是变化方向。**Overshooting** 表示先越过长期均衡再调整，不能把任何一次升值都如此命名。

## Connection

[开放经济制度](/cfa/asset-allocation/review/01-cme-part-1/step-06) 限制汇率与利率的独立性。货币预期还会进入本币口径的 [股票](/cfa/asset-allocation/review/02-cme-part-2/step-02) 与 [债券回报](/cfa/asset-allocation/review/02-cme-part-2/step-01)，所以资产预测与 FX 假设要保持一致。

## Exam Focus

- **Exam Trigger — Determine / Discuss：** 每一 observation 单独判断其方向，并说明使用的是贸易还是资本渠道。
- **Common Trap：** 反转报价仍沿用原符号；把高名义利率直接视为升值信号；或把 PPP 当作短期交易保证。
- **Boundary Condition：** PPP 是长期锚，短期资本流动和政策风险能造成偏离；资本外逃判断还取决于持仓与融资期限。
- **Constructed Response：** “Higher relative inflation with an unchanged exchange rate makes the domestic currency overvalued under PPP.” 一句对应条件、机制和结论。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other CME，No.2025060303000028 — adapted；答案为推导。</p>

A currency appreciates sharply after financial-market opening. Under the **overshooting** mechanism, its subsequent long-run movement is **most likely**:


<div class="review-options">

A. Depreciation from the overshot level.

B. Stabilization at that level.

C. Continued appreciation without adjustment.



</div>

::: tip Answer & Reasoning
**Answer: A.** 问的是 overshot 后的回归，不是否认开放带来的均衡变化。

**Exam Takeaway：** 先写 quotation，再说明长期价格锚与短期资本力量各在回答什么问题。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-currency)

</div>

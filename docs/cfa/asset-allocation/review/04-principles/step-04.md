---
title: "Step 4 — 用 MCTR 区分 Capital Weight 与 Risk Weight"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "04 · MCTR、ACTR 与 Risk Parity"
study: {"section": "Review Course", "module": "Principles of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/04-principles/", "step": 4, "total": 7, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "用 Scenario / Monte Carlo 检查路径与目标风险", "link": "/cfa/asset-allocation/review/04-principles/step-03"}, "map": {"label": "Learning Map", "title": "Principles of Asset Allocation", "link": "/cfa/asset-allocation/review/04-principles/"}, "next": {"label": "Next Step →", "title": "按 Funding Situation 选择 Liability-relative 方法", "link": "/cfa/asset-allocation/review/04-principles/step-05"}}
---

# 用 MCTR 区分 Capital Weight 与 Risk Weight

::: info 本步目标
能区分 capital allocation 与 risk allocation，计算边际/绝对/比例风险贡献，并解释最优风险预算的适用条件。
:::

## Why · 为什么 40% 股票可以贡献大部分组合风险？

资产的资本占比不等于风险占比。高波动资产若与组合其他部分强烈共振，即使权重不最大，也可能主导结果。反过来，一项资产的独立波动很高，却可能有分散作用。

Risk budgeting 将 total portfolio risk 拆成 contributions，再判断这部分风险获得多少补偿。它不是只把总波动压到最低，而是有意识地分配风险来源。

## Core & Intuition · 边际影响 × 当前权重 = 绝对贡献

先分三个量：**MCTR** 说明增加少量该项 exposure 对组合 total volatility 的边际影响；**ACTR** 是当前权重对应的 absolute contribution；**PCTR** 是其占总 volatility 的比例。

**Intuition：** 独立 volatility 只说明资产自己多不稳定，MCTR 还看它与当前组合的共同变动。因此用于计算的 beta 是相对**本组合**的 beta，不能随手拿 CAPM market beta 替代。

在无额外 binding constraints 的 interior tangency allocation，若一项资产每单位 marginal risk 提供更高 excess return，还可通过调整配置改善结果。最优时这种比率相等；它不同于“全部风险贡献相等”。

**Risk parity** 则主动设定相等风险贡献预算，不以 expected-return optimization 为中心。低波动、低共变的资产往往需要较多本金才能达到同风险贡献，但具体权重必须依完整 covariance 与 constraints 求解。Low expected return 本身不是提高权重的原因。

## Example · Williams：先计算 MCTR，再计算 ACTR

<p class="source-note">Source: Local Other AA / No.2025072102000044-4/5 — adapted；答案为推导。</p>

某资产的 beta relative to overall portfolio 为 1.091，组合 volatility 为 21.63%，capital weight 为 63.34%。

先算 MCTR：$1.091\times21.63\%=23.60\%$。再算 ACTR：$0.6334\times23.60\%=14.95\%$。其 PCTR 约为 $14.95/21.63=69.1\%$，高于 63.34% 的 capital weight。

这个差别解释了为何资金权重图不能直接当风险预算图。若只乘 beta × weight，会漏掉组合 volatility；若直接将 63.34% 当 risk contribution，又忽略了该资产的共变强度。

## CFA Language & Formula

::: info Formula · Must memorize
从组合 covariance 恢复风险，再分解贡献：

$$\sigma_p=\sqrt{w^\top\Sigma w},\qquad MCTR_i=\frac{(\Sigma w)_i}{\sigma_p}=\beta_{i,p}\sigma_p$$

$$ACTR_i=w_iMCTR_i,\quad\sum_i ACTR_i=\sigma_p,\quad PCTR_i=\frac{ACTR_i}{\sigma_p}$$

$w_i$ 用小数，$\Sigma$ 是同口径的 covariance matrix，$\beta_{i,p}$ 是相对 portfolio 的 beta。ACTR 的单位与 $\sigma_p$ 相同，PCTR 才是比例。
:::

::: info Formula · Know how to use · 最优补偿条件
在 interior、无额外 binding constraints 的 tangency 条件下：

$$\frac{E(R_i)-r_f}{MCTR_i}=\frac{E(R_p)-r_f}{\sigma_p}$$

经济含义是每单位边际风险的 excess-return compensation 相等。若约束绑定或风险贡献为负，需谨慎应用，不能用除法机械判所有现实组合。
:::

**Risk parity** 是 equal contributions，不是 equal capital weights，也不是上式的同义词。

## Connection

[Factor Exposures](/cfa/asset-allocation/review/03-overview/step-05) 与 [VCV](/cfa/asset-allocation/review/02-cme-part-2/step-05) 决定共变结构，[MVO](/cfa/asset-allocation/review/04-principles/step-01) 的最优条件解释风险补偿。若真实目标是负债稳定，预算还需改成对应的 liability-relative risk。

## Exam Focus

- **Exam Trigger — Calculate / Identify：** MCTR、ACTR、PCTR 逐步计算，并把 beta benchmark 写清楚。
- **Common Trap：** “optimal risk budget minimizes total risk”；“25% 每类即等风险”；或把 ACTR 写成 $w\beta$。
- **Boundary Condition：** 单项风险贡献可因对冲关系为负；constraints 与 liabilities 会改变最优预算。缺完整 covariance 时不能可靠推出具体 risk-parity weights。
- **Constructed Response：** “Risk budgeting decomposes total risk; risk parity equalizes risk contributions rather than capital allocations.”

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000028 — adapted；答案为推导。</p>

ACTR equals portfolio weight multiplied by:


<div class="review-options">

A. Asset beta alone.

B. Portfolio volatility alone.

C. Asset MCTR.



</div>

::: tip Answer & Reasoning
**Answer: C.** beta 与 portfolio volatility 的乘积才是 MCTR，少任何一项都不对。

**Exam Takeaway：** 先算边际贡献，再乘本金权重；等资金、等风险与最优补偿是三个不同条件。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-riskbudget)

</div>

---
title: "Step 5 — 透过资产标签检查共同 Risk Factors"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "05 · 共同风险因子与实施工具"
study: {"section": "Review Course", "module": "Overview of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/03-overview/", "step": 5, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "用可实施的 Asset Classes 建立机会集", "link": "/cfa/asset-allocation/review/03-overview/step-04"}, "map": {"label": "Learning Map", "title": "Overview of Asset Allocation", "link": "/cfa/asset-allocation/review/03-overview/"}, "next": {"label": "Next Step →", "title": "用成本与风险偏离确定 Rebalancing Policy", "link": "/cfa/asset-allocation/review/03-overview/step-06"}}
---

# 透过资产标签检查共同 Risk Factors

::: info 本步目标
能透过资产名称识别 systematic exposures，并区分风险模型中的 factor 与实际可投资的 factor portfolio / strategy。
:::

## Why · 为什么四类资产仍可能在同一次冲击中一起下跌？

Equities、high-yield debt、private equity 和 property 可以有不同名称，却共同依赖增长与融资环境。在增长下滑、流动性变差时，它们可能一起亏损。

Factor-based analysis 的用途是看出这些共同驱动，并明确希望承担多少 exposure。它补充资产类分类，而不是通过重新命名自动获得分散化。

## Core & Intuition · 识别驱动 → 衡量暴露 → 选择工具

先用 multifactor risk model 解释现有组合对 growth、inflation、rates、liquidity 等因子的敏感度，再决定期望的 exposures，最后用 assets / strategies 实施。

Macro / structural factors 帮助解释经济冲击；investment factors 如 value、size、momentum 常由观察到的 premiums / anomalies 和特定组合构造。前者是风险描述，后者可由投资组合近似取得；二者不能只因都叫 factor 就视为同一概念。

**Intuition：** 多个类别对同一个 factor 的 exposure 会累加。Capital weight 分散，如果暴露方向和强度相同，仍可能产生集中的 factor risk。相反，改变实施策略可改变暴露，却同时引入成本、tracking 和其他风险。

因子本身不能像一只证券直接买下。Factor portfolio / strategy 是工具，会有交易成本、杠杆或做空要求；模型暴露还会受定义、估计窗口和 regime change 影响。因子低相关也不能视为永久保证。

## Example · Law：解决风险重叠应做什么？

<p class="source-note">Source: Local Other AA / No.2025072102000041-5 — adapted；答案为推导。</p>

Raye 发现原配置的资产类有 overlapping inflation、liquidity 和 volatility exposures，准备确定想承担多少各项风险。

最有用的是 multifactor risk model：它把每项资产对共同因素的敏感度放在同一尺度，显示暴露如何合并。只把 “Derivatives” 改名为 foreign equities，改善了分类表述，却不能量化原有共同风险；仅比较各类波动，也没有回答哪项冲击会使它们一起变化。

## CFA Language & Formula

::: info Formula · Understand only
模型把回报分成共同驱动与残余部分：

$$R_i\approx\alpha_i+\sum_k b_{ik}F_k+\epsilon_i$$

组合对因子 $k$ 的暴露为 $b_{p,k}=\sum_i w_i b_{ik}$。$w_i$ 是 capital weight，$b_{ik}$ 是 exposure，不是风险贡献；残余 $\epsilon_i$ 仍需保留。本步理解加总机制即可，不推导完整 factor covariance model。
:::

**Systematic exposures** 描述共同风险；**risk contributions** 还依赖波动和 covariance。**Directly investable factors** 这种表述通常混淆了因子与 factor-tracking portfolio。

## Connection

[VCV 的 Factor Model](/cfa/asset-allocation/review/02-cme-part-2/step-05) 把共同驱动转换成 covariance；[Risk Budgeting](/cfa/asset-allocation/review/04-principles/step-04) 再把风险分配到贡献。前一步的 [Asset Classes](/cfa/asset-allocation/review/03-overview/step-04) 提供实施分类，三者要相互校验。

## Exam Focus

- **Exam Trigger — Identify / Explain：** 题干说各类别有 overlapping inflation、liquidity 或 volatility risks，想到 multifactor model。
- **Common Trap：** “Risk factors are directly investable”；“factor allocation always improves outcomes”；或以相等 capital weights 证明风险相等。
- **Boundary Condition：** Factor definition、estimation window 和 implementation costs 会改变结果；危机下的关系可能不同于正常样本。
- **Constructed Response：** 写 “The model identifies overlapping systematic exposures across asset classes.”，直接对应目的。

> **Quick Recall：** 两项资产同为 25% capital weight，factor exposure 会相同吗？\
> **Answer: No.** 暴露系数与共同风险结构可能不同。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000005 — adapted；答案为推导。</p>

Which statement is **most accurate**?


<div class="review-options">

A. Risk factors are directly investable.

B. Multifactor models help control systematic exposures.

C. Factor allocation always improves outcomes.



</div>

::: tip Answer & Reasoning
**Answer: B.** A 混淆风险描述与可实施组合，C 把工具能力误当结果保证。

**Exam Takeaway：** 资产类告诉你持有什么，因子模型告诉你共同承受什么冲击。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-factors)

</div>

---
title: "Step 3 — 选择与目标一致的 Risk Definition"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "03 · Asset-only、负债与目标风险"
study: {"section": "Review Course", "module": "Overview of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/03-overview/", "step": 3, "total": 6}
studyNav: {"previous": {"label": "← Previous", "title": "用 Economic Balance Sheet 看完整风险", "link": "/cfa/asset-allocation/review/03-overview/step-02"}, "map": {"label": "Learning Map", "title": "Overview of Asset Allocation", "link": "/cfa/asset-allocation/review/03-overview/"}, "next": {"label": "Next Step →", "title": "用可实施的 Asset Classes 建立机会集", "link": "/cfa/asset-allocation/review/03-overview/step-04"}}
---

# 选择与目标一致的 Risk Definition

::: info 本步目标
能先定义投资者的失败情景，再选择 asset-only、liability-relative 或 goals-based，而不是让现有工具替投资者决定风险。
:::

## Why · 为什么最低资产波动未必是最安全配置？

养老金的成功是按时支付负债，私人客户的成功可能是完成教育与退休目标。一个资产波动很低的组合，如果不能跟随负债价值或目标支出变化，仍会增加真正的失败风险。

优化前必须先问“什么叫失败”。本步把风险定义从资产本身，扩展到资产相对义务和每个具体目标；之后才有理由选择模型。

## Core & Intuition · 同一组 CME，三个不同的评估对象

三个框架都分配投资者资源，但评价结果的标尺不同：

| Approach | 决策中心 | 主要 Risk Definition |
| --- | --- | --- |
| Asset-only | 资产回报与风险的效率 | Portfolio return volatility 等资产风险 |
| Liability-relative | 资产如何支持负债 | Surplus、funding ratio 或 contributions 的不稳定 |
| Goals-based | 每个目标需要哪些资金 | 未达目标的 probability / shortfall |

**Intuition：** 假设利率下降，现金自身价值较稳定，长期负债现值却上升；单看资产波动会认为现金安全，funding ratio 却可能恶化。匹配负债的长债有较高独立价格波动，但能与负债同向变化，反而减小相对风险。

Asset-only 不是“不考虑投资者”：仍需目标和约束，只是没有把负债共变直接放到优化中心。Goals-based 也不专属于个人；按业务线建立不同目标账户的机构可以有类似 segmentation。不要用个人/机构标签取代风险分析。

## Example · VU 的未来现金支出应怎样进入配置？

<p class="source-note">Source: Local Other AA / No.2025072102000039-2 — adapted；答案为推导。</p>

顾问建议强调提供固定收益 cash distributions 的配置，以覆盖大学未来超出 tuition revenue 的支出。它把投资组合与未来支付相联系，最贴近 **liability-relative** 的思路。

如果客户改成分别为教育、退休与捐赠设立 sub-portfolios，并为每个目标规定 horizon 与 success probability，就更接近 goals-based。两者都关注支付，但前者强调资产/负债共同变化与匹配，后者强调目标层级及成功概率。

## CFA Language

**Surplus** 是资产减负债的价值；**funding ratio** 是资产相对负债的比例；**goal shortfall** 是未满足某项目标的程度或概率。考试中它们不是 portfolio volatility 的同义词。

本步是 **Understand only**：记住“目标 → 失败情景 → 风险尺度 → 配置工具”的顺序。具体 surplus formulas、hedging portfolio 和 probability-adjusted funding return 将在 Principles 中应用，这里不需要提前推导全部方法。

## Connection

上一 Step 的 [Economic Balance Sheet](/cfa/asset-allocation/review/03-overview/step-02) 提供义务与既有风险；下一 Module 的 [Liability-relative methods](/cfa/asset-allocation/review/04-principles/step-05) 与 [Goals-based funding](/cfa/asset-allocation/review/04-principles/step-06) 继承本步定义的成功/失败标准。

## Exam Focus

- **Exam Trigger — Most appropriate approach：** 写 “because the objective is … and risk should be measured as …”，把选择直接接到投资者目的。
- **Common Trap：** 给 DB pension 选最高 Sharpe ratio，却忽略贡献额稳定和负债对冲目标。
- **Boundary Condition：** 资产波动小不保证 funding risk 小；目标多且不能相互替代时，也不能只用一个全账户平均回报目标。
- **Constructed Response：** “Use a liability-relative approach because the objective is to stabilize funding, rather than minimize stand-alone asset volatility.”

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000004 — adapted；答案为推导。</p>

Which approach uses portfolio return volatility as its primary risk measure?


<div class="review-options">

A. Asset-only.

B. Goals-based.

C. Liability-relative.



</div>

::: tip Answer & Reasoning
**Answer: A.** B/C 分别把目标 shortfall、资产相对负债的风险放在中心。

**Exam Takeaway：** 先定义失败，再选择风险尺度和配置方法。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-approaches)

</div>

---
title: "Step 2 — 减少 MVO 输入误差造成的极端权重"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "02 · 稳健输入与 Global Market 基准"
study: {"section": "Review Course", "module": "Principles of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/04-principles/", "step": 2, "total": 7, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "从 Investor Utility 选择有效配置", "link": "/cfa/asset-allocation/review/04-principles/step-01"}, "map": {"label": "Learning Map", "title": "Principles of Asset Allocation", "link": "/cfa/asset-allocation/review/04-principles/"}, "next": {"label": "Next Step →", "title": "用 Scenario / Monte Carlo 检查路径与目标风险", "link": "/cfa/asset-allocation/review/04-principles/step-03"}}
---

# 减少 MVO 输入误差造成的极端权重

::: info 本步目标
能解释 MVO 的输入敏感性，区分 reverse optimization、Black–Litterman 与 resampling，并避免宣称这些方法消除错误。
:::

## Why · 为什么精确计算也可能产生极端权重？

优化器把输入当作可信事实。某资产 expected return 被高估一点，优化器可能大幅增加其权重；输出的小数位很多，并不说明预期准确。MVO 尤其容易对 expected-return errors 敏感。

稳健方法的目的，是控制噪声怎样进入配置。先识别起点、处理对象和剩余局限，不能把所有“更分散”结果都称作同一种方法。

## Core & Intuition · 限制、均衡基准、观点与输入采样

方法之间的关系可沿普通 MVO 的方向恢复：returns / covariance → weights。不同改进在链条不同位置工作：

| Method | 从哪里出发？ | 主要处理 | 仍需警惕 |
| --- | --- | --- | --- |
| Constraints / shrinkage | 权重范围或稳定的参数目标 | 限制集中或输入噪声 | 任意约束、错误 target |
| Reverse optimization | Investable global market weights 与风险 | 反推出 implied equilibrium returns | 市场基准不自动适合客户 |
| Black–Litterman | 均衡输入 + investor views + confidence | 将观点按信心融入预期 | 错误观点与不合理信心 |
| Resampled MVO | 对输入不确定性作抽样 | 反复优化、综合 weights，使配置更稳定 | 仍继承基础输入与模型误差 |

**Intuition：** Reverse optimization 先问“什么 returns 能使给定市场权重合理”，提供内部一致的起点。Black–Litterman 才进一步问“有证据的观点应让这个起点移动多少”。高信心会使观点影响更大，所以 confidence 本身也要有依据。

Resampling 不是多次从真实未来观察结果，而是从指定输入分布产生可能的输入，再平均配置。错误的中心假设仍可能产生稳定但错误的平均结果；平均权重也不保证位于原来 estimated frontier 上。

## Example · Patel：Reverse Optimization 改变的是什么？

<p class="source-note">Source: Local 原版书 AA / No.2018031301000004 — adapted；答案为推导。</p>

Patel 的表按给定的五个独立资产类别列出 market caps，总额 107.8 trillion；US equity 为 22.2 trillion、global-market beta 1.4，$r_f=2.0\%$、global premium 5.5%。

US equity 的均衡权重按 market cap 为 $22.2/107.8=20.59\%$，不同于原 MVO 的 35%。其 implied return 为 $2+1.4\times5.5=9.7\%$，不同于原 return input 8.6%。

这显示 reverse optimization 用既定市场权重恢复一致 returns，并不是从给定 returns 反推全部 risk parameters。案例的类别按源表使用，不能自行重定义其 global / US 覆盖而改掉数据。

## CFA Language & Formula

::: info Formula · Know how to use
本地题用 market-cap proportions 作为 equilibrium weights，用 global-market beta 求 implied return：

$$w_i^{market}=\frac{MC_i}{\sum_j MC_j},\qquad E(R_i)=r_f+\beta_{i,G}RP_G$$

$\beta_{i,G}$ 的 benchmark 是 global market，$RP_G$ 是 premium。先统一 market-cap 单位；不要拿旧 MVO weights 代替市场权重。
:::

**Reverse optimization** 只描述反推均衡输入；**Black–Litterman** 还需要 views 和 confidence。**Resampled MVO** 重复处理输入不确定性；它与模拟投资财富路径的 Monte Carlo 使用目的不同。

## Connection

[CME bias checks](/cfa/asset-allocation/review/01-cme-part-1/step-01) 与 [VCV shrinkage](/cfa/asset-allocation/review/02-cme-part-2/step-05) 处理基础输入。稳健 MVO 之后仍需 [Simulation](/cfa/asset-allocation/review/04-principles/step-03) 检查路径，以及 real-world liquidity / implementation constraints。

## Exam Focus

- **Exam Trigger — Contrast：** 分别回答 asset mix 与 expected returns；说明 ordinary MVO 和 reverse optimization 的方向相反。
- **Common Trap：** 声称 reverse optimization eliminates estimation error；看到任何 market tilt 就叫 Black–Litterman；认为 resampling 能修正系统性错误输入。
- **Boundary Condition：** Global market portfolio 是可解释的基准，不是所有投资者的最终 SAA；费用、vehicle 风险与流动性仍须单独纳入。
- **Constructed Response：** “Reverse optimization derives returns consistent with market weights; Black–Litterman combines those returns with views and their confidence.”

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000042-3 — adapted；答案为推导。</p>

An allocation starts from investable global market weights, derives equilibrium inputs and then adjusts for investor views. It is **best** described as:


<div class="review-options">

A. Black–Litterman.

B. Reverse optimization alone.

C. Unadjusted historical MVO.



</div>

::: tip Answer & Reasoning
**Answer: A.** B 提供基准，但没有包含后续 views integration。

**Exam Takeaway：** 看起点、处理对象与剩余误差，才能正确区分稳健配置方法。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-robust)

</div>

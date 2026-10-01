---
title: "Step 7 — 把配置经验法当作基准而非答案"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "07 · 经验法作为基准"
study: {"section": "Review Course", "module": "Principles of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/04-principles/", "step": 7, "total": 7}
studyNav: {"previous": {"label": "← Previous", "title": "把 Probability、Horizon 与 Funding Cost 连起来", "link": "/cfa/asset-allocation/review/04-principles/step-06"}, "map": {"label": "Learning Map", "title": "Principles of Asset Allocation", "link": "/cfa/asset-allocation/review/04-principles/"}, "next": {"label": "Next Step →", "title": "Module Review", "link": "/cfa/asset-allocation/review/04-principles/review"}}
---

# 把配置经验法当作基准而非答案

::: info 本步目标
能说明常见 heuristic 使用什么、忽略什么，并用目标、完整财富和流动性判断 endowment-style allocation 的适用性。
:::

## Why · 为什么输入不确定时，简单规则仍值得比较？

复杂配置的结果可能来自噪声，而非可靠的经济信息。简单规则透明、容易监督、实施成本较低，可以作为检验复杂结果的 benchmark。

但 benchmark 不是现成答案。它的价值取决于哪些重要信息被省略，以及这些省略是否与投资者的目标冲突。本步训练的是 critique，而不是记一个股票比例就结束。

## Core & Intuition · 每种规则省略了哪项决定？

把 heuristic 的做法与缺口并列，才知道它何时可用：

| Heuristic / model | 使用的核心机制 | 没有自动解决的问题 |
| --- | --- | --- |
| 60/40 | 固定 equity / bond capital split | 当前 risk preference、CME、负债与目标 |
| 120 minus age | 股票权重随年龄下降 | Human-capital risk、个人义务和风险容量 |
| 1/N | 每类相等 capital weight，定期再平衡 | Returns、volatility、correlations 与 risk contributions |
| Endowment / Yale model | 较多 alternatives、active management 与 illiquidity premiums | 当前支出、capital calls、capacity 与治理能力 |
| Norway model | 较多可规模化 public-market exposures，并考虑成本、治理与 ESG | 不应直接等同以主动私募为核心的 endowment 配置 |

**Intuition：** 年龄可以近似反映剩余工作期限，却不能告诉你劳动收入是否 equity-like，或明年是否有重大支付。1/N 减少参数估计依赖，却不使用共变信息，所以等本金不等风险。

Endowment-style allocation 能容忍非流动性，依赖稳定资源、可预测支出和管理能力。长期 horizon 提供机会，却不保证每个压力年份都有现金；illiquidity premium 也不是锁定财富就必然拿到的收益。

## Example · 1/N 为什么不能称为风险预算？

<p class="source-note">Source: Local Other AA / No.2025072102000046-8 — adapted；答案为推导。</p>

Müller 说 1/N allocation 依赖各 asset class 的 investment characteristics。实际的 1/N 规则每类投入相等资本，不因 volatility、expected return 或 correlation 而改变比例，因此这项说法不正确。

若两类资产的 MCTR 不同，即使本金相同，ACTR 仍不同。要让 risk contributions 相等，必须使用风险关系求权重，那已经是 risk parity / risk budgeting 的问题，不能再用 1/N 名称跳过计算。

## CFA Language

**Heuristic** 用简化规则作决策；**benchmark** 用于比较与检验；**optimal allocation** 需要说明相对什么目标、机会集与约束最优。三个标签不能互换。

本步为 **Understand only**。120 minus age 是规则识别，不是完整 risk-aversion optimization；60/40 与 1/N 也不需要为了显得数学化而增加公式推导。重点是知道每种方法保留了什么信息，以及省略哪些经济风险。

## Connection

[MVO](/cfa/asset-allocation/review/04-principles/step-01) 可以与简单规则比较，但评价尺度应与目标一致。[Economic Balance Sheet](/cfa/asset-allocation/review/03-overview/step-02) 修复年龄规则遗漏的风险，[Liquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02) 判断能否采用 endowment-style exposures。

## Exam Focus

- **Exam Trigger — Identify / Critique：** 点名规则的主要特征，再说明它没有使用哪项题干信息。
- **Common Trap：** 1/N exploits MCTR differences；age rule is a full risk-tolerance optimization；长期机构都适合 Yale。
- **Boundary Condition：** 简单规则可以有治理和成本优势；复杂模型也需要证明增益。Illiquidity premium 依市场、费用与管理能力，不保证实现。
- **Constructed Response：** “1/N equally allocates capital without considering volatility or correlation, so it does not equalize risk contributions.”

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000029 — adapted；答案为推导。</p>

Which statement is **most accurate**?


<div class="review-options">

A. 1/N exploits differences in MCTR.

B. The endowment model seeks illiquidity premiums.

C. 120 minus age is a full risk-tolerance optimization.



</div>

::: tip Answer & Reasoning
**Answer: B.** A 混淆 equal capital 与 risk budgeting；C 给年龄规则赋予了不存在的完整优化能力。

**Exam Takeaway：** 简单规则用于对照和识别缺口，适配性仍由投资者目标与约束证明。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-heuristics)

</div>

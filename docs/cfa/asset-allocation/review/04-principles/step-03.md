---
title: "Step 3 — 用 Scenario / Monte Carlo 检查路径与目标风险"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "03 · 财富路径、Scenario 与 Monte Carlo"
study: {"section": "Review Course", "module": "Principles of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/04-principles/", "step": 3, "total": 7}
studyNav: {"previous": {"label": "← Previous", "title": "减少 MVO 输入误差造成的极端权重", "link": "/cfa/asset-allocation/review/04-principles/step-02"}, "map": {"label": "Learning Map", "title": "Principles of Asset Allocation", "link": "/cfa/asset-allocation/review/04-principles/"}, "next": {"label": "Next Step →", "title": "用 MCTR 区分 Capital Weight 与 Risk Weight", "link": "/cfa/asset-allocation/review/04-principles/step-04"}}
---

# 用 Scenario / Monte Carlo 检查路径与目标风险

::: info 本步目标
能用提款例子解释 sequence risk，区分特定情景与概率路径，并判断模拟输出究竟依赖哪些假设。
:::

## Why · 为什么相同累计回报仍可能不能完成退休目标？

没有现金流时，回报的乘积决定终值；有提款时，亏损之后必须卖出更多份额，之后上涨作用于更少资本。回报顺序因此会改变剩余财富。

单期 mean / variance 的效率无法完整回答多期支出目标。Scenario analysis 与 Monte Carlo 的用途，是把回报、现金流、规则和目标放入时间路径，检验在哪些条件下会失败。

## Core & Intuition · 特定机制与条件性结果分布

**Scenario analysis** 将一个一致环境传给资产、负债与现金流，例如 recession、inflation shock 或 liquidity freeze。它帮助看清机制，少数情景却不足以自动得出精确成功概率。

**Monte Carlo simulation** 从指定 joint return / factor / cash-flow model 产生多条路径，再观察 terminal wealth、shortfall、funding ratio 或 contributions 的分布。税、非正态回报、动态支出与 rebalancing costs 都可以纳入，但必须显式建模。

**Intuition：** “可以处理”不等于“已经处理”。如果输入假设为独立正态回报、固定正常相关性、没有费用，运行十万次也不会自动出现未建模的 liquidity crisis。更多模拟降低数值抽样误差，不会消除参数或模型错误。

有效的检查应同时改变重要假设：return tails、serial dependence、inflation、withdrawal timing、资产可售性和再平衡规则。得到的是 conditional results，应说明条件，再解释投资含义。

## Example · 同一组回报，提款把顺序变成风险

<p class="source-note">Source: Original teaching example（用于说明本地 sequence-risk 知识点）。</p>

起始财富 100，每年年末提款 10。先 −20%、后 +25%：第一年剩 70，第二年 $70\times1.25-10=77.5$。先 +25%、后 −20%：第一年剩 115，第二年 $115\times0.8-10=82$。

无提款时，两条路径都为 $100\times0.8\times1.25=100$。有提款后，早期亏损留下更小的复利基础，所以终值不同。这就是 sequence risk；“累计回报相同”不能代替目标的现金流检验。

## CFA Language & Formula

::: info Formula · Know how to use
财富递推式的经济含义是“投资增长后扣支出”，或“先支出，再让剩余资金增长”：

$$W_{t+1}=W_t(1+R_{t+1})-C_{t+1}\quad\text{(期末提款)}$$

$$W_{t+1}=(W_t-C_t)(1+R_{t+1})\quad\text{(期初提款)}$$

$W$ 为可参与复利的财富，$C$ 为提款。先确认现金流时点，再套式子；future nominal spending 和 real spending 需以一致 inflation assumptions 转换。
:::

**Sequence risk** 是现金流与回报顺序的共同影响；**model risk** 是使用错误过程或规则的风险。它们不是“样本次数不足”的同义词。

## Connection

[MVO](/cfa/asset-allocation/review/04-principles/step-01) 提供单期候选，[Goals-based allocation](/cfa/asset-allocation/review/04-principles/step-06) 定义成功标准。模拟需要把 [Liquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02) 和 rebalancing 规则嵌入路径，而非只生成资产收益。

## Exam Focus

- **Exam Trigger — Explain why required：** 写 “Cash flows make terminal wealth path dependent”，说明为何需要多期建模。
- **Common Trap：** 将 simulation 当作目标；将很多路径当作假设可靠的证明；把它与 resampled MVO 的输入采样混为一谈。
- **Boundary Condition：** 若不建模 tails、correlation changes 和交易限制，输出不会自动包括这些风险。少数主观 scenarios 也不能直接宣称精确概率。
- **Constructed Response：** 用“early loss + withdrawal → less capital for later recovery”说明 sequence risk，比只写路径依赖更具体。

> **Quick Recall：** 有提款时，相同累计回报能保证相同终值吗？\
> **Answer: No.** 提款改变后续参与复利的本金。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000020 — adapted；答案为推导。</p>

Monte Carlo is **most likely** needed to model future wealth when:


<div class="review-options">

A. There are no cash flows.

B. Cash flows make terminal wealth path dependent.

C. Cash flows exist but terminal wealth is path independent.



</div>

::: tip Answer & Reasoning
**Answer: B.** 核心理由是路径依赖，不是简单“有很多资产”。

**Exam Takeaway：** 先确定现金流时点与规则，再把模拟结果解释为有条件的目标检验。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-simulation)

</div>

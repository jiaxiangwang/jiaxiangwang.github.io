---
title: "Step 3 — 用 Scenario / Monte Carlo 检查路径与目标风险"
---

# Step 3 — 用 Scenario / Monte Carlo 检查路径与目标风险

## 单期效率不保证多期目标成功

没有现金流时，terminal wealth 主要取决于累计回报；有提款时，同样一组年度回报的顺序可以产生不同终值。退休初期亏损后提款，会卖出更多份额，后续上涨作用于更小资本，这就是 sequence risk。

**Know how to use：** 若期末提款，$W_{t+1}=W_t(1+R_{t+1})-C_{t+1}$；若期初提款，$W_{t+1}=(W_t-C_t)(1+R_{t+1})$。先写现金流时点，再决定模型。假设初始 100，每年期末提款 10，回报 -20%、+25% 时终值 77.5；顺序相反时终值 82。无提款两者都是 100。

## Scenario Analysis 与 Monte Carlo 各看什么？

Scenario analysis 把一致的特定环境传给资产、负债与现金流，例如通胀冲击、growth recession、liquidity freeze。它清楚展示机制，但不能仅用几个主观情景声称已估计精确概率。

Monte Carlo simulation 从指定 joint return / factor / cash-flow 模型产生许多路径，记录终值、shortfall、funding ratio、required contributions 等分布。可纳入非正态回报、动态支出、税和 rebalancing cost；它不局限于均值与波动率，但必须显式建模这些特征。

## 模型允许，不代表结果可靠

如果模拟只用正常时期固定相关性、独立正态回报、无成本，运行十万次也不会自动覆盖 liquidity crisis。Simulation 产生的是**给定输入与规则的条件性结果**。参数、tail assumptions、withdrawal timing、inflation 和再平衡机制应作 sensitivity analysis。

VU Case 指出交易成本和非均值—方差分布特征，Monte Carlo 可处理它们；不是“只要用 Monte Carlo 就正确”，而是方法能够承载这些问题。

**Exam Trigger — Explain why required：** 明确“cash flows make terminal wealth path dependent”，而非笼统说长期要模拟。**Boundary Condition：** Monte Carlo 是检验配置的工具，不是独立投资目标；与 resampled MVO 的输入采样用途不同。

> Quick Recall：相同累计回报，有提款时终值一定相同吗？\
> **Answer: No。** 现金流让回报顺序影响可参与后续复利的资本。

## Immediate Practice

Source: Local Other AA，No.2025072102000020 — adapted；答案为推导。

Monte Carlo is **most likely** needed to model future wealth when:

A. There are no cash flows.\
B. Cash flows make terminal wealth path dependent.\
C. Cash flows exist but terminal wealth is path independent.

**Answer: B.** 核心理由是路径依赖，不是简单“有很多资产”。

## Connection

MVO 选单期效率，goals-based 定成功概率，Monte Carlo 检查多期实现；liquidity 与 rebalancing 规则必须在路径里体现。

[从 Investor Utility 选择有效配置](/cfa/asset-allocation/review/04-principles/step-01) · [把 Probability、Horizon 与 Funding Cost 连起来](/cfa/asset-allocation/review/04-principles/step-06) · [用现金流压力检验 Illiquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-simulation)

---

[← Previous](/cfa/asset-allocation/review/04-principles/step-02) · [Learning Map](/cfa/asset-allocation/review/04-principles/) · [Next Step →](/cfa/asset-allocation/review/04-principles/step-04)

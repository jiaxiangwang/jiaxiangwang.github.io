---
title: "Step 6 — 用成本与风险偏离确定 Rebalancing Policy"
---

# Step 6 — 用成本与风险偏离确定 Rebalancing Policy

## 为什么不能只说“涨了就卖”？

SAA 规定长期风险目标。市场价格变化会让实际权重 drift，rebalancing 主要恢复风险结构。它有交易成本、税和机会成本；每一点偏离都立刻交易可能让成本超过风险控制收益。

**Calendar rebalancing** 在固定日期检查/交易，简单但两次检查之间风险可能漂移。**Percentage-of-portfolio / corridor rebalancing** 在权重超限时触发，更直接控制偏离但需要持续监控。可组合使用；触发后不一定必须交易到精确 target，按政策与成本可先回到 corridor 内。

## Corridor Width 是边际取舍

| 其他条件相同的变化 | 典型 optimal corridor | 原因 |
| --- | --- | --- |
| Higher transaction costs / taxes | Wider | 少触发昂贵交易 |
| Higher risk aversion | Narrower | 对风险偏离更不容忍 |
| Higher volatility of the asset or rest of portfolio | Narrower（风险控制权衡下） | 权重/风险偏离的代价提高 |
| Higher correlation with rest of portfolio | Wider | 一起涨跌，偏离造成的结构变化较小 |
| Stronger momentum belief | Wider | 过早逆向交易可能放弃趋势 |

宽度结论须明确比较口径：asset / rest-of-portfolio volatility、absolute / proportional bands 和目标是**总体成本—风险最优**还是仅减少频繁交易。不能把不同问题里的方向机械拼起来。

## 税务账户为什么通常范围更宽？

Realized gains tax 增加卖出成本。Taxable account 可给更宽 corridor、用新增资金/现金流调权或在 tax-deferred account 实施部分调整，同时检查全账户经济风险。减少交易并不等于放弃 IPS 上限。

Law Case 问 wider range 的理由，给出的 higher transaction costs 合适；low correlation 则通常加强分散价值，偏离更值得控制，方向相反。

**Exam Trigger — Most / least accurate：** 逐条写“成本↑→更宽”或“偏离风险代价↑→更窄”。**Boundary Condition：** Illiquid assets 不能保证在越界时及时交易；private commitments、提款与现金缓冲必须前置规划。

## Immediate Practice

Source: Local Other AA，No.2025072102000009 — adapted；答案为推导。

Which condition supports a **narrower** rebalancing range?

A. Higher taxes.\
B. Stronger momentum beliefs.\
C. Lower correlation with other assets.

**Answer: C.** A/B 支持更宽；C 使保持分散化更有价值。

## Connection

Rebalancing 把 SAA 风险目标变成操作政策，taxes 与 liquidity 改变其成本；它与基于短期观点的 TAA 有不同目的。

[用 After-tax Exposure 进行配置与 Asset Location](/cfa/asset-allocation/review/05-constraints/step-04) · [将 Tactical Views 放在 SAA 与 IPS 边界内](/cfa/asset-allocation/review/05-constraints/step-05) · [用现金流压力检验 Illiquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-rebalancing)

---

[← Previous](/cfa/asset-allocation/review/03-overview/step-05) · [Learning Map](/cfa/asset-allocation/review/03-overview/) · [Next Step →](/cfa/asset-allocation/review/03-overview/review)

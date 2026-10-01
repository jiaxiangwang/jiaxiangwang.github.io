---
title: "Step 3 — 选择与目标一致的 Risk Definition"
---

# Step 3 — 选择与目标一致的 Risk Definition

## 三种配置框架解决同一个目标错配问题

优化之前先问“什么叫失败”。如果目标是稳定支出或负债支付，仅降低资产 return volatility 未必能降低真正的失败风险。

| Approach | 优化/选择对象 | Risk 的含义 | 适用问题 |
| --- | --- | --- | --- |
| Asset-only | 资产回报与风险效率 | Portfolio return volatility 等资产风险 | 负债/目标可另行处理，重视资产效率 |
| Liability-relative | 资产相对负债 | Surplus、funding ratio、贡献额不稳定 | DB pension 等明确支付义务 |
| Goals-based | 每个目标的 sub-portfolio | 未达目标的 probability / shortfall | 多期限、多优先级目标 |

Asset-only 不等于不知道投资者约束；它是没有把 liabilities 的共同变动直接放进目标函数。Goals-based 也不必仅限 individuals：保险机构按业务线划分目标/账户可以有相似 segmentation。不要用个人/机构标签代替目标分析。

## 为什么 Asset volatility 低仍可能不适合养老金？

持有现金可降低资产波动，但利率下降时负债现值可能上升，funding ratio 恶化。持有与负债匹配的长债可能有更高独立价格波动，却降低资产相对负债的波动。

VU 建议固定收益现金分配覆盖大学未来支出，思路是 **liability-relative**；私人客户按教育、退休与捐赠建立 sub-portfolios，思路是 **goals-based**。两者都关注支付，但前者强调共同风险与匹配，后者强调每个目标成功概率和资金分配。

## 先判断目标，再选择模型

本 Module 只建立框架；下一 Module 再在 liability-relative 中区分 surplus optimization、hedging/return-seeking 和 integrated ALM，在 goals-based 中用 horizon/probability-adjusted return 计算 funding cost。

**Exam Trigger — Most appropriate approach：** 写“because the objective is … and risk should be measured as …”。**Common Trap：** 看到 Sharpe ratio 高就选养老金方案，忽略贡献额稳定或负债对冲目标。**Boundary Condition：** 既有财富与目标越复杂，简单 asset-only 结果越需要额外经济资产负债表与路径检验。

## Immediate Practice

Source: Local Other AA，No.2025072102000004 — adapted；答案为推导。

Which approach uses portfolio return volatility as its primary risk measure?

A. Asset-only.\
B. Goals-based.\
C. Liability-relative.

**Answer: A.** B/C 分别把目标 shortfall、资产相对负债的风险放在中心。

## Connection

同一组 CME 可进入不同配置目标函数；Principles 中的方法选择必须继承这里的风险定义，而不能倒过来让工具决定目标。

[用 Economic Balance Sheet 看完整风险](/cfa/asset-allocation/review/03-overview/step-02) · [按 Funding Situation 选择 Liability-relative 方法](/cfa/asset-allocation/review/04-principles/step-05) · [把 Probability、Horizon 与 Funding Cost 连起来](/cfa/asset-allocation/review/04-principles/step-06)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-approaches)

---

[← Previous](/cfa/asset-allocation/review/03-overview/step-02) · [Learning Map](/cfa/asset-allocation/review/03-overview/) · [Next Step →](/cfa/asset-allocation/review/03-overview/step-04)

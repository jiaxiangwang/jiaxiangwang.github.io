---
title: "Step 5 — 按 Funding Situation 选择 Liability-relative 方法"
---

# Step 5 — 按 Funding Situation 选择 Liability-relative 方法

## 目标是支付负债，而非让资产 Sharpe 最高

先恢复三项：负债现金流/估值风险、assets 对负债的共变、sponsor 的出资能力。Funded status 和 volatility of contributions 比资产自身波动更贴近很多 DB pension 的真实风险。

**Must memorize：**

$$Surplus=A-L,\qquad Funding\ Ratio=\frac{A}{L}$$

资产 205、负债 241 时 ratio 85.06%；两者都减少 25 后，surplus 仍为 -36，但 ratio $180/216=83.33\%$。美元 surplus 不变不代表 ratio 不变；欠资状态下同额下降会恶化 ratio。

## 三种方法按问题选

| Method | 思路 | 典型适配与边界 |
| --- | --- | --- |
| Surplus optimization | 在单期目标中平衡 expected surplus return 与 surplus variance | 能把 liabilities 当相对风险基准；不自动处理多期 contributions |
| Hedging / return-seeking portfolios | 先用资产覆盖 liability-hedging portfolio，再将剩余投向回报组合 | 资金充足、负债可较可靠对冲时清楚；欠资无法足额建 hedge |
| Integrated asset–liability management (ALM) | 多期同时模拟资产、负债、出资与动态决策 | 目标为未来 funded status 与贡献稳定时更合适，但模型复杂 |

Surplus return 的归一化必须依题干。例如用期初 assets 归一，$R_S\approx R_A-(L_0/A_0)R_L$，因此 funding ratio 影响 liability risk 在目标函数中的权重。不同资料可能用不同 surplus return 定义，不能只背同名符号。

## Hedge 比例为什么来自经济负债？

本地 Johansson Case，assets 10 billion、liabilities 8.5 billion，liabilities 由 index-linked government bonds 驱动。若能以这些债券充分匹配，85% assets 用于 hedge，15% 用于 return-seeking；不选最高预期回报组合。这仍要满足现金流、duration、inflation 与信用匹配条件。

**Exam Trigger — Most appropriate：** 单期欠资/保守→考虑 surplus optimization；明确多期贡献额与 funding goal→integrated ALM；有足额资金和可对冲义务→two-portfolio。**Boundary Condition：** 冻结计划与固定负债易建 hedge；closed to new employees 仍可能继续 accrue benefits，不等于 frozen fixed liabilities。

## Immediate Practice

Source: Local Other AA，No.2025072102000046-3 — adapted；答案为推导。

Assets are $205m and liabilities $241m. Both fall $25m. Funding ratio will:

A. Decrease.\
B. Stay unchanged.\
C. Increase.

**Answer: A.** 85.06% → 83.33%，尽管 surplus 不变。

## Connection

经济资产负债表同时识别 sponsor 经营风险；CME 的 rates/inflation 进入负债价值，governance 决定目标优先级和贡献政策。

[用 Economic Balance Sheet 看完整风险](/cfa/asset-allocation/review/03-overview/step-02) · [将 Yield、Risk Premium 与实现回报分开](/cfa/asset-allocation/review/02-cme-part-2/step-01) · [选择与目标一致的 Risk Definition](/cfa/asset-allocation/review/03-overview/step-03)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-liability)

---

[← Previous](/cfa/asset-allocation/review/04-principles/step-04) · [Learning Map](/cfa/asset-allocation/review/04-principles/) · [Next Step →](/cfa/asset-allocation/review/04-principles/step-06)

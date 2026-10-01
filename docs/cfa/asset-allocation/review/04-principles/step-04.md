---
title: "Step 4 — 用 MCTR 区分 Capital Weight 与 Risk Weight"
---

# Step 4 — 用 MCTR 区分 Capital Weight 与 Risk Weight

## 资金分配和风险分配不是同一件事

Equities 波动较高、且与其他资产共振，可能以 40% 的 capital weight 贡献大部分 risk。Risk budgeting 先把 total risk 拆成 contributions，再判断承担这些风险获得的补偿是否合理；不等于只把总风险降到最低。

**Must memorize：**

$$\sigma_p=\sqrt{w^\top\Sigma w},\qquad MCTR_i=\frac{(\Sigma w)_i}{\sigma_p}=\beta_{i,p}\sigma_p$$

$$ACTR_i=w_iMCTR_i,\quad\sum_i ACTR_i=\sigma_p,\quad PCTR_i=\frac{ACTR_i}{\sigma_p}$$

MCTR 是资产权重小幅增加对 total volatility 的边际影响；ACTR 是当前权重下的 absolute contribution；PCTR 是比例。$\beta_{i,p}$ 是相对**本组合**的 beta，不是随手用市场 beta。

**Know how to use：** 某类 beta 1.091、$\sigma_p=21.63\%$，MCTR $=23.60\%$；若 weight 63.34%，ACTR $=14.95\%$。先乘 beta，再乘 weight，不能把 ACTR 或 capital weight 误当 MCTR。

## 什么时候 Excess Return / MCTR 应相等？

在无额外 binding constraints、各风险资产为 interior positions 的 tangency / 最优风险预算条件下：

$$\frac{E(R_i)-r_f}{MCTR_i}=\frac{E(R_p)-r_f}{\sigma_p}$$

直觉：若某资产每增加一单位 marginal risk 能换更多 excess return，就仍有重新分配的收益。约束绑定、负权重或负风险贡献会使这个简洁条件需要调整，不能用它机械判所有现实 portfolio。

## Risk Parity 是特定预算，不是万能优化

Risk parity 通常使各资产的风险贡献相等，而非资金权重相等，也不以 expected returns 为核心输入。低波动、低共变资产往往需要更大 capital weight 才达到同 risk contribution；实际权重仍需完整 covariance 与 constraints。Low expected return 本身不是提高权重的理由。

**Exam Trigger — Calculate / Identify：** MCTR、ACTR、PCTR 分开；把 beta 的 benchmark 写清。**Common Trap：** “optimal risk budget minimizes total risk”或“每类投入 25% 即等风险”。

## Immediate Practice

Source: Local Other AA，No.2025072102000028 — adapted；答案为推导。

ACTR equals portfolio weight multiplied by:

A. Asset beta alone.\
B. Portfolio volatility alone.\
C. Asset MCTR.

**Answer: C.** beta 与 portfolio volatility 的乘积才是 MCTR，少任何一项都不对。

## Connection

Factor/VCV 决定 MCTR；MVO 的最优条件解释为何 marginal risk 的回报应一致，但现实约束与 liabilities 会改变预算。

[透过资产标签检查共同 Risk Factors](/cfa/asset-allocation/review/03-overview/step-05) · [让 Variance–Covariance Matrix 反映真实风险](/cfa/asset-allocation/review/02-cme-part-2/step-05) · [从 Investor Utility 选择有效配置](/cfa/asset-allocation/review/04-principles/step-01)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-risk budget)

---

[← Previous](/cfa/asset-allocation/review/04-principles/step-03) · [Learning Map](/cfa/asset-allocation/review/04-principles/) · [Next Step →](/cfa/asset-allocation/review/04-principles/step-05)

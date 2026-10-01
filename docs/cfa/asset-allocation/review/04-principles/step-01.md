---
title: "Step 1 — 从 Investor Utility 选择有效配置"
---

# Step 1 — 从 Investor Utility 选择有效配置

## MVO 先解决效率，再解决适合谁

Mean–Variance Optimization (MVO) 在给定 expected returns、variances、covariances 和 constraints 下，找出同风险回报更高、或同回报风险更低的 portfolios。Efficient frontier 是效率集合，投资者 risk aversion 再决定其中哪个最合适。

**Must memorize（decimal inputs）：**

$$U=E(R_p)-\frac12\lambda\sigma_p^2$$

$\lambda$ 越大，对 variance 的惩罚越大。若回报与 volatility 用百分数数值输入，等价地写 $U_{\%}=E(R)_{\%}-0.005\lambda\sigma_{\%}^2$。不能把 0.5 与 0.005 混用，也不能把 standard deviation 直接替代 variance。

例如 $\lambda=8$，A 的 $\mu=10\%,\sigma=12\%$；B 为 8%/8%；C 为 6%/2%。效用为 4.24%、5.44%、5.84%，所以 C 合适。最高 expected return 与最高 utility 是两个问题。

## 有 Risk-free asset 后，先比较 Sharpe Ratio

若可以按同一 risk-free rate 借贷且无额外约束，tangency portfolio 为最高 Sharpe ratio 的风险组合。目标回报在它与 $r_f$ 之间时，持有部分风险组合、部分现金：

**Know how to use：**

$$w_T=\frac{R_{target}-r_f}{E(R_T)-r_f},\quad\sigma_{mix}=|w_T|\sigma_T$$

$r_f=3\%,E(R_T)=8\%,R_{target}=7\%$，$w_T=80\%$，风险组合波动 11% 时混合波动为 8.8%。同 target return 下，要比较**混合后的**风险，而非原组合风险或原回报最高者。

## 风险资产有效边界的形状

只含 risky assets 且 long-only 时，边界 slope 表示多承担一单位风险能换多少预期回报。Global minimum variance 附近不是最平；constraints 开始/退出 binding 会形成 kinks，不能把每个 kink 都归因于 leverage。

**Exam Trigger — Calculate / Determine：** 先写输入口径，再算效用或混合风险。**Boundary Condition：** 借贷利率不同、负债目标、非正态回报和 liquidity constraints 会使经典单周期 MVO 结论需要修正；MVO 不自动覆盖所有 factor risks。

## Immediate Practice

Source: Local Other AA，No.2025072102000017 — adapted；答案为推导。

Risk-free return is 3%; a tangency portfolio has expected return 8% and volatility 11%. A foundation targets 7%. The tangency weight is **closest to**:

A. 20%.\
B. 50%.\
C. 80%.

**Answer: C.** $(7-3)/(8-3)=80\%$；20% 是 cash weight。

## Connection

输入来自 CME，但 expected return 的小误差会被权重优化放大；下一步的 robust methods 与 simulation 分别处理输入和路径问题。

[减少 MVO 输入误差造成的极端权重](/cfa/asset-allocation/review/04-principles/step-02) · [用 Scenario / Monte Carlo 检查路径与目标风险](/cfa/asset-allocation/review/04-principles/step-03) · [用 MCTR 区分 Capital Weight 与 Risk Weight](/cfa/asset-allocation/review/04-principles/step-04)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-mvo)

---

[← Previous](/cfa/asset-allocation/review/04-principles/) · [Learning Map](/cfa/asset-allocation/review/04-principles/) · [Next Step →](/cfa/asset-allocation/review/04-principles/step-02)

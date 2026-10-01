---
title: "Step 4 — 用 After-tax Exposure 进行配置与 Asset Location"
---

# Step 4 — 用 After-tax Exposure 进行配置与 Asset Location

## Tax 改的是实际可消费财富

税前相同的资产，在不同账户和收益来源下提供的净现金流不同。**Asset allocation** 决定整体 economic exposures，**asset location** 决定哪些 exposures 放在哪些 taxable / tax-advantaged accounts。先定整体风险，再安排账户位置。

在题设明确 interest tax 较高、dividends / long-term gains 税较低的情况下，tax-inefficient high-turnover / income-heavy assets 优先考虑 tax-advantaged accounts；较低周转、capital-gains-oriented exposures 更适合 taxable accounts。不要不看税制就断言所有国家股票/债券的税务排序。

## 线性 Tax Scaling 的最小模型

**Know how to use（constant effective tax + symmetric treatment 的简化）：**

$$R_{AT}=(1-t)R_{PT},\quad\sigma_{AT}=(1-t)\sigma_{PT}$$

分布均值更低、dispersion 更小。若各资产正的线性缩放系数固定，correlation 不变；covariance 按 $(1-t_i)(1-t_j)$ 缩放。现实 progressive rates、deferred gains、不同损失抵扣与现金流时点会破坏简单线性关系。

不同税种和账户不能只套一个 $t$。Deferred capital gains 先享受未缴税资本的复利；实际卖出时才实现税负。Tax-deferred account 的余额也可能含未来税务负债，合并账户时要按净可消费 exposures 考虑。

## Rebalancing 与税的权衡

Taxable account 实现 gains 会支付税，所以相同经济风险下可设更宽 bands、用现金流/其他账户协同调权。题干提供 80%±8% 和 75%±10.7% 两种近似同 risk-profile 方案时，taxable 选较宽的后者、tax-deferred 选前者；不能只比较税前 target weights。

本地 Young Case 的 municipal-bond 题按其常见教学语境推导时，municipal income 的 tax-exempt 处理是一项**明确的解题假设**，不是仓库提供的现实税法。题库会将这一假设显示在分析中，避免把税制推断冒充来源事实。

**Exam Trigger — Calculate / Determine：** 先读收益来源、税率、账户类型和 loss treatment，再算净收益和风险。**Common Trap：** 把最受税务优待的资产反而放进 tax-deferred account；或税后只改 mean 不改 volatility。

## Immediate Practice

Source: Local Other AA，No.2025072102000051-6 — adapted；答案为推导。

Under fixed positive linear tax scaling, which MVO input can remain unchanged?

A. Expected returns.\
B. Correlations.\
C. Standard deviations.

**Answer: B.** Mean 与 volatility 被缩放，correlation 在这个简化假设下不变。

## Connection

Tax 改变 MVO 输入、goal funding 和 rebalancing cost；整体经济风险要跨账户合并，而不能按税前名义余额直接加权。

[从 Investor Utility 选择有效配置](/cfa/asset-allocation/review/04-principles/step-01) · [把 Probability、Horizon 与 Funding Cost 连起来](/cfa/asset-allocation/review/04-principles/step-06) · [用成本与风险偏离确定 Rebalancing Policy](/cfa/asset-allocation/review/03-overview/step-06)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-taxes)

---

[← Previous](/cfa/asset-allocation/review/05-constraints/step-03) · [Learning Map](/cfa/asset-allocation/review/05-constraints/) · [Next Step →](/cfa/asset-allocation/review/05-constraints/step-05)

---
title: "Step 1 — 将 Yield、Risk Premium 与实现回报分开"
---

# Step 1 — 将 Yield、Risk Premium 与实现回报分开

## 债券预期先拆风险，再拆回报

Building block approach 解释投资者为何要求某个收益率：真实无风险利率 + 预期通胀 + term premium + credit premium + liquidity premium。长债相对短债的差额主要包含 term premium；公司债相对同期限国债还包含 credit 与 liquidity 补偿。应比较同币种、同期限，避免把所有 spread 都叫信用风险。

**Know how to use：**

$$E(R)\approx r_{real}+\pi_e+TP+CP+LP$$

这是风险溢价框架中的要求/预期回报分解。若题给 1-year nominal government rate 1%，已经含通胀，不能再加一次 0.6%。Term 1%、credit 0.75%、liquidity 0.55%，10-year corporate 的 building-block return 为 3.30%。

## 为什么 Yield to Maturity 不是任何期限的实现收益？

YTM 使用特定持有与再投资假设。利率变动既影响卖出价格，也影响 coupon reinvestment；两者方向相反。**Macaulay Duration** 是现金流加权平均回收时间，在简化的单次平行利率变化下，提供 price risk 与 reinvestment risk 的平衡期限。

| Horizon $H$ 与 Macaulay Duration $D_M$ | 主导风险 | 利率上升的典型总影响 |
| --- | --- | --- |
| $H<D_M$ | Price risk | 价格损失较占主导，回报下降 |
| $H\approx D_M$ | 两者近似相抵 | 实现回报接近起始收益率 |
| $H>D_M$ | Reinvestment risk | 更高再投资收入较占主导 |

**Know how to use：** 价格的一阶敏感度用 **Modified Duration**：$\Delta P/P\approx-D_{mod}\Delta y$；与 horizon 比较则用 Macaulay Duration。不能把两个 duration 的作用互换。

## Emerging market debt 不只是更高 Yield

关注 ability to pay 与 willingness to pay：财政/外部债务、税基和产业集中、外汇储备相对短期外债、资本外逃、法治和政治意愿。外币债尤其受本币贬值与外汇不足影响。本地资料中的风险指标是筛查线索，不是适用于所有国家的硬性违约阈值。

**Exam Trigger — Calculate / Determine：** 先拆名义无风险与额外 premium，再按题干投资规则判断是否买入。**Common Trap：** 把更高 required return 自动视为更有吸引力；风险变差也会使所需收益上升。

## Immediate Practice

Source: Local Other CME，No.2025060303000022 — adapted；答案为推导。

A fixed-rate bond has Macaulay duration 5 years; the investor's horizon is 3 years. Realized return is **most likely**:

A. More sensitive to price changes than reinvestment income.\
B. Unchanged because the two effects exactly offset.\
C. More sensitive to reinvestment income than price changes.

**Answer: A.** 3 年内收入再投资不足以抵消较远现金流的价格敏感度。

## Connection

利率预测来自 Part 1，进入债券回报后还要看期限与信用；liability-relative allocation 则要比较资产与负债的利率暴露。

[把 Monetary / Fiscal Policy 转成利率判断](/cfa/asset-allocation/review/01-cme-part-1/step-05) · [按 Funding Situation 选择 Liability-relative 方法](/cfa/asset-allocation/review/04-principles/step-05)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-bonds)

---

[← Previous](/cfa/asset-allocation/review/02-cme-part-2/) · [Learning Map](/cfa/asset-allocation/review/02-cme-part-2/) · [Next Step →](/cfa/asset-allocation/review/02-cme-part-2/step-02)

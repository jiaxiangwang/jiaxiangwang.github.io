---
title: "Step 3 — 把租金、Cap Rate 与估值平滑串起来"
---

# Step 3 — 把租金、Cap Rate 与估值平滑串起来

## Property 同时包含债券与股权特征

租约像信用现金流，租户可能违约；租约和资产期限使价值受长期利率影响；租金成长、lease rollover、vacancy 与最终出售价值的不确定性又像 equity risk。房地产回报补偿可以包含 **term、credit、equity premiums**，不能只把 property 当“固定租金债券”。

**Know how to use：**

$$V\approx\frac{NOI}{c},\qquad c\approx r-g$$

$NOI$ 是 net operating income，$c$ 是 capitalization rate。租金未来增长更高会提高价值、降低给定 required return 下的 cap rate；折现率更高则通常提高 cap rate、降低价格。

## 一年回报来自收入加价格变化

**Know how to use（近似）：**

$$E(R_{RE})\approx c_0+g_{NOI}-\%\Delta c$$

收入收益近似为当前 cap rate；NOI 增长包括 real growth 与 inflation；cap rate 下降使估值上升，因此减号很关键。较精确的价格比为 $V_1/V_0=(1+g_{NOI})c_0/c_1$，需区分题干要求的近似与现金流时点。

例如 $c_0=5.7\%,c_1=5.5\%,g_{real}=1\%,\pi=1.5\%$：$\%\Delta c=5.5/5.7-1=-3.51\%$，近似回报为 $5.7+2.5+3.51=11.71\%$。**Cap rate 下跌 20 bp** 不等于估值贡献只有 0.20%。

## 为什么历史波动看起来很低？

Private real estate 常依赖 appraisal 而非连续交易，估值滞后把本期真实冲击分散到多期，造成 serial correlation 和较低 observed variance。与每日交易资产的同期 correlation 也可能失真。数据频率、估值方法、物业异质性与 leverage 都必须比较一致。

Listed REIT 短期受 equity-market sentiment 影响，多年期才可能更接近 underlying property 的经济特征。不要用短期 REIT 数据直接承诺与 equities 的强分散化。

**Exam Trigger — Calculate / Explain：** 区分 cap-rate level、bp change 和 relative change；解释 smoothing 为什么同时扭曲 risk 与 correlation。**Boundary Condition：** 长期稳定 cap rate 时不应永久计入 cap-rate compression；用 GDP 估 NOI growth 需要题目或模型假设支持。

> Quick Recall：appraisal smoothing 后 observed variance 通常高还是低？\
> **Answer: Lower。** 风险被延迟记录，不是经济风险消失。

## Immediate Practice

Source: Local Other CME，No.2025060303000027 — adapted；答案为推导。

Real estate's equity risk premium **most likely** compensates for:

A. Long-term rate changes only.\
B. Tenant default only.\
C. Property value, rent growth, lease rollover and vacancy uncertainty.

**Answer: C.** A/B 分别更多对应 term/credit risk，C 才是 residual property risk。

## Connection

房地产预期不能脱离 inflation 与 rates；进入 MVO 和 liquidity 规划时必须修正估值平滑与实际 vehicle 风险。

[区分预期通胀、意外通胀与 Deflation](/cfa/asset-allocation/review/01-cme-part-1/step-04) · [让 Variance–Covariance Matrix 反映真实风险](/cfa/asset-allocation/review/02-cme-part-2/step-05) · [用现金流压力检验 Illiquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-realestate)

---

[← Previous](/cfa/asset-allocation/review/02-cme-part-2/step-02) · [Learning Map](/cfa/asset-allocation/review/02-cme-part-2/) · [Next Step →](/cfa/asset-allocation/review/02-cme-part-2/step-04)

---
title: "Step 2 — 减少 MVO 输入误差造成的极端权重"
---

# Step 2 — 减少 MVO 输入误差造成的极端权重

## Optimizer 会把输入中的“便宜机会”放大

MVO 对 expected returns 尤其敏感，少量高估就可能使某类资产占据大量权重。历史平均不是免估计误差的事实，相关性和风险也可能因 regime change 变化。改进方法的共同问题是：**如何约束噪声，而不是追求更精细的单点答案？**

| 方法 | 起点与处理 | 解决什么 | 仍有什么局限 |
| --- | --- | --- | --- |
| Weight constraints / shrinkage | 限制集中，向稳定目标收缩 | 减少极端权重或参数噪声 | 约束可能任意，目标可能错误 |
| Reverse optimization | 从 market weights 与风险推 implied returns | 给内部一致的均衡基准 | 市场组合未必适合投资者 |
| Black–Litterman | 均衡基准 + views + confidence | 将观点温和融入 expected returns | 观点和信心仍可出错 |
| Resampled MVO | 对输入采样，逐次优化后组合结果 | 让权重更分散且较稳定 | 仍继承原始输入误差，未必位于原 frontier |

## Reverse Optimization 是反过来问

普通 MVO 是 returns/covariances → weights；reverse optimization 是市场权重与风险关系 → equilibrium returns。不是从 expected returns 反推全部 risk parameters。

**Know how to use：** 题给 asset beta relative to global market，可用 $E(R_i)=r_f+\beta_i RP_G$。$r_f=2\%,RP_G=5.5\%,\beta_{US}=1.4$ 时 implied return 9.7%；global bonds beta 0.6 时为 5.3%。均衡权重由 market capitalization proportions 得到，不照搬此前 MVO 权重。

## Black–Litterman 为什么不等于 Reverse Optimization？

Reverse optimization 只提供起点。加入投资者对某市场的 relative/absolute views，并按 confidence 权衡基准与观点，才构成 Black–Litterman 的关键用途。不把“在市场组合上有任何 tilt”都当成相同方法；识别题要有均衡推导、观点调整的线索。

Resampling 对输入不确定性作模拟，不能证明真实未来会符合输入。真实非流动投资的 vehicle、费用、leverage 与指数统计差异，也不是靠 resampling 自动解决。

**Exam Trigger — Contrast：** 分别对 weights 和 expected returns 作答。**Common Trap：** “reverse optimization eliminates estimation error”与“resampling fixes wrong inputs”都过度承诺。

## Immediate Practice

Source: Local Other AA，No.2025072102000042-3 — adapted；答案为推导。

An allocation starts from investable global market weights, derives equilibrium inputs and then adjusts for investor views. It is **best** described as:

A. Black–Litterman.\
B. Reverse optimization alone.\
C. Unadjusted historical MVO.

**Answer: A.** B 提供基准，但没有包含后续 views integration。

## Connection

对数据偏差与 VCV 噪声的理解决定如何选稳健方法；实际配置还要交给 liquidity 与 Monte Carlo 做可实施/路径检查。

[把经济观点变成可检验的 Capital Market Expectations](/cfa/asset-allocation/review/01-cme-part-1/step-01) · [让 Variance–Covariance Matrix 反映真实风险](/cfa/asset-allocation/review/02-cme-part-2/step-05) · [从 Investor Utility 选择有效配置](/cfa/asset-allocation/review/04-principles/step-01)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-robust)

---

[← Previous](/cfa/asset-allocation/review/04-principles/step-01) · [Learning Map](/cfa/asset-allocation/review/04-principles/) · [Next Step →](/cfa/asset-allocation/review/04-principles/step-03)

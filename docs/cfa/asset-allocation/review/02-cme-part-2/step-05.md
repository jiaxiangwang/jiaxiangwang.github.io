---
title: "Step 5 — 让 Variance–Covariance Matrix 反映真实风险"
---

# Step 5 — 让 Variance–Covariance Matrix 反映真实风险

## 配置风险来自共变，不能只看各资产波动

Variance–covariance matrix (VCV) 包含资产自身 variance 与两两 covariance。它必须与预期回报使用一致的频率、币种和样本口径；只把波动率填入对角线会漏掉组合的共同风险。

**Know how to use：** $n$ 个资产需要 $n$ 个 variance 和 $n(n-1)/2$ 个不同 covariance。200 个资产的 covariance 数为 $200\times199/2=19,900$；若题问全部独立 VCV 元素，再加 200 得 20,100。矩阵有 40,000 个格子，但对称元素不是独立参数。

## Sample statistics 与 Factor model 的取舍

Sample VCV 直接使用历史收益，共变关系较自由，但资产数相对样本数很大时估计噪声严重。Factor model 用少数共同因子解释协方差，减少参数并提供结构；风险是遗漏暴露、因子冗余或错误忽略 idiosyncratic residual variance。

**Understand only：**

$$\Sigma\approx B\Omega B^\top+\Psi$$

$B$ 是资产 factor exposures；$\Omega$ 是 factor covariance；$\Psi$ 是 residual covariance（常简化为对角矩阵）。删掉残差后，某些组合可能被错误认为 riskless。不要把因子模型的简化当成真实风险消失。

## Shrinkage 为什么可能更有效？

**Know how to use：**

$$\widehat\Sigma_{shrunk}=a\Sigma_{target}+(1-a)\widehat\Sigma_{sample},\quad 0\le a\le1$$

用较稳定的 target 约束噪声大的 sample estimate，可能以少量 bias 换更低 estimation variance 和均方误差。不能说 sample VCV “必然 biased and inconsistent”；样本性质取决于统计条件。也不能保证任意 target 或任意权重都改善结果。

## 数据频率也是风险假设

Real estate appraisal smoothing 会压低观测 variance，并扭曲同期 correlation。Stress 时相关性和流动性可能同时恶化，正常时期的 VCV 不是尾部场景的完整描述。MVO 前先检查风险数据，再用 scenario / Monte Carlo 看组合能否承受不利路径。

**Exam Trigger — Calculate / Identify：** 分清 covariance-only、全部独立元素和矩阵格数。**Common Trap：** 题干提到“4 factors”，但问 sample statistic covariance 数时仍用 200 个资产，不能改算 800 个 exposure。

## Immediate Practice

Source: Local Other CME，No.2025060303000029 — adapted；答案为推导。

For 200 assets, how many distinct covariances does a **sample-statistics** VCV require?

A. 800.\
B. 19,900.\
C. 40,000.

**Answer: B.** $n(n-1)/2$；800 是另一种 exposure 计数，40,000 是重复计算对称格子。

## Connection

风险估计接到 MVO、MCTR 和 simulation；appraisal smoothing 在输入端就会把非流动资产看起来过度有吸引力。

[把租金、Cap Rate 与估值平滑串起来](/cfa/asset-allocation/review/02-cme-part-2/step-03) · [减少 MVO 输入误差造成的极端权重](/cfa/asset-allocation/review/04-principles/step-02) · [用 MCTR 区分 Capital Weight 与 Risk Weight](/cfa/asset-allocation/review/04-principles/step-04)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-volatility)

---

[← Previous](/cfa/asset-allocation/review/02-cme-part-2/step-04) · [Learning Map](/cfa/asset-allocation/review/02-cme-part-2/) · [Next Step →](/cfa/asset-allocation/review/02-cme-part-2/review)

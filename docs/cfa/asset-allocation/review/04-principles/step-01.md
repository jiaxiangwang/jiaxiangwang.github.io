---
title: "Step 1 — 从 Investor Utility 选择有效配置"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "01 · MVO、Utility 与现金混合"
study: {"section": "Review Course", "module": "Principles of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/04-principles/", "step": 1, "total": 7}
studyNav: {"previous": {"label": "← Previous", "title": "Overview", "link": "/cfa/asset-allocation/review/04-principles/"}, "map": {"label": "Learning Map", "title": "Principles of Asset Allocation", "link": "/cfa/asset-allocation/review/04-principles/"}, "next": {"label": "Next Step →", "title": "减少 MVO 输入误差造成的极端权重", "link": "/cfa/asset-allocation/review/04-principles/step-02"}}
---

# 从 Investor Utility 选择有效配置

::: info 本步目标
能先辨认有效配置，再用 investor utility 或 risk-free mixing 选择适合目标的组合，并核对输入单位和模型边界。
:::

## Why · 为什么最高回报组合不一定最适合投资者？

Mean–Variance Optimization (MVO) 能比较资产风险与回报的效率，但“效率高”还没有回答投资者愿意承担多少风险。高 risk aversion 的投资者，可以合理选择预期回报较低却效用更高的组合。

本步按“效率 → 适合性 → 目标下的实施”复习。先理解 efficient frontier，再用 utility 选点；允许 risk-free asset 时，还需比较组合与现金混合后的风险。

## Core & Intuition · 有效边界提供选择集合，风险偏好决定取点

给定 CME 和 constraints，MVO 找出同风险下预期回报更高、或同预期回报下风险更低的 portfolios。**Efficient frontier** 是这些有效选择的集合，**global minimum variance portfolio** 是最小风险起点；投资者的 risk aversion 再决定偏好的位置。

**Intuition：** Utility 从预期回报中减去风险惩罚。Risk aversion 越高，同样 variance 越昂贵，因此“最高均值”与“最高效用”会分离。风险惩罚使用 variance，不是直接减 volatility。

若可按相同 $r_f$ 借贷、没有额外限制，风险组合的 tangency portfolio 提供最高 Sharpe ratio；投资者用它与 risk-free asset 的比例调整总风险。目标低于 tangency return 时，不能直接比较未混合风险组合的波动，应先把每个候选方案混到同一目标回报。

只有 risky assets 且 long-only 的边界，slope 表示增加一单位风险换取多少 expected return；GMV 附近上支不是最平。Constraints 开始或退出 binding 可产生 kinks，不能把所有 kink 都解释为 leverage。

## Example · Perkins：低回报组合也能有最高效用

<p class="source-note">Source: Local Other AA / No.2025072102000047-1 — adapted；答案为推导。</p>

Perkins 的 $\lambda=8$。候选 A 的 mean / volatility 为 10% / 12%，B 为 8% / 8%，C 为 6% / 2%。

用小数输入，A 的 $U=0.10-0.5\times8\times0.12^2=4.24\%$；B 为 5.44%，C 为 5.84%，因此选择 C。C 的 mean 最低，但其 variance 的惩罚少得更多。

如果只看 Sharpe 或 expected return，就没有使用题干给定的 risk aversion；如果直接减 $0.5\lambda\sigma$，则改变了目标函数。

## CFA Language & Formula

::: info Formula · Must memorize · Investor Utility
经济含义是 expected reward 减 investor-specific risk penalty：

$$U=E(R_p)-\frac12\lambda\sigma_p^2$$

$E(R)$ 与 $\sigma$ 使用小数。若输入百分数数值，等价写法是 $U_{\%}=E(R)_{\%}-0.005\lambda\sigma_{\%}^2$。不要混用 0.5 与 0.005，也不要把 utility 当作承诺实现的 return。
:::

::: info Formula · Know how to use · Risk-free Mixing
给定 target return，用线性回报关系求风险组合权重：

$$w_T=\frac{R_{target}-r_f}{E(R_T)-r_f},\qquad\sigma_{mix}=|w_T|\sigma_T$$

$r_f=3\%,E(R_T)=8\%,R_{target}=7\%$ 时 $w_T=80\%$；若 $\sigma_T=11\%$，混合波动为 8.8%。剩余 20% 是 risk-free weight。$w_T>1$ 需要杠杆，是否允许必须看题干。
:::

**Efficient** 与 **appropriate** 不是同义词：前者相对机会集，后者还取决于投资者和约束。

## Connection

MVO 输入来自 [CME 与 VCV](/cfa/asset-allocation/review/02-cme-part-2/step-05)。[Robust Methods](/cfa/asset-allocation/review/04-principles/step-02) 改善对输入噪声的敏感性；[Simulation](/cfa/asset-allocation/review/04-principles/step-03) 检查单期效率无法回答的路径与目标问题。

## Exam Focus

- **Exam Trigger — Calculate / Determine：** 先确认 decimal / percentage units，再算 utility；同 target 的方案需比较混合后的 volatility。
- **Common Trap：** 直接选择最高 mean；把 variance 换成 standard deviation；把 cash weight 当 tangency weight。
- **Boundary Condition：** 不同借贷利率、杠杆限制、liquidity constraints、负债目标或非正态回报会改变经典结果。MVO 也不自动保证各 factor 风险均衡。
- **Constructed Response：** 写“C has the highest utility after applying the given risk-aversion penalty”，不要只写它风险最低。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000017 — adapted；答案为推导。</p>

Risk-free return is 3%; a tangency portfolio has expected return 8% and volatility 11%. A foundation targets 7%. The tangency weight is **closest to**:


<div class="review-options">

A. 20%.

B. 50%.

C. 80%.



</div>

::: tip Answer & Reasoning
**Answer: C.** $(7-3)/(8-3)=80\%$；20% 是 cash weight。

**Exam Takeaway：** 先看效率，再用投资者目标比较效用或同目标下的混合风险。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-mvo)

</div>

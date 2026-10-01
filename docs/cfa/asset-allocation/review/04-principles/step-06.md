---
title: "Step 6 — 把 Probability、Horizon 与 Funding Cost 连起来"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "06 · 成功概率、期限与目标资金成本"
study: {"section": "Review Course", "module": "Principles of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/04-principles/", "step": 6, "total": 7, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "按 Funding Situation 选择 Liability-relative 方法", "link": "/cfa/asset-allocation/review/04-principles/step-05"}, "map": {"label": "Learning Map", "title": "Principles of Asset Allocation", "link": "/cfa/asset-allocation/review/04-principles/"}, "next": {"label": "Next Step →", "title": "把配置经验法当作基准而非答案", "link": "/cfa/asset-allocation/review/04-principles/step-07"}}
---

# 把 Probability、Horizon 与 Funding Cost 连起来

::: info 本步目标
能用目标的 horizon / success probability 选择 minimum expectation return，再按现金流时点计算 funding cost；能区分单期 safety-first 与多期目标。
:::

## Why · 为什么最高 Mean Return 不一定让目标最便宜？

客户要的可能是“99% 确定能支付基本生活”，而不是平均财富最高。高均值、高波动的组合，在严格成功概率下，lower-tail outcome 反而可能更差，需要更多初始资本。

Goals-based allocation 先为每个目标定义金额、horizon、priority 和 required success probability，再选 sub-portfolio。Funding cost 应使用对应期限和概率的 minimum expectation return，而不是无条件 mean。

## Core & Intuition · 先选正确的概率行，再算现值

完整链条是：**目标现金流 → horizon / required success → 合格的 minimum return → funding cost → 与总资本比较 → 形成 sub-portfolio weights**。

相同目标下，能达到要求概率的 minimum return 越高，所需初始资本越少。更严格 success probability 通常让 lower-tail return 下降，funding cost 上升；更长期限可能降低年化噪声，但不会消除 sequence risk 或保证成功。

**Intuition：** Mean 是分布的中心，客户需要的 success probability 却限制分布的下尾。不能先选高均值组合，再把均值当作“高概率保证的收益”。题干给 probability / horizon table 时，先使用表格，不能用自己的简化模型覆盖它。

若只问下一年能否超过一个 return threshold，可以用 Roy Safety-First Ratio 比较 standardized buffer；多期目标则还需现金流与终值分布。每个目标单独成功 90%，也不自动意味着所有目标一起成功 90%。

## Example · Armstrong：同一组组合，三个目标选择不同

<p class="source-note">Source: Local Other AA / No.2025072102000048 — adapted；答案为推导。</p>

Armstrongs 有 8 million，要求五年后 5 million 的房屋目标有 85% 成功率，十年生活支出有 99% 成功率，二十五年后 10 million nominal donation 有 75% 成功率。

| 先定位 Goal 的条件 | 最高 minimum return | 对应 Module |
| --- | --- | --- |
| 5 years / 85% | 4.4% | C |
| 10 years / 99% | 2.2% | B |
| 25 years / 75% | 7.5% | D |

先在正确行选组合，再用该 rate 计算目标现值并相加，剩余资本按指令投 A。生活支出的首笔时点在本地 source 未明示，相关 [完整练习](/cfa/asset-allocation/questions/2025072102000048) 保留期初与期末两种结果；这里不强定一个总 funding amount。

## CFA Language & Formula

::: info Formula · Must memorize · 单一未来目标
金额已为 future nominal amount 时，用匹配的 probability / horizon return 折现：

$$PV_{goal}=\frac{FV_{goal}}{(1+r_{min})^T}$$

$T$ 是目标期限，$r_{min}$ 来自对应成功概率和期限。不要再为已给 nominal FV 重复增加 inflation，也不要用 mean 替代 $r_{min}$。
:::

::: info Formula · Know how to use · 连续支出
若未来 $N$ 年每年**期初**支出，第一笔 $C_0$、增长率 $g$、折现率 $r$：

$$PV=C_0\sum_{t=0}^{N-1}\left(\frac{1+g}{1+r}\right)^t$$

即时支出是 $t=0$，不能再折现一年；若第一笔在年末，则需按其时点调整。$g$ 与 $r$ 使用一致 nominal / real 口径。
:::

::: info Formula · Know how to use · Roy Safety-First
单期、可按相同正态模型比较的分布下，标准化目标缓冲越高，shortfall probability 越低：

$$SFR=\frac{E(R_p)-R_L}{\sigma_p}$$

$R_L$ 是最低可接受 return，不是默认 $r_f$。例如本金 900,000、一年后提款 54,000 且不损本金，$R_L=6\%$。Mean / volatility 为 10.5% / 20%、9% / 13%、7.75% / 10% 的 SFR 分别为 0.225、0.2308、0.175，第二个最优（Local Other AA / Shipman / No.2025072102000042-1 — adapted；答案为推导）。
:::

**Minimum expectation return** 是相应成功概率下的门槛，不是均值，也不是 guaranteed return。非正态分布不能仅凭 SFR 精确比较 shortfall probability。

## Connection

[Risk Definition](/cfa/asset-allocation/review/03-overview/step-03) 定义成功，[Simulation](/cfa/asset-allocation/review/04-principles/step-03) 检验多期及联合 shortfall。[Taxes](/cfa/asset-allocation/review/05-constraints/step-04) 与 inflation 则要求净回报和目标支出使用一致口径。

## Exam Focus

- **Exam Trigger — Select / Justify / Construct：** 正确 horizon/probability row → 最大合格 $r_{min}$ → PV → 总资金与权重。
- **Common Trap：** 85% success 目标直接用 mean 9% 折现；期初提款再折现；将 goal threshold 换为 risk-free rate。
- **Boundary Condition：** 预算不足时要调整目标、期限、成功率或增加资金；不能仅升风险就宣称目标已获保障。缺现金流时点时保留条件答案。
- **Constructed Response：** 选择理由应写“highest minimum return for the specified horizon and probability”，不是 highest expected return。

> **Quick Recall：** Required success probability 更高，通常需要更多还是更少初始资本？\
> **Answer: More.** 更保守的 lower-tail discount rate 提高 funding cost。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000011 — adapted；答案为推导。</p>

A portfolio has mean return 9% and volatility 15%. The client wants an 85% probability of reaching a five-year goal. The discount rate is **most likely**:


<div class="review-options">

A. Below 9%.

B. Equal to 9%.

C. Above 9%.



</div>

::: tip Answer & Reasoning
**Answer: A.** 高于 50% 的成功概率需要用更保守的 lower-tail return，而不是均值。

**Exam Takeaway：** 概率与期限决定可用的折现率，现金流时点决定怎样计算现值。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-goals)

</div>

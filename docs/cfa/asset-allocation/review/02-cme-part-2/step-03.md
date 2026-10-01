---
title: "Step 3 — 把租金、Cap Rate 与估值平滑串起来"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "03 · 房地产现金流、Cap Rate 与平滑"
study: {"section": "Review Course", "module": "CME Part 2", "moduleLink": "/cfa/asset-allocation/review/02-cme-part-2/", "step": 3, "total": 5, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "从盈利、分红与估值拆解 Equity Return", "link": "/cfa/asset-allocation/review/02-cme-part-2/step-02"}, "map": {"label": "Learning Map", "title": "CME Part 2", "link": "/cfa/asset-allocation/review/02-cme-part-2/"}, "next": {"label": "Next Step →", "title": "区分 PPP 长期锚与 Capital Flows 短期力量", "link": "/cfa/asset-allocation/review/02-cme-part-2/step-04"}}
---

# 把租金、Cap Rate 与估值平滑串起来

::: info 本步目标
能解释房地产的多种风险补偿，正确区分 cap-rate 水平与变化率，并判断估值平滑怎样污染配置输入。
:::

## Why · 为什么稳定租金不代表稳定经济价值？

租金合同看起来像债券，但租户可能违约、空置率会变，未来重订租约和出售价格也不确定。与此同时，appraisal-based returns 可能更新很慢，令报表上的波动低于经济风险。

本步把估值与风险输入连起来：先看 NOI 和 cap rate 如何决定价值，再看数据是否忠实记录这种价值变化。

## Core & Intuition · 现金流、资本化与数据测量分三层

第一层是现金流：**net operating income (NOI)** 受租金增长、租户、空置和费用影响。第二层是资本化：同样 NOI，在更高 required return 下通常值更少；更高可持续增长则支持更高价值。第三层是测量：private property 的 appraisal 未必即时反映市场冲击。

| 风险来源 | 为什么需要 premium？ | CFA 对应辨认 |
| --- | --- | --- |
| 租约与资产的长期性 | 价值暴露于长期利率和折现率变化 | Term premium |
| 租户不能支付 | 租约现金流存在违约风险 | Credit premium |
| 物业价值、租金增长、续租与空置 | 残余经营/资产价值不确定 | Equity risk premium |

**Intuition：** Cap rate 可以理解为当前 NOI 相对价格的收益率。未来增长更有价值时，投资者愿意为同样当前 NOI 支付更高价格，cap rate 就更低；required return 上升时，价格需要下降，cap rate 通常更高。

Appraisal smoothing 把本期冲击延迟到以后记录，形成 serial correlation、压低 observed variance，也可能扭曲与日交易资产的同期 correlation。经济风险没有消失，只是统计记录不同步。Listed REIT 短期还受 equity-market sentiment 影响，多年期才可能更接近底层 property。

## Example · Cap rate 下调 20 bp，价格贡献不止 0.20%

<p class="source-note">Source: Local Other CME / No.2025060303000026 — adapted；答案为推导。</p>

当前 cap rate 5.7%，预计变为 5.5%，real growth 1%、inflation 1.5%。在本题的简化 NOI growth 假设下，增长约 2.5%。

Cap rate 的水平变化为 −20 bp，但相对变化是 $5.5/5.7-1=-3.51\%$。近似总回报为当前收入 5.7% + NOI growth 2.5% − cap-rate relative change (−3.51%)，即约 **11.71%**。

结果中的额外收益来自 cap-rate compression。若题目改成长期稳定 cap rate，就应去掉这项持续重估，不能把短期高回报永久外推。

## CFA Language & Formula

::: info Formula · Know how to use
稳定增长的估值直觉是“现金流除以资本化率”：

$$V\approx\frac{NOI}{c},\qquad c\approx r-g$$

$c$ 是 cap rate，$r$ 是 required return，$g$ 是可持续 NOI growth；$c\approx r-g$ 依赖稳定增长及一致现金流口径。

本地题的一年回报近似为：

$$E(R_{RE})\approx c_0+g_{NOI}-\%\Delta c$$

$\%\Delta c=c_1/c_0-1$，不是 basis-point change。价格关系 $V_1/V_0=(1+g_{NOI})c_0/c_1$ 可用于理解方向；需要精确 total return 时，还应按照题干处理收到 NOI 的时点。
:::

**Appraisal-based** 与 **transaction-based** 区分的是测量方法；**direct real estate** 与 **listed REITs** 区分的是持有形式。不能把两组词当作完全相同的分类。

## Connection

[Inflation](/cfa/asset-allocation/review/01-cme-part-1/step-04) 同时影响租金和折现率；[VCV estimation](/cfa/asset-allocation/review/02-cme-part-2/step-05) 需要识别 smoothing，避免优化器把低观测风险当作真正安全。[Illiquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02) 则检查这种配置能否满足现金需要。

## Exam Focus

- **Exam Trigger — Calculate / Explain：** 分清 cap-rate level、bp change 与 relative change；说明 smoothing 怎样影响 risk 和 covariance。
- **Common Trap：** 将 −20 bp 直接作为 +0.20% 估值贡献；或用短期 REIT 表现证明 direct property 与 equities 高度分散。
- **Boundary Condition：** GDP growth 代替 NOI growth 需要题目或模型支持；稳定 cap rate 的长期预测不含永久 compression。
- **Constructed Response：** 写 “Appraisals delay market shocks, understating observed volatility and distorting contemporaneous correlations.”

> **Quick Recall：** Appraisal smoothing 后波动变低，经济风险是否真的减少？\
> **Answer: No.** 是风险被延迟记录，不能由较平滑的历史数据直接提高配置。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other CME，No.2025060303000027 — adapted；答案为推导。</p>

Real estate's equity risk premium **most likely** compensates for:


<div class="review-options">

A. Long-term rate changes only.

B. Tenant default only.

C. Property value, rent growth, lease rollover and vacancy uncertainty.



</div>

::: tip Answer & Reasoning
**Answer: C.** A/B 分别更多对应 term/credit risk，C 才是 residual property risk。

**Exam Takeaway：** 先算 NOI 与 cap-rate 的相对变化，再检查观测风险和实际流动性。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-realestate)

</div>

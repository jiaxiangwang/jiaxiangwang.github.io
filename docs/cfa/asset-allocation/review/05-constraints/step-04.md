---
title: "Step 4 — 用 After-tax Exposure 进行配置与 Asset Location"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "04 · 税后配置与 Asset Location"
study: {"section": "Review Course", "module": "Real-World Constraints", "moduleLink": "/cfa/asset-allocation/review/05-constraints/", "step": 4, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "识别 Goals、Constraints 与 Beliefs 的变化", "link": "/cfa/asset-allocation/review/05-constraints/step-03"}, "map": {"label": "Learning Map", "title": "Real-World Constraints", "link": "/cfa/asset-allocation/review/05-constraints/"}, "next": {"label": "Next Step →", "title": "将 Tactical Views 放在 SAA 与 IPS 边界内", "link": "/cfa/asset-allocation/review/05-constraints/step-05"}}
---

# 用 After-tax Exposure 进行配置与 Asset Location

::: info 本步目标
能区分整体资产暴露与账户位置，在题干税制下计算税后输入，并解释税对 correlation 与再平衡的条件性影响。
:::

## Why · 为什么税前余额相同，不代表可消费财富相同？

Taxable account 的收益可能当期缴税，tax-deferred account 的余额也可能包含未来税务负债。同样的税前配置，在不同收益来源和账户中，能够支持的净支出不同。

先决定整体 **asset allocation**，再安排 **asset location**：前者决定承担什么经济风险，后者决定这些暴露放在哪类账户。不能只为减税，将投资者整体风险变成另一个组合。

## Core & Intuition · 净回报、净风险、账户位置与交易成本

税务分析从题干给定的制度开始：interest、dividends、capital gains 的税率与实现时点，losses 如何抵扣，以及账户是否递延。不同国家或产品不能无条件套同一个排序。

若题干明确 interest tax 较高、dividends / long-term gains 较低，可优先把 income-heavy / high-turnover exposures 放在 tax-advantaged accounts，把相对 tax-efficient exposures 留在 taxable accounts；仍需检查总资金与风险。

**Intuition：** 在固定、对称的线性税收模型中，正负回报都按同一比例缩小，所以 mean 和 volatility 一起缩放，correlation 可以不变。现实的 deferral、progressive rates、loss restrictions 或税务择时打破了这个简化。

税还提高 taxable rebalancing 的成本。可以用更宽 bands、新资金或其他账户协同调权，但必须合并检查整个投资者的 exposures；减少实现税并不取消 IPS limits。

## Example · Martin：为什么较税务友好的股票不优先占用递延账户？

<p class="source-note">Source: Local Other AA / No.2025072102000050-3 — adapted；答案为推导。</p>

Martin 的 interest income 税率为 35%，dividends 与 capital gains 为 20%。Neal 认为获得更有利税务待遇的资产应放入 tax-deferred accounts。

在题设环境下，递延空间更适合相对 tax-inefficient 的利息类 exposure。把已经较 tax-efficient 的资产放进去，会占用本可保护高税率收入的空间。结论是账户位置要按净税务作用比较，不能仅凭“有利税务待遇”四个字反转逻辑。

若题干没有说明 municipal bonds 是否免税，应先确认适用税制。若完全免税，taxable account 保留免税优势；若仍有税负，就按净收益比较，不能仅凭债券名称决定位置。

## CFA Language & Formula

::: info Formula · Know how to use · 简化线性 Tax Scaling
若税率 $t$ 固定、正负回报对称处理，净回报是原回报的正比例缩放：

$$R_{AT}=(1-t)R_{PT},\qquad\sigma_{AT}=(1-t)\sigma_{PT}$$

例如 mean 8%、volatility 10%、$t=25\%$，净 mean 为 6%，净 volatility 为 7.5%。对两个资产：

$$Cov_{AT}(i,j)=(1-t_i)(1-t_j)Cov_{PT}(i,j)$$

Covariance 与各 standard deviations 同比例变化，所以 correlation 不变。输入是 constant effective tax rates；不能把 progressive marginal tax 或 deferred gains 随意代入这个模型。
:::

**Asset location** 改变税务位置；**after-tax economic exposure** 才说明支持消费的净风险。Capital-gains deferral 让未缴税资本继续复利，但最终实现税负仍需处理。

## Connection

[MVO](/cfa/asset-allocation/review/04-principles/step-01) 应使用与决策一致的净输入，[Goals Funding](/cfa/asset-allocation/review/04-principles/step-06) 要对应净可消费回报。[Rebalancing](/cfa/asset-allocation/review/03-overview/step-06) 则把 realized-gains taxes 当作纠偏成本。

## Exam Focus

- **Exam Trigger — Calculate / Determine：** 收益类型 → 税率与时点 → loss treatment → account type → 净输入或 location。
- **Common Trap：** 税后只改 mean 不改 volatility；把较 tax-efficient assets 反而优先放递延账户；用税前名义余额直接合并净财富。
- **Boundary Condition：** Correlation 不变依赖固定正线性 scaling；实际税制、递延和不同亏损抵扣可改变关系。具体税率以题干为准。
- **Constructed Response：** 写“higher-tax income is relatively more tax-inefficient, so sheltering it uses the tax-deferred space more effectively”。

> **Quick Recall：** 固定线性 scaling 下，covariance 与 correlation 都不变吗？\
> **Answer: No.** Covariance 缩放，correlation 可保持不变。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000051-6 — adapted；答案为推导。</p>

Under fixed positive linear tax scaling, which MVO input can remain unchanged?


<div class="review-options">

A. Expected returns.

B. Correlations.

C. Standard deviations.



</div>

::: tip Answer & Reasoning
**Answer: B.** Mean 与 volatility 被缩放，correlation 在这个简化假设下不变。

**Exam Takeaway：** 税前风险、税后风险与账户位置分开分析，再合并检查可消费财富。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-taxes)

</div>

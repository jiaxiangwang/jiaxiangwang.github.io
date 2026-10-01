---
title: "Step 5 — 将 Tactical Views 放在 SAA 与 IPS 边界内"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "05 · TAA 观点、规则与 IPS"
study: {"section": "Review Course", "module": "Real-World Constraints", "moduleLink": "/cfa/asset-allocation/review/05-constraints/", "step": 5, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "用 After-tax Exposure 进行配置与 Asset Location", "link": "/cfa/asset-allocation/review/05-constraints/step-04"}, "map": {"label": "Learning Map", "title": "Real-World Constraints", "link": "/cfa/asset-allocation/review/05-constraints/"}, "next": {"label": "Next Step →", "title": "把 Behavioral Bias 转成可执行的治理防线", "link": "/cfa/asset-allocation/review/05-constraints/step-06"}}
---

# 将 Tactical Views 放在 SAA 与 IPS 边界内

::: info 本步目标
能区分 systematic / discretionary TAA，检验观点是否有授权，并相对 policy SAA 衡量净增量收益。
:::

## Why · 为什么 Positive Alpha Forecast 仍不能越过 IPS？

TAA 是在战略风险政策之内暂时利用相对回报机会。经理看好某市场，并不获得自行取消上限的权力；高 expected Sharpe 也不能使越界方案成为可执行选择。

本步先辨认观点产生方式，再检查 permitted tilt、实施成本和评价基准。少任何一环，短期好观点都可能变成错误的配置决定。

## Core & Intuition · 观点 → 授权范围 → 实施 → 相对评价

**Discretionary TAA** 使用判断性 macro、valuation 与 market views；**systematic TAA** 使用预先规定的模型或规则捕捉相对回报/趋势。两者都可能参考经济数据，区别是决定如何形成和执行。

| 检查 | 需要回答的问题 |
| --- | --- |
| View / signal | 是相对市场已定价信息的机会，还是仅描述经济？ |
| Permitted tilt | 各资产 upper / lower limits 与整体约束是否允许？ |
| Implementation | 调仓资金来自哪里，有哪些增量 cost / tax / liquidity effects？ |
| Evaluation | 相对原 policy SAA，风险调整与净回报是否改善？ |

**Intuition：** 市场上涨会使 TAA 组合赚钱，但政策组合也可能赚钱；真正评价的是相对基准的增量。Current drifted weights 反映价格历史，policy weights 才表达要比较的 SAA 策略。

KUE 的 IG bonds 已在 lower limit 15%，private property 已在 upper limit 15%。不能只根据 EM 的 forecast 最高就进一步减 bonds 或加 property；应先找 permitted ranges 内能提供资金的调整。例如 developed equity 30% 与 infrastructure 12% 仍有合法空间，可将后者减 1 pp、前者加 1 pp，利用 +2% 相对 −1% 的 forecast；这正是 [KUE 对应练习](/cfa/asset-allocation/questions/2025072102000051#q-2025072102000051-3) 的可行选项。

## Example · KCPF：移动平均规则属于哪种决定？

<p class="source-note">Source: Local Other AA / No.2025072102000050-7 — adapted；答案为推导。</p>

KCPF 计划在 50-day moving average 上穿或下穿 200-day average 时，自动将 equity allocation 增加或减少 5%。

规则事先明确，交易由信号自动触发，所以是 systematic TAA。它不是因为用了市场数据就变成 discretionary，也不只是把上涨权重带回 target 的 routine rebalancing。若该信号持续多年仍偏离政策，则还需复核长期 beliefs 和 SAA，而不是默认永久战术化。

## CFA Language & Formula

::: info Formula · Know how to use
毛增量收益比较同一期间下两套权重：

$$R_{TAA}-R_{SAA}=\sum_i(w_i^{TAA}-w_i^{SAA})R_i$$

两套 weights 均应合计 100%，asset definitions 和 return period 一致；基准为 policy SAA，不是随意选择的 drifted portfolio。净增量还需扣相对实施该 SAA 的额外交易/税务成本，正常 SAA rebalancing cost 不重复计入。
:::

**Sharpe ratio** 可用于相同窗口、同 $r_f$、同口径的 risk-adjusted comparison；还要检查 tails、drawdown 和 constraints，不能将其与 t-statistic 直接相减。**Systematic** 是规则性质，不是收益保证。

## Connection

[Business Cycle CME](/cfa/asset-allocation/review/01-cme-part-1/step-03) 提供条件性观点，[Governance](/cfa/asset-allocation/review/03-overview/step-01) 提供授权。[Rebalancing](/cfa/asset-allocation/review/03-overview/step-06) 有不同目的；[Taxes](/cfa/asset-allocation/review/05-constraints/step-04) 改变观点实施的净增益。

## Exam Focus

- **Exam Trigger — Identify / Evaluate：** 判断规则/主观、政策边界、relative return 与净成本。
- **Common Trap：** 最高 forecast 就买入，不看资金来源及上下限；以 current weights 代 policy SAA；高 risk-adjusted expectation 就允许越界。
- **Boundary Condition：** 缺 weight 或关键 Exhibit 时不能反推增量回报；持续跨周期的环境变化可能要求 SAA review。
- **Constructed Response：** “The moving-average rule is systematic TAA, subject to the approved allocation limits.”

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000050-7 — adapted；答案为推导。</p>

A pension automatically changes equity weight by 5% when a 50-day moving average crosses a 200-day average. This is:


<div class="review-options">

A. De-risking only.

B. Systematic TAA.

C. Discretionary TAA.



</div>

::: tip Answer & Reasoning
**Answer: B.** 预先规定、自动执行的趋势规则。

**Exam Takeaway：** TAA 的有效性要同时通过观点、授权、资金和相对净绩效四项检查。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-taa)

</div>

---
title: "Step 2 — 用 Economic Balance Sheet 看完整风险"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "02 · 完整财富与 Human Capital"
study: {"section": "Review Course", "module": "Overview of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/03-overview/", "step": 2, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "建立 SAA 的目标、授权与责任框架", "link": "/cfa/asset-allocation/review/03-overview/step-01"}, "map": {"label": "Learning Map", "title": "Overview of Asset Allocation", "link": "/cfa/asset-allocation/review/03-overview/"}, "next": {"label": "Next Step →", "title": "选择与目标一致的 Risk Definition", "link": "/cfa/asset-allocation/review/03-overview/step-03"}}
---

# 用 Economic Balance Sheet 看完整风险

::: info 本步目标
能构建 Economic Balance Sheet，计算完整净值，并解释 human capital、用途限制与金融持仓共同造成的风险。
:::

## Why · 为什么只看证券账户会低估投资者的集中风险？

两个人都有 100 万金融资产，但一人收入稳定且与市场低相关，另一人的工资、奖金和持股都依赖同一科技公司，能够承担的风险并不相同。账户余额相同，经济暴露不同。

Economic Balance Sheet 将投资者全部经济资产和未来义务放到现值口径。先算净值，再讨论风险来源和现金可用性；不能让一个净值数字替代这两项判断。

## Core & Intuition · 资产、未来收入、未来支付与用途限制

最小框架是：**financial assets + real assets + human capital / future inflows − explicit liabilities − future consumption / commitments 的现值**。私人教育目标和 endowment 支持义务，即使不是法定债，也影响配置。

| 要恢复的项目 | 为什么必须纳入？ | 后续还要检查什么？ |
| --- | --- | --- |
| Human capital / future inflows | 尚未收到的收入也是经济资源 | 与市场或雇主的相关性；是否可交易、是否可靠 |
| Explicit liabilities | Mortgage、法定养老金等有支付义务 | 时点、币种、利率敏感度与 contingent conditions |
| Consumption / goals | 决定资产需要支持的真实用途 | 优先级、金额、时间与可调整程度 |
| Restricted assets | 有经济价值但不能任意支出 | 对应用途，不能抵销无关义务 |

**Intuition：** Bond-like human capital 是相对稳定、低市场相关的未来收入；equity-like human capital 更依赖周期、奖金或创业结果。金融配置需要考虑这些既有风险，但 human capital 不是可随意买卖调权的证券。

工作生涯推进时，剩余劳动收入现值通常减少，financial capital 可能增加；这是典型 life-cycle 机制，而非每次职业变化都严格单调。净值充足也不代表 liquidity 充足，未来 pledge 不能直接支付今天的账单。

## Example · Law 家庭：净值与雇主风险分别回答

<p class="source-note">Source: Local Other AA / No.2025072102000041-1/2 — adapted；答案为推导。</p>

经济资产为 equities 0.800、bonds 0.450、real estate 0.400 和 human capital 1.025 million，合计 2.675。义务为 mortgage 0.225、consumption 0.750、education 0.275 和 endowment 0.500 million，合计 1.750，净值为 **0.925 million**。

随后检查风险：两位配偶都在 WS 工作，80% 股票也是 WS shares。劳动收入与金融财富可能在同一公司恶化时一起受损。这个问题不会因为净值为正就消失；最值得担忧的是共同来源的集中暴露，而非单纯最大的资产金额。

## CFA Language & Formula

::: info Formula · Know how to use
Economic Net Worth (ENW) 是完整资产与义务的经济现值之差：

$$ENW=PV(economic\ assets)-PV(economic\ liabilities)$$

先列项目，再做加减。已给现值时不再次折现；future consumption 若已含某个教育或目标，应检查是否重复计入。本地 Law 表将项目单列，按其口径相加。
:::

**Quasi-liabilities** 包括未必具有法律强制性的未来支持/支出；**contingent liabilities** 会随条件变化。二者不代表“可忽略的负债”。**Human capital** 的现值描述规模，bond-like / equity-like 描述风险性质。

## Connection

本表帮助选择 [Risk Definition](/cfa/asset-allocation/review/03-overview/step-03)。同样的逻辑在 [Liability-relative allocation](/cfa/asset-allocation/review/04-principles/step-05) 中用于养老金及 sponsor 风险，在 [Liquidity planning](/cfa/asset-allocation/review/05-constraints/step-02) 中进一步区分经济资源与当期可用现金。

## Exam Focus

- **Exam Trigger — Calculate / Discuss：** 先完整列资产和义务，再分别解释净值、相关性与可用性。
- **Common Trap：** 只减 mortgage；漏掉 consumption；把 human capital 当作可交易资产，或将 pledge 当成今天的 cash。
- **Boundary Condition：** Restricted funds 只能服务特定用途；收入的 bond-like / equity-like 判断取决于实际风险，不仅是职业名称。
- **Constructed Response：** 说明 employer shares 同时与两人的 human capital 同源，就能表达真正的集中风险。

> **Quick Recall：** Human capital 很 equity-like，是否意味着金融股票也应更多？\
> **Answer: No.** 已有劳动风险可能要求金融财富分散或对冲。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000041-1/2 — adapted；答案为推导。</p>

Using the Law family figures above, **calculate** economic net worth and **identify** the most concerning financial holding.

::: tip Answer & Reasoning
**Conclusion:** ENW is $925,000; the WS shares are the most concerning holding.

**Scoring Points:**

- Economic assets: $2.675 million; obligations: $1.750 million; net: $0.925 million.
- Both spouses' employment income and their dominant equity holding depend on WS.

**Minimum Passing Answer:** ENW = $2.675m − $1.750m = $0.925m. WS shares concentrate financial wealth in the same source as both spouses' human capital.

**Exam Takeaway：** 完整净值、风险来源和现金可用性，是三个必须分别回答的问题。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-balance)

</div>

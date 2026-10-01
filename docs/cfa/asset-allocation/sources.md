---
title: "Asset Allocation — Sources & Coverage"
pageClass: cfa-study
prev: false
next: false
study: {"section": "Sources & Coverage", "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/#core", "system": null}
---

# Sources & Coverage

## 2027 范围与 LOS

权威范围文件：仓库 `doc/目录.txt`，标题为 **2027 CFA Level III — Portfolio Management Pathway**。它给出本 Topic 的五个 Learning Modules 与内容分支，但没有逐条 LOS 原文/编号，也没有完整 2027 Curriculum 正文。

**TODO: source verification required** — 将逐条官方 2027 LOS 原文/编号核对到本 Topic 的 30 个 Review Steps。目前页面使用本地 outline 和题目建立的复习能力目标，Question metadata 的 `los` 保持 `null`，不伪造官方编号或声称完整官方 LOS 核验已完成。

## 题目来源与答案状态

| Local source | Export label | 独立小题记录 |
| --- | --- | --- |
| `doc/Other/Core-Asset Allocation-AA_OTH.md` | o / Other | 103 |
| `doc/Other/Core-Asset Allocation-CME_OTH.md` | o / Other | 16 |
| `doc/原版书/Core-Asset Allocation-AA_ORIG.md` | c / 原版书 | 47 |
| `doc/原版书/Core-Asset Allocation-CME_ORIG.md` | c / 原版书 | 46 |

这些文件是 2026-09-13 的题目导出，名称/标签未提供可核实的出版年份或具体 CFA 官方出处。**不从 Question ID 前四位推断出版年份，不将 “原版书”自动等同于已验证的官方 EOC。** Public question label 使用实际本地 collection、filename 和原 ID；均为 adapted。

所有 168 道纳入题的 reference answers、scoring points 与 explanations 均由题干和清晰 Exhibit 推导。仓库无答案键，不标 “Official Answer”。MCQ 不使用模型/后台评分；Constructed Response 不自动判分。

## 处理汇总

- 扫描 212 条独立小题记录（按 Case 小题计数）。
- 纳入 168 道唯一题。
- 38 条重复记录合并，映射如下。
- 6 道继续跳过；原 14 道中经独立复核恢复 8 道，详见 [逐条复核结论](/cfa/asset-allocation/skip-review)。

## 重复合并

| 原版书 Case ID | 唯一练习 Case ID | 合并小题数 |
| --- | --- | --- |
| 2017102002000001 | [2025072102000041](/cfa/asset-allocation/questions/2025072102000041) | 8 |
| 2018031301000001 | [2025072102000046](/cfa/asset-allocation/questions/2025072102000046) | 8 |
| 2018031301000002 | [2025072102000047](/cfa/asset-allocation/questions/2025072102000047) | 5 |
| 2018031301000006 | [2025072102000048](/cfa/asset-allocation/questions/2025072102000048) | 2 |
| 2018052801000001 | [2025072102000051](/cfa/asset-allocation/questions/2025072102000051) | 6 |
| 2018052801000002 | [2025072102000050](/cfa/asset-allocation/questions/2025072102000050) | 7 |
| 2018052801000004 | [2025072102000052](/cfa/asset-allocation/questions/2025072102000052) | 2 |

同源不同导出的清晰版本可互校公式/表格，但不凭重复次数认定答案权威。

## 当前跳过记录

[查看原 14 个记录的独立复核、恢复理由与反例 →](/cfa/asset-allocation/skip-review)

| Source question ID | 仍需确认的关键条件 |
| --- | --- |
| [2025060303000002](/cfa/asset-allocation/skip-review#review-2025060303000002) | 仍跳过。Financial crisis 是可能的 intended answer，但三种冲击的长期结果都依赖规模、持续时间、重建和制度反应。本地仅有问题/选项，没有原解释，不能把“灾害或战争之后可能重建升级”推成必然改善长期增长。保留到能核实原解释中的比较模型。 |
| [2020012102000005-2](/cfa/asset-allocation/skip-review#review-2020012102000005-2) | 仍跳过。数据只足以计算 Singer–Terhaar equilibrium required premiums：healthcare 3.4588%、watch 1.9765%、consumer 2.4706%。没有价格、cash-flow valuation 或独立 forecast / implied-return 比较。更高 required premium 不等于 undervaluation；较低 premium 也不等于便宜。第 1 小题继续保留。 |
| [2025072102000019](/cfa/asset-allocation/skip-review#review-2025072102000019) | 仍跳过。源题的 C（global equity indexes correlation close to one）可能是其 homogeneity 教学意图，但“over any reasonably long time period”仍缺指数集合、币种和相关性条件。一般国际股票相关性较高不等于稳定接近 1。未改成较弱的说法来制造唯一答案。 |
| [2025072102000041-7](/cfa/asset-allocation/skip-review#review-2025072102000041-7) | 仍跳过。原版书 2017102002000001-7 确认三组合权重清晰，但仍没有目标 future amount / funding basis、组合 minimum-return 或 success-probability 数据。75/25 对 moderately important twenty-year goal 的建议不能唯一定位本题 high-probability endowment 目标；选择中间风险 Portfolio 3 只是可能意图，不能替代资金与概率条件。 |
| [2025072102000046-7](/cfa/asset-allocation/skip-review#review-2025072102000046-7) | 仍跳过。两导出均只给 domestic bonds 最低 expected return 与对其他类最低 covariance，没有自身 variance 或完整 VCV。Risk parity 依赖 w_i(Σw)_i，expected return 不决定预算；最低 off-diagonal covariance 不保证最低 MCTR。下面的反例证明缺项会改变答案。 |
| [2025072102000008](/cfa/asset-allocation/skip-review#review-2025072102000008) | 仍跳过。A 可判错，C 的一般 asset-location 建议有支持；但 B 的 exclude baseline rebalancing costs 也可合理理解为仅评估 TAA 的增量成本。净增量应扣 C_TAA−C_baseline，不能仅凭原句认定 B 错误。本地无答案解释可区分这两种读法；不收窄选项含义来强定 C。 |

## 有限条件下保留的题

- OHF 的 TAA equity cell 明确为完整六资产预算条件下推导（65%），不伪装成原始导出单元格；gross incremental return 为 0.525%。
- 主权风险、一般税务处理和 funded-status 的 most / least likely 题使用题目对应的定性框架；分析明确条件，不宣称数学唯一排序或现行税法结论。
- Armstrong goals funding 的首笔 spending 时点未明示：CR 分别显示立即提款与年末提款两种结果，不宣称唯一数字。
- Young municipal-bond 问题：明确 tax-exempt convention 是推断，并同时检查全部收益按 25% 征税的替代；两者均支持 P3。
- Singer–Terhaar 整合变化题：区分 transition valuation gain 与整合后长期 required return；不把 required premium 直接当 valuation attractiveness。
- Property cap/GDP 题：分析中明确 constant cap rate 与 NOI growth≈nominal GDP 的简化假设。
- Macaulay-horizon、safety-first 与 tax-scaling 题均注明简化模型边界，不将结论泛化为现实投资保证。
- SPP Exhibit 3 的 hedge-fund 权重与 Exhibit 2 冲突，保留题不依赖该行；不补改缺失事实。

## Review Coverage Map

按 outline 的每条分支定位复习页；以下是 repository-defined coverage，不是已核验的官方 LOS 列表。

### CME Part 1

- Economic growth → [区分 Trend Growth 与周期增长](/cfa/asset-allocation/review/01-cme-part-1/step-02)
- Business cycle → [从 Business Cycle 识别政策和资产方向](/cfa/asset-allocation/review/01-cme-part-1/step-03)
- Inflation → [区分预期通胀、意外通胀与 Deflation](/cfa/asset-allocation/review/01-cme-part-1/step-04)
- Monetary / Fiscal policy → [把 Monetary / Fiscal Policy 转成利率判断](/cfa/asset-allocation/review/01-cme-part-1/step-05)
- Yield curve / Interest rates → [从 Business Cycle 识别政策和资产方向](/cfa/asset-allocation/review/01-cme-part-1/step-03)

### CME Part 2

- Fixed-income return → [将 Yield、Risk Premium 与实现回报分开](/cfa/asset-allocation/review/02-cme-part-2/step-01)
- Equity return → [从盈利、分红与估值拆解 Equity Return](/cfa/asset-allocation/review/02-cme-part-2/step-02)
- Real estate → [把租金、Cap Rate 与估值平滑串起来](/cfa/asset-allocation/review/02-cme-part-2/step-03)
- Currency → [区分 PPP 长期锚与 Capital Flows 短期力量](/cfa/asset-allocation/review/02-cme-part-2/step-04)
- Volatility → [让 Variance–Covariance Matrix 反映真实风险](/cfa/asset-allocation/review/02-cme-part-2/step-05)

### Overview of Asset Allocation

- Economic balance sheet → [用 Economic Balance Sheet 看完整风险](/cfa/asset-allocation/review/03-overview/step-02)
- Asset-only → [选择与目标一致的 Risk Definition](/cfa/asset-allocation/review/03-overview/step-03)
- Liability-relative → [选择与目标一致的 Risk Definition](/cfa/asset-allocation/review/03-overview/step-03)
- Goals-based → [选择与目标一致的 Risk Definition](/cfa/asset-allocation/review/03-overview/step-03)
- Risk factors → [透过资产标签检查共同 Risk Factors](/cfa/asset-allocation/review/03-overview/step-05)
- Rebalancing → [用成本与风险偏离确定 Rebalancing Policy](/cfa/asset-allocation/review/03-overview/step-06)

### Principles of Asset Allocation

- MVO → [从 Investor Utility 选择有效配置](/cfa/asset-allocation/review/04-principles/step-01)
- Global market portfolio → [减少 MVO 输入误差造成的极端权重](/cfa/asset-allocation/review/04-principles/step-02)
- Monte Carlo / Scenario analysis → [用 Scenario / Monte Carlo 检查路径与目标风险](/cfa/asset-allocation/review/04-principles/step-03)
- Risk budgeting → [用 MCTR 区分 Capital Weight 与 Risk Weight](/cfa/asset-allocation/review/04-principles/step-04)
- Liability-relative allocation → [按 Funding Situation 选择 Liability-relative 方法](/cfa/asset-allocation/review/04-principles/step-05)
- Goals-based allocation → [把 Probability、Horizon 与 Funding Cost 连起来](/cfa/asset-allocation/review/04-principles/step-06)

### Real-World Constraints

- Asset size → [用 Asset Size、Capacity 与 Regulation 划定可行配置](/cfa/asset-allocation/review/05-constraints/step-01)
- Liquidity → [用现金流压力检验 Illiquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02)
- Time horizon → [识别 Goals、Constraints 与 Beliefs 的变化](/cfa/asset-allocation/review/05-constraints/step-03)
- Taxes → [用 After-tax Exposure 进行配置与 Asset Location](/cfa/asset-allocation/review/05-constraints/step-04)
- Regulation → [用 Asset Size、Capacity 与 Regulation 划定可行配置](/cfa/asset-allocation/review/05-constraints/step-01)
- Tactical allocation → [将 Tactical Views 放在 SAA 与 IPS 边界内](/cfa/asset-allocation/review/05-constraints/step-05)
- Behavioral biases → [把 Behavioral Bias 转成可执行的治理防线](/cfa/asset-allocation/review/05-constraints/step-06)

[Learning Map](/cfa/asset-allocation/) · [Question Bank](/cfa/asset-allocation/questions/)

---
title: "Asset Allocation — Sources & Coverage"
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

所有 160 道纳入题的 reference answers、scoring points 与 explanations 均由题干和清晰 Exhibit 推导。仓库无答案键，不标 “Official Answer”。MCQ 不使用模型/后台评分；Constructed Response 不自动判分。

## 处理汇总

- 扫描 212 条独立小题记录（按 Case 小题计数）。
- 纳入 160 道唯一题。
- 38 条重复记录合并，映射如下。
- 14 道因无法可靠确认而跳过，原因逐项列出。

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

## 跳过记录

| Source question ID | 原因 |
| --- | --- |
| 2025060303000002 | 长期增长冲击的选项不能仅由题干唯一排序，无答案键。 |
| 2025060303000023 | 多项主权风险指标相互冲突，列标题损坏且没有可靠答案键。 |
| 2020012102000005-2 | 仅给均衡所需风险溢价，没有价格或预测收益，不能作 valuation attractiveness 排序。 |
| 2025072102000018 | 最低固定权重选项把 residential real estate 与 human capital 的 20%/30% 对调；其他选项也不能准确表达经济风险约束。 |
| 2025072102000019 | global equity indexes 的具体集合与同质性定义缺失，风险/回报/相关性泛化无法唯一确认。 |
| 2025072102000031 | 税率与税制缺失；不能凭利息占比推定所有 major economies 的税务排序。 |
| 2025072102000041-7 | 三个组合没有收益/风险/成功率数据，且高成功率的 endowment 目标与通用 moderately important 示例不能可靠映射到唯一组合。 |
| 2025072102000043-2 | 年龄、短端利率对工资型养老金负债/资产的净影响资料不足，无法唯一比较 funded status。 |
| 2025072102000044-3 | Statement 2 对 systematic risk 的表述与同源非流动性指数局限不一致；没有答案键，不能可靠判唯一选项。 |
| 2025072102000049-5 | TAA public equity weight 缺失、当前权重不合计 100%，关键 Exhibit 3 未导出；不反推缺失权重。 |
| 2025072102000051-3 | IG bonds 已在 lower limit，private real estate 已在 upper limit；预期收益最优选项违反 IPS，不能静默修订权重。 |
| 2025072102000046-2 | 高风险资产的宽band建议混用纯交易次数与总体optimalcorridor口径；与同Topic其他题方向冲突，无答案键，不能唯一确认。 |
| 2025072102000046-7 | 仅给domesticbonds与其他资产的lowcovariance与lowexpectedreturn，缺自身variance/完整VCV，无法可靠推出riskparitycapitalweight相对25%。 |
| 2025072102000008 | TAA成本选项对排除基准rebalancing成本的措辞有歧义，B/C可能分别在incrementalcost与assetlocation语境下成立；没有答案键，不强定唯一MCQ。 |

## 有限条件下保留的题

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

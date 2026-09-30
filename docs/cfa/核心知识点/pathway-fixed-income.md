---
title: "固定收益 · Fixed Income（Pathway）"
collection: 核心知识点
book: "Portfolio Management Pathway"
---

# 固定收益 · Fixed Income（Pathway）

## 单笔负债利率免疫策略

1. 利率免疫策略的目标：尽可能降低债券资产收益率的波动，保证债券可以实现稳定的投资收益，使其实现预期的目标增值，保证期末有足够的现金流偿还负债（minimize the varianceinrealizedrateofreturn）
2. 单期负债免疫的条件是：资产PV ≥负债PV资产的Macaulay duration =负债的到期日（maturity or due date or liability的Macaulay duration）最小化资产的convexity（minimize assetconvexity）
3. 虽然期初资产Mac .Duration等于负债的Mac .Duration，但Duration会随着时间的流逝与利率的改变而改变，且无法保证资产与负债的两个数据变动比例一致。所以随着时间的流逝与利率的改变，资产与负债的Mac .Duration可能不再相等，不再维持免疫。为了保证持续的免疫，需要在利率改变后以及隔期进行Rebalancing ，保证资产与负债的Mac .Duration重新回到相等的免疫条件。

## 多笔负债利率免疫策略

1. 多期负债做Duration-matching免疫的要求是：资产PV ≥负债PV资产BPV =负债BPV （或者使用Money duration数据or使用PVBP数据）资产Convexity>负债Convexity，且最小化minimize资产convexity
2. 构建匹配的过程中可以使用衍生品，使用衍生品的策略称为Derivativesoverlay，借助衍生品的Duration来调节资产的Duration，从而使得：资产BPV +衍生品BPV =负债BPV
3. 在Duration-matching过程中，如果资产的PV大于负债PV存在盈余，且在基金许可的情况下，可以使用或有免疫策略（contingent immunization ），即资产可以短暂退出免疫策略，做主动的投资策略追求收益最大化。可以使用衍生品结合利率预期，主动调节资产端的BPV从而盈利。

## 利率免疫策略的风险

1. 免疫策略会存在诸多风险：模型风险（model risk），即免疫策略的假设与现实不符带来的风险，包括资产与负债指标（如duration）计算的误差风险（measurement error）。利率基差风险（spread risk），影响资产与负债的利率变动不一致，导致免疫出现误差。对手方风险（counterparty creditrisk），使用的衍生品头寸面临的信用风险。抵押品枯竭风险（collateralbecomes exhausted ），使用衍生品头寸时，因为亏损较大需要补交抵押品，可能面临抵押品不足的风险。资产的流动性风险，在contingent immunization里涉及主动策略，主动策略会有频繁的交易，如果资产流动性差将会面临流动性风险。

## 匹配指数的策略

1. 以指数的收益作为衡量基准的债券策略有：完全模拟指数(Pure indexing),增强型跟踪指数(Enhanced indexing)以及主动active management 。其中只有Pure indexing和Enhanced indexing属于跟踪指数的策略，Activemanagement是参考指数收益作为评价，但不要求跟踪指数头寸。
2. 完全模拟指数(pure indexing)是100%复刻指数的头寸与权重，优势是可以完美模拟指数的收益和风险，但实务中基本上不可行。因为完美复刻需要购买指数的所有持仓，购买成本大，且流动性差的债券很难购入，同时需要完美复刻指数的调仓，这会增加交易成本。
3. 增强型跟踪指数(Enhanced -indexing)：利用抽样的方法，抽取指数中具有代表性的债券，跟踪指数中关键的指标。交易成本更小，构建难度更低，一定程度上可以较好地跟踪指数，很好地平衡了成本与跟踪效率。但存在一定跟踪误差（trackingerror）。

## 其他方法获得债券头寸

1. 通过其他方法构建债券指数头寸，这些方法有：投资公募基金（mutual fund）：具有规模优势，适合小资金，更易获得分散化；可以用基金净值NAV完成基金的申赎，但基金的申赎存在时滞（one day time lag），不能实时完成交易。购买ETF ：具有规模优势，适合小资金，更易获得分散化，同时为交易所交易基金，具有较高流动性，可以日内完成ETF份额交易；但当ETF的基金净值NAV不等于ETF二级市场价格时，会因为标的物债券的流动性过差导致套利难以执行，所以可能会出现二级市场价格持续偏离NAV的情况。收益互换（totalreturn swap ）：利用互换合约支付浮动利率现金流，收到标的物债券指数的现金流，用这种办法获得债券头寸。收到的现金流包括标的物债券指数的利息coupon现金流，以及指数价格上升的收益现金流。但当指数价格下跌产生亏损时，除支付约定的浮动利率之外，还需要额外支付价格下跌对应的现金流，承担指数的亏损。

## 利率曲线的变动

1. 利率曲线的变动分为：平行移动（level），斜率的改变（slope），曲度的改变（curvature）平行移动：利率曲线上所有的利率发生同方向，同幅度的变动。衡量债券平行移动影响的指标是Modifiedduration/Effectiveduration（一阶线性影响），以及凸度convexity（二阶非线性影响）。斜率的改变：包括利率曲线变得更加陡峭（steepening）——长期利率相对上升，短期利率相对下降；利率曲线更加平缓（flattening）——短期利率相对上升，长期利率相对下降。在讨论斜率改变时，是把利率曲线分成了短期和长期两段讨论相对改变。曲线弯曲度的改变：将曲线分成了
3. 段——短期，中期及长期利率。短期、长期利率的变动方向一致，中期利率的变动方向相反。当短期、长期利率上升且中期利率相对下降时，称为positive butterflymovement ；当短期、长期利率下降且中期利率上升时，变动称为negative butterflymovement 。
2. 衡量非平行移动的指标只有债券的key rateduration。

## 利率曲线稳定时的策略

1. 利率曲线稳定时的策略理念（stable yield curve）：增加组合的久期/期限（increase duration/maturity）和使用杠杆（using leverage）
2. 利率曲线稳定时的具体策略有：买入并持有（buy -and -hold）：延长投资期，买入更长期的债券并持有至到期，赚长期债券的高收益率。骑乘策略（ridingthe yieldcurve）：维持投资期不变，买入更长期的债券。投资期结束时提前卖出债券，赚到提前卖出债券对应的价差收益。息差策略（Repo Carry trade）：借入短期利率，投资长期利率，赚取息差收益，且为杠杆头寸。

## 利率曲线改变时的策略

1. 预测利率曲线发生平行移动平行下移：增加组合的久期（Duration）——买入更长期/久期更大的债券，或者进入receive fixed payfloating的swap ，或者使用Long futures。平行上移：降低组合的久期——卖出长期债券，进入Pay fixedreceivefloating的swap ，使用short futures。
2. 预测利率曲线发生斜率的改变（steepening——短期利率相对下降，长期利率相对上升）Duration-neutralyieldcurve steepening策略：long短期债券，short长期债券，组合的净duration为0。Bull steepener策略：曲线发生bull steepening，bull代表曲线整体平行下移，叠加短期利率下降更多导致steepening——long短期债券，short长期债券，并且使得组合净duration大于0。Bear steepener策略：曲线发生bear steepening，bear代表曲线整体平行上升，叠加长期上升更多导致的steepening——long短期债券，short长期债券，并且组合的净duration小于0。

## 利率曲线改变时的策略

3. 预测利率曲线发生斜率的改变（Flattening——短期利率相对上升，长期利率相对下降）Duration-neutralyieldcurve flattener策略：long长期债券，short短期债券，组合的净duration为0。Bull flattener策略：bull代表曲线整体平行下移，叠加长期利率下降更多导致曲线更平缓——long长期债券，short短期债券，并且使得组合净duration大于0。Bear flattener策略：bear代表曲线整体平行上升，叠加短期上升更多导致的flattening——long短期债券，short长期债券，并且组合的净duration小于0。

## 利率曲线改变时的策略

4. 预测利率曲度发生的改变（curvature改变）Positivebutterfly改变——短期、长期利率相对上升且中期利率相对下降。策略是Long中期债券（bullet组合），short短期+长期债券（barbell组合），即Long bullet组合+Short barbell组合。Negative butterfly改变——短期、长期利率相对下降，中期利率相对上升。策略是long短期+长期债券（barbell组合），Short中期债券（bullet），即long barbell组合+Short bullet组合。
5. 预测利率曲线波动率发生改变（volatilitychange ）预测波动率上升（volatilityincrease）：long任意option获得long convexity/volatility；或将组合的longoption-freebond换成long putable bond ，因为putable bond里面隐含long putoption预测波动率下降（volatilitydecrease）：short任意option降低组合的convexity/volatility；或将组合里的long option-freebond换成long callablebond ，因为callablebond里隐含short calloption

## 衡量信用风险的指标

1. 衡量固定利率债券信用风险的息差（creditspread forfixed-coupon bond ）息差Yieldspread ：债券的YTM –相近期限国债的YTM 。计算简单，但存在期限的差异导致息差不准确G -spread：债券的YTM –同期限的国债YTM 。衡量精确，可能需要用线性插值法计算同期限的国债YTMI-spread：债券的YTM –同期限的swap rate。Swap rate本身有信用风险，减出来的差值I-spread不是债券的绝对风险衡量，I-spread只衡量债券相对swap rate的相对信用风险。ASW spread（asset swap spread ）：利用swap将债券固定利率转换为浮动利率时，swap里市场参考利率MRR叠加的息差spread 。浮动利率端叠加的spread是为了平衡债券固定利率与swap浮动利率MRR之间的风险，体现了债券固定利率与市场参考利率MRR之间的息差Z-spread ：基于市场即期利率曲线计算的息差spread ，是All-in one spread ，债券的所有风险都装到Z-spread里。只适合不含权债券分析信用风险，含权债券的Z-spread会有权利的补偿，会干扰信用风险的分析。

## 衡量信用风险的指标

2. 衡量固定利率债券信用风险的息差（creditspread forfixed-coupon bond ）OAS （option-adjusted spread）：将债券Z-spread里面的期权补偿踢出，保留信用风险补偿部分，这部分为OAS 。适合分析含权债券的信用风险。CDS Basis（CDS spread –Z-spread ）：用CDS市场上对信用风险Creditrisk的定价（CDS spread ）减去债券市场上对信用风险的定价(Z-spread)。差值反应两个市场的定价误差，当误差过大时，可以在两个市场上进行套利交易（basistrade）（三级不涉及该策略）。

## 衡量信用风险的指标

3. 衡量浮动利率债券信用风险的息差（creditspread forfloating-ratebond ）利息补偿Quoted margin （QM ）：决定浮动利率债券的利息Coupon 。QM的大小取决于债券发行时刻的信用风险，信用风险大的债券，补偿的QM大。债券一旦发行，QM将不再改变。折现率补偿Discount margin （DM ）：DM为浮动利率债券折现率的一部分，实时反映债券的信用风险，当信用风险变化时，DM将发生改变。折现率补偿Z-Discount margin （Z-DM ）：与DM类同，区别是与DM搭配的市场基准利率是单一的MRR ，即(单一的MRR + DM)构成现金流折现率。而Z-DM里面，与Z-DM搭配的是一条MRR curve，即每个期限的现金流使用对应期限的MRR ，（对应期限的MRR+Z -DM ）构成现金流折现率，债券会涉及多个MRR利率，即一条MRR曲线。同一个债券，分母的折现率要一样，即（单一的MRR+DM ）与（一条MRR curve + Z-DM ）一致。如果MRRcurve向上倾斜，会造成现金流使用到的MRR利率越来越大。为了保证整体折现率一致，则Z-DM要小于DM 。

## 分析流动性和尾部风险

1. 分析流动性风险（Liquidityrisk）交易量（trading volume ）和买卖价差（bid-ask spread）:交易量越大，买卖价差越小，代表市场的流动性越好。一般发达国家的国债市场交易量大，且买卖价差小；刚刚发行的债券（on -the-run）流动性最好。
2. 衡量尾部风险（tailrisk）的指标有：VaR （Value atrisk）：在一定时间内，在一定的概率水平下，资产的最大亏损。CVaR （Conditional VaR ）：对损失超过VaR时的所有尾部损失求一个平均值，该平均值为CVaR 。增量VaR （incremental VaR ）：在组合里加入新头寸后，引起的VaR的改变，衡量新增头寸的增量影响。相对VaR （relativeVaR ）：当存在比较基准（benchmark ）时，衡量相对于比较基准的VaR 。
3. 计算债券一个月的，99%概率水平下的VaR ，已知利率的波动率是年化波动率annual volatility1−Duration Δ 2.33 Δ annual volatility Δ Δ market value12

## 利用CDS构建信用策略

1. CDS合约的价格（每1元面值的价格）：CDS Price ≈ 1 + (Fixed Coupon – CDS Spread) × EffSpreadDurCDS
2. CDS的long-short策略预测A板块的信用风险上升，B板块的信用风险下降：买入A板块的CDS合约，赚取风险下降带来的理赔，同时卖出B板块的CDS合约，赚取卖出保险的保费——Buy CDS protectionon A,SellCDS protectionon B

## 信用风险策略

1. 信用风险曲线保持不变（creditcurve remain stable）买入更长期的债券赚取更大的信用风险补偿（higher creditspread），或者买入评级更低的债券赚取更大的信用风险补偿。构建买入并持有策略（buy -and -hold）：买入信用风险更大、评级更低的债券，因为预测信用曲线维持不变，投资债券可以赚到稳定的信用风险补偿，买入评级更低的债券可以稳定赚到更大的补偿。信用风险曲线的骑乘策略（riding the yield curve）：买入更长期的债券，提前卖出债券赚取债券的价差收益。策略的收益包括：利息coupon收益与买卖价差收益。但因为是只关注信用风险，所以策略的收益只能是和信用风险相关，即与信用风险相关的coupon收益以及与信用风险相关的价差收益。

## 信用风险策略

2. 信用风险曲线改变对应的策略（dynamic creditspread curve strategy）预测经济复苏（recovery）：垃圾债（high-yieldbond ）的信用风险补偿（creditspread ）大幅下降，可以提前投资该类债券赚取价格大幅上升的收益预测经济复苏，伴随信用风险曲线更陡峭（steepening）：短期信用风险相对下降，长期信用风险相对上升。买入长期CDS合约获得保护，卖出短期CDS合约赚取期权费——buy CDS protection on long-term,sellCDS protectionon short-term预测经济变差（downturn ）：卖出对信用风险敏感较大的垃圾债，避免垃圾债价格大幅下跌的亏损预测经济变差，且对低等级债券的不利影响更大：买入低等级债券的CDS合约获得保护，卖出高等级债券的CDS合约赚取保费。

---
title: "交易执行 · Trading"
collection: 核心知识点
book: "Core Subjects"
---

# 交易执行 · Trading

## 交易成本

1. 分固定成本和可变成本，可变成本分显性成本和隐性成本。
2. 隐性成本包含：The bid–ask spread 、市场影响、延迟成本和机会成本。
3. bid-ask spread = best ask price-best bid price
4. 市场影响（或价格影响）是指交易对交易价格的影响。想要完成大额订单的交易员通常必须调整价格，以鼓励其他人与他们进行交易。
5. 延迟成本（也称为滑点）是由于无法立即完成预期交易而产生的。当价格如交易者所预期那样变动，但交易者却未能及时成交订单时，他们就无法获利。
6. 机会成本（或未实现的利润/损失）是由于未能及时执行交易而产生的。当交易者未能及时执行订单，而价格按预期方向移动时，其潜在盈利会因机会成本而损失。

## 交易成本的评估

1. Effectivespread fora buy order = 2 × (Trade price-midquote ); Effectivespread fora sellorder = 2×(midquote -Trade price)
2. Effectivespread关于交易成本的评估——For buy ：Trade size×[Trade price–(Bid+ Ask)/2];For sell：Trade size×[(Bid+ Ask)/2 –Trade price]。其不足之处是没有考虑延迟成本和机会成本。
3. Implementation Shortfall是指纸面投资组合价值超过实际投资组合价值的部分，考虑了市场影响、延迟成本和机会成本。
4. VWAP关于交易成本的评估—— For buy orders: Trade size×(Trade VWAP − VWAP benchmark)；Forsell orders: Trade size×(VWAP benchmark − Trade VWAP)。该方法没有考虑市场影响。

## 电子市场

1. 电子交易使得买卖价差和交易成本大幅下降。竞争促使价差缩小，使得需要的买方交易员的数量减少，并且比人工交易员更高效地处理交易。
2. 高频交易员完成往返通常只需几毫秒，一天之内，他们的交易次数可能超过一千次。

## ElectronicTrading System Facilities

1. 速度非常重要，降低延迟的两种方法：FastCommunications和FastComputations 。提高FastCommunications方法：最小化通信距离和最大限度地提高线路速度。提高Fast Computations方法：电子交易商使用非常快的计算机，还必须运行非常高效的软件，并优化他们的计算机代码以提高速度以及创建列联表。

## 电子交易风险

1. 当程序员犯错误，交换服务器处理流量的能力不足，或者计算机硬件或通信线路出现故障时，就会发生电子交易所交易系统故障。
2. 失控的算法：编程错误导致的意外命令。
3. 胖手指错误：手工交易员提交的订单比预期的要大。
4. 过大的订单：交易员会试图执行一个规模过大的可成交订单。
5. 恶意订单流：例如，拒绝服务攻击。

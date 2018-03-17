## 排序算法

> Wiki (English): https://en.wikipedia.org/wiki/Sorting_algorithm
>
> Wiki (中文): [https://zh.wikipedia.org/wiki/排序算法](https://zh.wikipedia.org/wiki/排序算法)

### 定义

维基百科给出的定义如下：

> In [computer science](https://en.wikipedia.org/wiki/Computer_science), a **sorting algorithm** is an algorithm that puts elements of a list in a certain order. The most-used orders are numerical order and *lexicographical order*[^字典序]. Efficient sorting is important for optimizing the use of other algorithms (such as search and merge algorithms) which require input data to be in sorted lists; it is also often useful for *canonicalizing*[^规范化] data and for producing human-readable output. More formally, the output must satisfy two conditions:
>
> 1. The output is in nondecreasing order (each element is no smaller than the previous element according to the desired total order);
> 2. The output is a *permutation*[^排列] (reordering but with all of the original elements) of the input.
>
> Further, the data is often taken to be in an **array**, which allows random access, rather than a **list**, which only allows sequential access, though often algorithms can be applied with suitable modification to either type of data.

### 分类

维基百科给出的划分(已翻译)如下：

* 以输入的列表的大小为问题的规模$$n$$的[计算复杂度](https://zh.wikipedia.org/wiki/計算複雜性理論)（最差、平均、最优）

  > #### 渐进上限
  >
  > 假如当且仅当存在正实数$$M$$和实数$$x_0$$，使得对于所有的$$x>x_0$$，均有：$$|f(x)|\le{M|g(x)|}$$成立，我们就可以说：当$$x\rightarrow\infty$$时，$$f(x)=O(g(x))$$，通常$$x\rightarrow\infty$$的条件可略去。
  >
  > 此概念也可以用于描述函数$$f$$在接近实数$$a$$时的行为，通常$$a=0$$。当且仅当存在正实数$$M$$和实数$$\delta$$，使得对于所有符合$$0\le{|x-a|\le\delta}$$的$$x$$，均有$$|f(x)|\le{M|g(x)|}$$。
  >
  > #### 其他渐进符号
  >
  > | 符号                    | 定义                                                         |
  > | ----------------------- | ------------------------------------------------------------ |
  > | $$f(n)=O(g(n))$$        | 渐近上限                                                     |
  > | $$f(n)=o(g(n))$$        | Asymptotically negligible渐近可忽略不计(![\lim {}{\frac {f(n)}{g(n)}}=0](https://wikimedia.org/api/rest_v1/media/math/render/svg/82e179fc2fecb98329a4888bbd476ea4e1c9097d)) |
  > | $$f(n)=\Omega{(g(n))}$$ | 渐近下限（当且仅当![g(n)=\mathrm {O} (f(n))](https://wikimedia.org/api/rest_v1/media/math/render/svg/8162f119c81b6eb56e6268d2ed8dc4e91ff34bfa)） |
  > | $$f(n)=\omega{(g(n))}$$ | Asymptotically dominant渐近主导（当且仅当![g(n)=o(f(n))](https://wikimedia.org/api/rest_v1/media/math/render/svg/1a3f56c4faa0b1249c48a0441787c24ccf1ad19a)） |
  > | $$f(n)=\Theta{(g(n))}$$ | Asymptotically tight bound渐近紧约束（当且仅当![f(n)=\mathrm {O} (g(n))](https://wikimedia.org/api/rest_v1/media/math/render/svg/ae173e9684293e8d13e23d8154c11177c644781a)且![f(n)=\Omega (g(n))](https://wikimedia.org/api/rest_v1/media/math/render/svg/9df8a463b6e106cce5d68174c1df5768a1682ef8)） |
  >
  > **注意**：大O符号经常被误用：有的作者可能会使用大O符号表达大Θ符号的含义。因此在看到大O符号时应首先确定其是否为误用。


​    

  对于典型的连续性排序算法来说，不错的时间复杂度为$$O(nlog_2{n})$$；而对于并行性的排序算法来说，较好的时间复杂度为$$O(log_2n)$$；而较差的算法的时间复杂度为$$O(n^2)$$。

  理想的连续性排序算法的时间复杂度为$$O(n)$$，但是在平均情况下无法达到。最优的并行性排序算法的时间复杂度为$$O(log_2n)$$。

* 交换的[计算复杂度](https://zh.wikipedia.org/wiki/計算複雜性理論)（对于[原地算法](https://zh.wikipedia.org/wiki/原地算法)来说）

* 内存的使用量

  较为特殊的是，一些排序算法为原地算法。严格来说，除了需要排序的元素占用的空间，原地算法只需要 $$O(1)$$的空间复杂度；有时额外空间复杂度为$$O(log{n})$$的算法也被看作原地的。

* 递归

* 稳定性

* 是否为[比较排序](https://en.wikipedia.org/wiki/Comparison_sort)

* 大体方法


  插入、交换、选择、合并等。交换排序：冒泡排序、快速排序；选择排序：堆排序、鸡尾酒排序

* 串／并行

* 适应性

  对输入提前排序是否会影响算法的运行时长，照顾到这点的排序算法称为具有[适应性](https://en.wikipedia.org/wiki/Adaptive_sort)的。

### 常见算法

尽管有着众多的排序算法，但实际上仅有一小部分算法起着支配作用。插入排序算法用在小型数据集合中，而对于大型的数据集合，通常使用[渐进最优算法](https://en.wikipedia.org/wiki/Asymptotically_optimal_algorithm)（堆排序、快速排序、归并排序）。

高效的排序的算法通常使用混合算法：用渐进最优算法进行大体的排序，而在递归的结尾使用插入排序对小型列表排序。高度调教的实现会使用更为精细的变种算法，例如：[Timsort](https://en.wikipedia.org/wiki/Timsort)（包含归并排序、插入排序以及额外的逻辑，被Java、Android和Python使用）、[itrosort](https://en.wikipedia.org/wiki/Introsort)[^内省排序]（包含快速排序和堆排序，它的不同形式被一些C++库和.Net所实现）。

对于更多的严格的数据，例如：对于有着固定的间隔的数字们，通常使用[外部排序](https://en.wikipedia.org/wiki/External_sorting)（又称为：分发排序），例如：[基数排序](https://zh.wikipedia.org/wiki/基数排序)、[计数排序](https://zh.wikipedia.org/wiki/计数排序)。

#### 简单排序

两种简单排序：插入排序与选择排序都在少量数据上都表现得很好（由于较低的开销），但在大量数据上并不让人满意。

通常插入排序的要比选择排序更快（需要更少的比较），但选择排序需要写的语句更少，可以用在当写的语句数成为约束时使用。

##### 插入排序

**插入排序**（英语：Insertion Sort）是一种简单直观的[排序算法](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。**插入排序**在实现上，通常采用原地（in-place）排序（即只需用到$$O(1)$$的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

##### 选择排序

**选择排序**（Selection sort）是一种简单直观的[排序算法](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)。它的工作原理如下。首先在未排序序列中找到最小或最大元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

#### 高效排序

实际中使用的排序算法的平均时间复杂度的渐进上限为$$O(n*logn)$$，通常有：堆排序、归并排序、快速排序，三者都有各自的优缺点，其中最为显著的是：简单的归并排序算法需要$$O(n)$$的额外空间复杂度、简单的快速排序的最差时间复杂度为$$O(n^2)$$，当这些缺席可以通过更复杂的改进来解决或改善。

尽管这些算法在处理随机数据时都是渐进高效的，但是为了应用于现实世界中的数据，需要使用多种改进。

* 首先，这些算法在处理小型数据时花费的开销是显著的，所以经常采用混合算法，通常当数据的规模足够小时切换到插入排序算法。
* 其次，这些算法通常在输入的数据已经有序或接近有序时（这种情况在现实世界中是存在的，此时，使用恰当的算法可以在$$O(n)$$时间内完成排序）表现得比较差。
* 最后，这些算法可能是不稳定的，而通常情况下我们希望算法是稳定的。

通常我们采用更为精细的算法，例如：

* Timsort：基于归并排序
* 自省排序introsort：基于快速排序，回落到堆排序

##### 堆排序

堆排序是简单的选择排序的一种更为高效的版本。

##### 归并排序

归并操作（merge），也叫归并算法，指的是将两个已经排序的序列合并成一个序列的操作。归并排序算法依赖归并操作。

##### 快速排序

快速排序（英语：Quicksort），又称**划分交换排序**（partition-exchange sort），简称[快排](https://zh.wikipedia.org/wiki/%E5%BF%AB%E6%8E%92)，一种[排序算法](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)，最早由[东尼·霍尔](https://zh.wikipedia.org/wiki/%E6%9D%B1%E5%B0%BC%C2%B7%E9%9C%8D%E7%88%BE)提出。在平均状况下，排序{\displaystyle n}![n](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b)个项目要![{\displaystyle \Theta (n\log n)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1b8781cea4259c3bd43204e02d08b9b9ce8fe0ff)（[大O符号](https://zh.wikipedia.org/wiki/%E5%A4%A7O%E7%AC%A6%E5%8F%B7)）次比较。在最坏状况下则需要![{\displaystyle \Theta (n^{2})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/215877752c4f392a7276328d4d37709bf7c3f55d)次比较，但这种状况并不常见。事实上，快速排序通常明显比其他![{\displaystyle \Theta (n\log n)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1b8781cea4259c3bd43204e02d08b9b9ce8fe0ff)算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地达成。

#### 冒泡排序及其变种

冒泡排序及其变种（如：鸡尾酒排序）都是很简单但非常低效率的排序算法。

##### 冒泡排序

冒泡算法可以用于小型的数据排序，小到渐进的低效性不会被着重考量。

又或者，可以将冒泡算法应用于几乎有序的列表中，这时排序算法的时间复杂度为$$O(n)$$级别的。

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Bubblesort-edited-color.svg/512px-Bubblesort-edited-color.svg.png)

##### 希尔排序

希尔排序是对插入排序的改进。插入算法的时间复杂度为$$O(kn)$$，$$n$$是列表的长度，而$$k$$是两个脱离位置（有序时的位置）的元素的距离。所以，当列表已经几乎有序时，插入排序可以非常快。因此，第一步不去对远隔的元素进行排序，而是逐渐的讲元素之间的距离缩短，来让最终的排序变得异常迅速。

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Shell_sorting_algorithm_color_bars.svg/512px-Shell_sorting_algorithm_color_bars.svg.png)

希尔排序的时间复杂度是个开放性的问题，取决于元素的间隔的选取，广为人知的有$$O(n^2)$$、$$O(n^{4/3})$$和$$O(nlog_2)$$。希尔排序是原地算法，而且仅需要相对较少的代码，并且不需要使用调用栈，使得它在嵌入式系统和操作系统内核中十分重要。

#####  梳排序

梳排序（Comb sort）是一种由[Wlodzimierz Dobosiewicz](https://en.wikipedia.org/wiki/Wlodzimierz_Dobosiewicz)于1980年所发明的不稳定[排序算法](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)，并由[Stephen Lacey](https://en.wikipedia.org/wiki/Stephen_Lacey)和[Richard Box](https://en.wikipedia.org/wiki/Richard_Box)于1991年四月号的[Byte杂志](https://en.wikipedia.org/wiki/Byte_Magazine)中推广。梳排序是改良自[泡沫排序](https://zh.wikipedia.org/wiki/%E6%B3%A1%E6%B2%AB%E6%8E%92%E5%BA%8F)和[快速排序](https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)，其要旨在于消除*乌龟*，亦即在阵列尾部的小数值，这些数值是造成泡沫排序缓慢的主因。相对地，*兔子*，亦即在阵列前端的大数值，不影响泡沫排序的效能。

在泡沫排序中，只比较阵列中相邻的二项，即比较的二项的*间距（Gap）*是1，梳排序提出此间距其实可大于1，改自[插入排序](https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F)的[希尔排序](https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F)同样提出相同观点。梳排序中，开始时的间距设定为阵列长度，并在循环中以固定比率递减，通常*递减率*设定为1.3。在一次循环中，梳排序如同泡沫排序一样把阵列从首到尾扫描一次，比较及交换两项，不同的是两项的间距不固定于1。如果间距递减至1，梳排序假定输入阵列大致排序好，并以泡沫排序作最后检查及修正。

###### 递减率

递减率的设定影响着梳排序的效率，原作者以随机数作实验，得到最有效递减率为1.3的。如果此比率太小，则导致一循环中有过多的比较，如果比率太大，则未能有效消除阵列中的乌龟。

亦有人提议用![{\displaystyle 1/\left(1-{\frac {1}{e^{\varphi }}}\right)\approx 1.247330950103979}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5a690af8744dedfc8e5c7c5031c6b4cac1ad68a3)作递减率，同时增加换算表协助于每一循环开始时计算新间距。

因为编程语言中乘法比除法快，故会取递减率倒数与间距相乘，![{\displaystyle {\frac {1}{1.247330950103979}}=0.801711847137793\approx 0.8}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cf95dfe8165efadd4f406a92b6874f423f9a84c4)

设定递减率为1.3时，最后只会有三种不同的间距组合：(9, 6, 4, 3, 2, 1)、(10, 7, 5, 3, 2, 1)、或 (11, 8, 6, 4, 3, 2, 1)。实验证明，如果间距变成9或10时一律改作11，则对效率有明显改善，原因是如果间距曾经是9或10，则到间距变成1时，数值通常不是递增序列，故此要进行几次泡沫排序循环修正。加入此指定间距的变异形式称为*梳排序-11(Combsort11)*。

#### 分发排序

##### 计数排序

##### 筒排序

##### 基数排序





[^内省排序]: introspective内省的 

[^字典序]: [Wiki条目](https://zh.wikipedia.org/wiki/字典序)
[^规范化]: [Wiki条目](https://en.wikipedia.org/wiki/Canonicalization)
[^排列]: [Wiki条目](ttps://zh.wikipedia.org/wiki/置換)


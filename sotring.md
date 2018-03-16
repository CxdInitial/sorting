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



##### 快速排序

#### 冒泡排序及其变种

##### 冒泡排序

##### 希尔排序

##### 梳排序

#### 分发排序

##### 计数排序

##### 筒排序

##### 基数排序





[^内省排序]: introspective内省的 

[^字典序]: [Wiki条目](https://zh.wikipedia.org/wiki/字典序)
[^规范化]: [Wiki条目](https://en.wikipedia.org/wiki/Canonicalization)
[^排列]: [Wiki条目](ttps://zh.wikipedia.org/wiki/置換)


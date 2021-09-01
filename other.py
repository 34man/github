import numpy as np

# asarray 和 array 都能产生新数组，但是 存拷问题
# 但区别是 np.array（默认情况下）将会copy该对象，而 np.asarray除非必要，否则不会copy该对象
li = [1,2,3,4]
new = np.asarray(li)

new1 = np.array(li)
new
new1
li = [2,2,2,2]
new
new1


# 补充：视图与副本
#
# 视图与副本的区别我们在后面 Numpy 拷贝与输出的部分还会再讲到，这里我们先简单解释一下
#
# python的 list 的切片返回是原数据的副本，即开辟了一个新的内存地址储存数据，因此修改切片出来的结果，原数据并不会发生改变。
#
# 而numpy 以效率为主，所以 numpy 的切片返回的是原数据的视图，即不会创建新的内存地址，而是对原数据内存地址的引用。所以对numpy 切片结果进行修改会发现，原数据也一起发生了改变。
#
# 注意：numpy 中所有的运算操作符都不会为数组创建副本

li = [1,2,3,4]
arr = np.asarray(li)
new = arr[slice(2, 3)]
new
arr[2] = 30
new
arr

# 使用索引数组进行索引访问
# NumPy 数组可以使用其他数组（或任何其他可以转换为数组的类似序列的对象，如列表，除元组之外的索引;请参阅本文档末尾的原因）。
#
# 注意：对于索引数组的所有情况，返回的是原始数据的副本，而不是切片获取的视图。
#
# 索引数组必须是整数类型。数组中的每个值指示要使用的数组中的哪个值代替索引。

li = [1, 2, 3, 4]
arr = np.asarray(li)
a = arr[1]
arr[2] = 30
a

花式索引：
x = np.arange(32).reshape((8,4))
x
print (x[[4,2,1,7]])

numpy.concatenate
numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，格式如下：

x1 = np.asarray(range(15)).reshape(3, 5)
x2 = np.asarray(range(15, 30)).reshape(3, 5)
x1
x2

np.concatenate((x1, x2), axis=1)
np.concatenate((x1, x2), axis=0)

numpy.stack
numpy.stack 函数用于沿新轴连接数组序列
x1
x2


np.stack((x1, x2), axis=1)

np.stack((x1, x2), axis=0)

np.stack((x1, x2), axis=2)

当 axis=0 的时候，意味着整体，也就是一个2行3列的数组。所以对于0维堆叠，相当于简单的物理罗列，比如这四个数组代表的是4张图像的数据，
进行0维堆叠也就是把它们按顺序排放了起来，形成了一个(4,2,3)的3维数组。

当 axis=1 的时候，意味着第一个维度，也就是数组的每一行。所以对于1维堆叠，4个2行3列的数组，各自拿出自己的第一行数据进行堆叠形成3
维数组的第一“行”，各自拿出自己的第二行数据进行堆叠形成3维数组的第二“行”，从而形成了一个(2,4,3)的3维数组。

当 axis=2 的时候，意味着第二个维度，注意：千万不要理解成2维堆叠是对每一列拿出来进行堆叠！这个堆叠是对于整个维度来讲的，我们把一维
空间理解为一条线，而二维空间则是一个平面。从第二个维度堆叠可以看作平面与平面的堆叠。

numpy.split
numpy.split 函数沿特定的轴将数组分割为子数组，格式如下：

numpy.split(arr, indices_or_sections, axis)
参数说明：

arr：被分割的数组
indices_or_sections：果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置（左开右闭）
axis：设置沿着哪个方向进行切分，默认为 0，横向切分，即水平方向。为 1 时，纵向切分，即竖直方向。

x1[0]

np.split(x1[0], indices_or_sections=1)

np.split(x1[0], [2])

np.delete(x1[0], 0)

np.insert(x1[0], 0, 0)

np.append(x1[0], 0)

np.unique(x1)


浅拷贝 深拷贝 无拷贝
x1 = np.asarray(range(5))
x2 = x1   # 简单的引用
x1 is x2
print(id(x1), id(x2))
x1[1] = 3
x2
x2[1] = 5
x1
这里浅拷贝和 python 中的浅拷贝机制略微有些区别，如前面介绍过的切片操作就是一种浅拷贝。浅拷贝不同的 ndarray
对象可以共享相同的数据区。view方法可以新建一个新的 ndarray，但是只会 copy 父对象，不会 copy 底层的数据，共用原始引用指向的对象数据。
如果在view上修改数据，会直接反馈到原始对象。

浅拷贝 用 .view() 和无拷贝一样，深拷贝用.copy()


pass



pass












pass

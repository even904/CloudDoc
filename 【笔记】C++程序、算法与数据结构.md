---
author: [Even]
date: [2025年04月05日]
update: [2025年04月05日]
title: [【笔记】C++程序、算法与数据结构]
tags: [笔记,课程,C++,算法,数据结构]
---


# C++程序、算法与数据结构

## C++匿名函数

``` Cpp
[capture](parameters) -> return_type { 
    // 函数体 
}
```

1. `[capture]`：捕获列表，用于捕获外部作用域中的变量。

-   `[]`：不捕获任何变量。
-   `[=]`：按值捕获所有外部变量。
-   `[&]`：按引用捕获所有外部变量。
-   `[x, &y]`：按值捕获 x，按引用捕获 y。
-   `[this]`：捕获当前类的 this 指针。

2. `(parameters)`：参数列表，和普通函数的参数列表类似。

    可以为空，表示没有参数。
    如果没有参数，括号可以省略。

3. `-> return_type`：返回类型（可选）。

    如果编译器能够推导出返回类型，则可以省略 `-> return_type`。
    如果返回类型明确或复杂，建议显式指定。

4. `{ function_body }`：函数体，包含具体的逻辑。

示例：
```Cpp
sort(intervals.begin(),intervals.end(),[](vector<int>& a, vector<int>& b) {return a[1] < b[1];});
```

## std::vector

#### (1) 插入元素

- push_back(value)：在末尾添加一个元素。
```Cpp
vec.push_back(42);
```
- emplace_back(args...)：在末尾直接构造一个元素（效率更高）。
```Cpp
vec.emplace_back(42);
```
- insert(pos, value)：在指定位置插入一个元素。
```Cpp
vec.insert(vec.begin() + 2, 99); // 在索引 2 的位置插入 99
```
- insert(pos, n, value)：在指定位置插入 n 个相同的元素。
```Cpp
vec.insert(vec.begin(), 3, 7); // 在开头插入 3 个 7
```
- insert(pos, first, last)：在指定位置插入一个范围内的元素。
```Cpp
    std::vector<int> other = {10, 20};
    vec.insert(vec.end(), other.begin(), other.end());
```
#### (2) 删除元素

- pop_back()：移除最后一个元素。
```Cpp
vec.pop_back();
```
- erase(pos)：移除指定位置的元素。
```Cpp
vec.erase(vec.begin() + 2); // 移除索引 2 的元素
```
- erase(first, last)：移除一个范围内的元素。
```Cpp
vec.erase(vec.begin(), vec.begin() + 3); // 移除前 3 个元素
```
- clear()：清空所有元素。
```Cpp
vec.clear();
```
## C++迭代器

```Cpp
// 正向迭代器
for (auto it = vec.begin(); it != vec.end(); ++it) {
    std::cout << *it << " ";
}
// 反向迭代器
for (auto rit = vec.rbegin(); rit != vec.rend(); ++rit) {
    std::cout << *rit << " ";
}
```

支持迭代器的对象可以使用基于范围的for循环(Range-based for loop)，遍历更简便

示例：
```Cpp
    for(const vector<int> & person: people){
        ans.insert(ans.begin() + person[1] , person);
    }
```
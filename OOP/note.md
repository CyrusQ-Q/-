# 0. OOP-Python 面向对象
- Python 的面向对象
- 面向对象编程
    - 基础
    - 共有私有
    - 继承
    - 组合
- 魔法函数
    -魔法函数概述
    -构造类魔法函数
    -运算魔法函数

# 1. 面向对象概述（ObjectOriented.OO）
- OOP思想：
    - 接触到任意一个任务，首先想到的是任务这个世界
- 几个名词
    - OO : 面向对象
    - OOA : 面向对象的分析
    - OOD : 面向对象的设计
    - OOI : 面向对象的实现
    - OOP : 面向对象的编程
    - OOA -> OOD -> OOI: 面向对象的实现过程
- 类和对象的概念
    - 类：抽象名词，代表一个集合，共性的事物。
    - 对象：具象的事物，单个个体
    - 类与对象的关系
        - 一个具象，代表一类事物的某一个个体
        - 一个是抽象，代表的是一类事物
    - 类中的内容应该具有两个内容
        - 表明事物的特征，叫做属性（变量）
        - 表明事物的功能或者动作，称为成员方法（函数）
        
# 2. 类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值可以使用None
    - 案例 01.py
- 实体化类
        
        变量 = 类名 ()     #实例化了一个对象
- 访问对象成员
    - 使用点操作符
            
            obj.成员属性名称
            obj.成员方法
- 对象所有成员检查

        # dict 前后各有两个下划线
        obj.__dict__
- 类所有的成员
        
        # dict 前后各有两个下划线
        class_name.__dict__            
           
    
# 3. anaconda 的基本使用
- anaconda主要是一个虚拟环境管理器，还是一个安装包管理器
- conda list: 显示anaconda安装的包
- conda env list: 显示anaconda的虚拟环境列表
- conda create -n xxx python=3.6: 创建版本为3.6的虚拟环境，名称为xxx
class Person():
    # 函数的名称可以任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        # 所有输入的姓名以大写形式保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "运行一下name")

p1 = Person()
p1.name = "XiaoHong"
print(p1.name)
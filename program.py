# # # class A:
# # #     def __init__(self, name):
# # #         self.name = name

# # #     def print_name(self):
# # #         print(self.name)

# # # class B(A):
# # #     def __init__(self, name, age):
# # #         super().__init__(name)
# # #         self.age = age

# # #     def print_age(self):
# # #         print(self.age)

# # # a = A("Sanika")
# # # b = B("Sanika", 20)

# # # a.print_name()
# # # print("--------------------------------")
# # # b.print_name()
# # # b.print_age()

# # class A:
# #     def abc(self):
# #         print("A")

# # class B(A):
# #     def xyz(self):
# #         print("B")
# # class C(B):
# #     def pqr(self):
# #         print("C")

# # f = C()
# # f.abc()
# # f.xyz()
# # f.pqr()

# class A:

#     def abc(self):
#         print("A")

# class B:
#     def xyz(self):
#         print("B")

# class C(A, B):
#     def pqr(self):
#         print("C")

# f = C()
# f.abc()
# f.xyz()
# f.pqr()

class A:
    def abc(self):
        print("A")
class B(A):
    def abc(self):
        print("B")

f = B()

f.abc()
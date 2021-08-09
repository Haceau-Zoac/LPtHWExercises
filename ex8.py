from turtle import get_shapepoly


格式化器 = "{} {} {} {}"

print(格式化器.format(1, 2, 3, 4))
print(格式化器.format("一", "二", "三", "四"))
print(格式化器.format(True, False, False, True))
print(格式化器.format(格式化器, 格式化器, 格式化器, 格式化器))
print(格式化器.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
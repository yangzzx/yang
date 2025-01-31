import random

choices = ["石头", "剪刀", "布"]

print("欢迎来到石头剪刀布游戏！")
while True:
    user_choice = input("请输入你的选择（石头、剪刀、布），输入 '退出' 结束游戏：")
    if user_choice == "退出":
        print("游戏结束，再见！")
        break
    if user_choice not in choices:
        print("输入无效，请输入 石头、剪刀 或 布。")
        continue

    computer_choice = random.choice(choices)
    print(f"计算机选择了：{computer_choice}")

    if user_choice == computer_choice:
        print("平局！")
    elif (
        (user_choice == "石头" and computer_choice == "剪刀") or
        (user_choice == "剪刀" and computer_choice == "布") or
        (user_choice == "布" and computer_choice == "石头")
    ):
        print("你赢了！")
    else:
        print("你输了！")
def fight():
    # 我的血条
    my_hp = 1000
    # 敌人的血条
    your_hp = 1000
    # 我的攻击力
    my_power = 80
    # 敌人的攻击力
    your_power = 60

    while True:
        # 我剩余血条 等于 我的之前血条 减去 敌人的一次攻击
        my_hp = my_hp - your_power
        # 敌人剩余血条 等于 敌人的之前血条 减去 我的一次攻击
        your_hp = your_hp - my_power
        if my_hp <= 0:
            print("我输了")
            break
        elif your_hp <= 0:
            print("你输了")
            break
# 调用该方法
fight()






import math

def ballistic_compensation(target_distance):
    # 常量定义
    GRAVITY = 9.8  # 重力加速度，单位 m/s^2
    AIR_RESISTANCE = 0.01  # 空气阻力常数

    # 计算补偿高度
    time_of_flight = math.sqrt((2 * target_distance) / AIR_RESISTANCE)
    compensation_height = (GRAVITY * time_of_flight**2) / 8

    return compensation_height

# 测试
target_distance = float(input("请输入目标距离（单位：米）："))
compensation = ballistic_compensation(target_distance)
print("补偿高度为：", compensation, "米")
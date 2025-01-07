import hashlib
import os
import time
import psutil
from flask import Flask, jsonify, request

app = Flask(__name__)

# 线性同余法的参数
a = 1664525
c = 1013904223
m = 2**32

# 初始种子
seed = int(time.time()) + os.getpid() + psutil.virtual_memory().percent

# 线性同余法生成随机数
def lcg(seed):
    global a, c, m
    return (a * seed + c) % m

# 使用哈希混合增强随机性
def hash_mix(random_value):
    return int(hashlib.sha256(str(random_value).encode('utf-8')).hexdigest(), 16)

# 结合时间戳、进程ID、内存等熵源
def entropy_source():
    return int(time.time() * 1000) + os.getpid() + psutil.virtual_memory().percent

# 生成一个0到1之间的15位小数的随机数
def complex_random_decimal():
    global seed
    seed = lcg(seed)  # 线性同余法生成一个基础随机数
    mixed = hash_mix(seed)  # 使用哈希混合
    entropy = entropy_source()  # 结合系统熵源
    complex_random_number = (mixed ^ int(entropy)) % m  # 强制将 entropy 转换为整数
    return complex_random_number / m  # 归一化到0到1之间，并保留15位小数

# 生成在给定范围内的随机整数
def complex_random_int(min_value, max_value):
    # 生成0到1之间的小数
    decimal = complex_random_decimal()
    # 归一化到[min_value, max_value]之间并返回整数
    return min_value + int(decimal * (max_value - min_value))

@app.route('/generate_random_decimal', methods=['GET'])
def generate_random_decimal():
    """生成0到1之间的15位小数随机数"""
    random_decimal = round(complex_random_decimal(), 15)
    return jsonify({"random_decimal": random_decimal})

@app.route('/generate_random_int', methods=['GET'])
def generate_random_int():
    """生成在给定范围内的随机整数"""
    # 获取查询参数 min 和 max
    min_value = request.args.get('min', type=int, default=0)
    max_value = request.args.get('max', type=int, default=100)
    
    # 确保 min 小于 max
    if min_value > max_value:
        return jsonify({"error": "'min' should be less than 'max'"}), 400
    
    random_int = complex_random_int(min_value, max_value)
    return jsonify({"random_integer": random_int})

if __name__ == '__main__':
    app.run(debug=True)

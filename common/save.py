"""
 * @description: TODO 
 * @author ChenDong
 * @date 2024/8/19 下午5:04
 * @version 1.0
"""
def save(filename, content):
    with open(filename, mode='w', encoding='utf-8') as f:
        for i in content:
            f.write(i)
            f.write('\n')
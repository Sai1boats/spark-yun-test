import os
import platform
import subprocess

if __name__ == '__main__':
    fi = {1: '.', 2: 'test_login.py', 3: 'test', 4: 'test_—engine'}
    a = eval(input("选择要执行的用例：\n0.初始化requirements\n1.全部用例\n2.登录界面\n3.后台管理\n4.计算引擎\n->:"))
    current_dir = os.path.dirname(os.path.abspath(__file__))
    system = platform.system()
    if a == 0:
        command = f'pip3 install -r -y {current_dir}/requirements.txt'
        if system == 'Windows':
            command = f'pip3 install -r  {current_dir}/requirements.txt&& playwright install'
        else:
            command = f'pip3 install -r  {current_dir}/requirements.txt; playwright install'
    else:
        # 定义要执行的命令
        if system == 'Windows':
            command = f'cd {current_dir}/Cases && pytest {fi[a]} -s -q'
        else:
            command = f'cd {current_dir}/Cases; pytest {fi[a]} -s -q'

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # 检查命令是否执行成功
    if result.returncode == 0:
        output = result.stdout
        print(output)
    else:
        # 如果命令执行失败，获取错误信息
        error = result.stderr
        print(f'命令执行失败：{error}')

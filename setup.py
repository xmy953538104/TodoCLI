from setuptools import setup, find_packages

setup(
    name='todo_cli',
    version='0.1.0',
    description='一个简单的命令行 TODO 管理器',
    author='MY',
    author_email='xmy953538104@gmail.com',
    packages=find_packages(),
    install_requires=[],  # 无依赖
    entry_points={
        'console_scripts': [
            'todo=todo_cli.main:main',  # 安装后可直接运行 'todo add "任务"'
        ],
    },
    python_requires='>=3.6',
)

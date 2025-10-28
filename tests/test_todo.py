import os
import json
from todo_cli.todo_manager import load_tasks, add_task, delete_task

def test_add_and_load():
    # 清空文件
    if os.path.exists('tasks.json'):
        os.remove('tasks.json')
    add_task("测试任务")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]['description'] == "测试任务"

def test_delete():
    add_task("要删除的任务")
    tasks = load_tasks()
    delete_task(1)
    tasks = load_tasks()
    assert len(tasks) == 0

if __name__ == "__main__":
    test_add_and_load()
    test_delete()
    print("所有测试通过！")

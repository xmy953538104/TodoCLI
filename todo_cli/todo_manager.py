import json
import os
from typing import List

TASKS_FILE = 'tasks.json'

def load_tasks() -> List[dict]:
    """加载任务列表"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks: List[dict]):
    """保存任务列表"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description: str):
    """添加任务"""
    tasks = load_tasks()
    task = {'id': len(tasks) + 1, 'description': description, 'done': False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"任务添加成功: {description}")

def list_tasks():
    """列出任务"""
    tasks = load_tasks()
    if not tasks:
        print("没有任务！")
        return
    for task in tasks:
        status = "✓" if task['done'] else "○"
        print(f"{status} [{task['id']}] {task['description']}")

def delete_task(task_id: int):
    """删除任务"""
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    # 更新 ID
    for i, task in enumerate(tasks, 1):
        task['id'] = i
    save_tasks(tasks)
    print(f"任务 {task_id} 删除成功！")

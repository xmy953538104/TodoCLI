import sys
from todo_manager import add_task, list_tasks, delete_task

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python -m todo_cli [add|list|delete] [描述或ID]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "delete" and len(sys.argv) > 2:
        try:
            delete_task(int(sys.argv[2]))
        except ValueError:
            print("ID 必须是数字！")
    else:
        print("无效命令！用法: add '买牛奶', list, delete 1")

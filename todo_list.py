today_task = []

def append_task(today_task):
    for i in range(1, 6):
        task = input(f'{i}) Enter a task: ')
        today_task.append(task)

def show_task(today_task):
        for t in today_task:
            print(f"- {t}")
    
def remove_task(task_list,del_task):
         if del_task in today_task:
            task_list.remove(del_task)
            print(f'"{del_task}" removed successfully!')
         else:
            print(f'"{del_task}" not found in your list.')


def main():
    print("To-Do List App")
    append_task(today_task)

    while today_task:
        print("\nYour current tasks:")
        show_task(today_task)

        ask_user = input('\nDo you want to delete a task? (Yes/No): ')
        if ask_user.lower() == 'yes':
            del_task = input('Enter the exact task name you want to delete: ')
            remove_task(today_task, del_task)
        elif ask_user.lower() == 'no':
            print("Okay, task list not modified.")
            break
        else:
            print("Invalid input. Please type Yes or No.")

    if not today_task:
            print("\nAll tasks are done! Your to-do list is now empty.")   
        
main()
print("Thanks for using To-Do List App")

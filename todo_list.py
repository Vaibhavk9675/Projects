print("To-Do List App")

today_task = []

for i in range(1, 6):
    task = input(f'{i}) Enter a task: ')
    today_task.append(task)

while today_task:
    print("\nYour current tasks:")
    for t in today_task:
        print(f"- {t}")

    user_input = input('\nDo you want to delete a task? (Yes/No): ')
    
    if user_input.lower() == 'yes':
        del_task = input('Enter the exact task name you want to delete: ')
        if del_task in today_task:
            today_task.remove(del_task)
            print(f'"{del_task}" removed successfully!')
        else:
            print(f'"{del_task}" not found in your list.')
    elif user_input.lower() == 'no':
        print("Okay, task list not modified.")
    else:
        print("Invalid input. Please type Yes or No.")

print("\nAll tasks completed! Your To-Do List is now empty.")
print("Thanks for using To-Do List App")
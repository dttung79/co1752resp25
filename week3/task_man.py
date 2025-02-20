def print_tasks(tasks, times):
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]} - {times[i]} minutes")

def print_long_tasks(tasks, times, length=30):
    count = 0
    for i in range(len(tasks)):
        if times[i] > length:
            count += 1
            print(f"{count}. {tasks[i]} - {times[i]} minutes")
    if count == 0:
        print(f"No tasks are longer than {length} minutes")

def print_longest_task(tasks, times):
    longest_time = times[0]
    longest_task = tasks[0]
    for i in range(1, len(times)):
        if times[i] > longest_time:
            longest_time = times[i]
            longest_task = tasks[i]
    print(f"The longest task is {longest_task} - {longest_time} minutes")

def calculate_total(times):
    total = 0
    for t in times:
        total += t
    hours = total // 60     # integer division
    minutes = total % 60    # remainder
    return hours, minutes

def get_task_time(tasks, times, task_name):
    for i in range(len(tasks)):
        if tasks[i] == task_name:
            return times[i]
    
    return None

def print_menu():
    print("Task Manager")
    print("1. Print tasks")
    print("2. Print tasks long tasks")
    print("3. Print the longest task")
    print("4. Calculate total time")
    print("5. Get task time")
    print("6. Exit")

def main(tasks, times):
    running = True
    while running:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1: print_tasks(tasks, times)
        elif choice == 2: print_long_tasks(tasks, times)
        elif choice == 3: print_longest_task(tasks, times)
        elif choice == 4: 
            hours, minutes = calculate_total(times)
            print(f"Total time is {hours} hours and {minutes} minutes")
        elif choice == 5:
            task_name = input("Enter task name: ")
            task_time = get_task_time(tasks, times, task_name)
            if task_time is not None:
                print(f"{task_name} takes {task_time} minutes")
            else:
                print(f"{task_name} not found")
        elif choice == 6: running = False
        else: print("Invalid choice")

#### Main program ####
if __name__ == "__main__":
    tasks = ["Email", "Meeting", "Coding", "Review", "Lunch", "Report", "Call", "Research", "Presentation", "Planning"]
    times = [30, 45, 60, 20, 50, 40, 35, 25, 55, 65]
    main(tasks, times)
import json
import time

class TaskTracker:

    tasks = {}
    tasksDone = {}
    tasksInProgress = {}
    tasksNotDone = {}

    def __init__(self, tasks, tasksDone, tasksInProgress, tasksNotDone):
        self.tasks = tasks
        self.tasksDone = tasksDone
        self.tasksInProgress = tasksInProgress
        self.tasksNotDone = tasksNotDone
    
    #Adds task to global dictionary and smaller dictionary depending on 'progress' parameter.
    def add_task(tasks, tasksDone, tasksInProgress, tasksNotDone, task, progress):
        if progress.lower() == 'notdone':
            tasks.update(task)
            tasksNotDone.update(task)
        elif progress.lower() == 'inprogress':
            tasks.update(task)
            tasksInProgress.update(task)
        elif progress.lower() == 'done':
            tasks.update(task)
            tasksDone.update(task)
        else:
            print("Invalid Entry")
    
    #Attemps to remove task from 3 smaller dictionaries; Upon success, adds to dictionary that 
    #coorelates with 'progress' value given.
    def update_task(tasks, tasksDone, tasksInProgress, tasksNotDone, task, progress):
        if progress.lower() == 'done':
            try:
                pop = tasksDone.pop([task][0])
                tasksDone.update({task : pop})
                print("Task already marked as: Done")
                print('Would you like to change task ID? (Y/N)')
                if input().lower() == 'y':
                    print('Provide a new ID for task \'' + task + '\'')
                    newid = input()
                    tasksDone[task]['id'] = newid
                    tasks[task]['id'] = newid
                print('Would you like to change task description? (Y/N)')
                if input().lower() == 'y':
                    print('Provide a new description for task \'' + task + '\'')
                    newdesc = input()
                    tasksDone[task]['description'] = newdesc
                    tasks[task]['description'] = newdesc
            except KeyError:
                try:
                    pop = tasksInProgress.pop([task][0])
                    tasksDone.update({task : pop})
                    tasksDone[task]['last updated'] = time.ctime(time.time())
                    tasks[task]['last updated'] = time.ctime(time.time())
                    tasksDone[task]['status'] = 'done'
                    tasks[task]['status'] = 'done'
                    print('Would you like to change task ID? (Y/N)')
                    if input().lower() == 'y':
                        print('Provide a new ID for task \'' + task + '\'')
                        newid = input()
                        tasksDone[task]['id'] = newid
                        tasks[task]['id'] = newid
                    print('Would you like to change task description? (Y/N)')
                    if input().lower() == 'y':
                        print('Provide a new description for task \'' + task + '\'')
                        newdesc = input()
                        tasksDone[task]['description'] = newdesc
                        tasks[task]['description'] = newdesc
                except KeyError:
                    try:
                        pop = tasksNotDone.pop([task][0])
                        tasksDone.update({task : pop})
                        tasksDone[task]['last updated'] = time.ctime(time.time())
                        tasks[task]['last updated'] = time.ctime(time.time())
                        tasksDone[task]['status'] = 'done'
                        tasks[task]['status'] = 'done'
                        print('Would you like to change task ID? (Y/N)')
                        if input().lower() == 'y':
                            print('Provide a new ID for task \'' + task + '\'')
                            newid = input()
                            tasksDone[task]['id'] = newid
                            tasks[task]['id'] = newid
                        print('Would you like to change task description? (Y/N)')
                        if input().lower() == 'y':
                            print('Provide a new description for task \'' + task + '\'')
                            newdesc = input()
                            tasksDone[task]['description'] = newdesc
                            tasks[task]['description'] = newdesc
                    except KeyError:
                        print("Task does not exist.")

        elif progress.lower() == 'inprogress':
            try:
                pop = tasksDone.pop([task][0])
                tasksInProgress.update({task : pop})
                tasksInProgress[task]['last updated'] = time.ctime(time.time())
                tasks[task]['last updated'] = time.ctime(time.time())
                tasksInProgress[task]['status'] = 'inprogress'
                tasks[task]['status'] = 'inprogress'
                print('Would you like to change task ID? (Y/N)')
                if input().lower() == 'y':
                    print('Provide a new ID for task \'' + task + '\'')
                    newid = input()
                    tasksInProgress[task]['id'] = newid
                    tasks[task]['id'] = newid
                print('Would you like to change task description? (Y/N)')
                if input().lower() == 'y':
                    print('Provide a new description for task \'' + task + '\'')
                    newdesc = input()
                    tasksInProgress[task]['description'] = newdesc
                    tasks[task]['description'] = newdesc
            except KeyError:
                try:
                    pop = tasksInProgress.pop([task][0])
                    tasksInProgress.update({task : pop})
                    print('Task already marked as: InProgress')
                    print('Would you like to change task ID? (Y/N)')
                    if input().lower() == 'y':
                        print('Provide a new ID for task \'' + task + '\'')
                        newid = input()
                        tasksInProgress[task]['id'] = newid
                        tasks[task]['id'] = newid
                    print('Would you like to change task description? (Y/N)')
                    if input().lower() == 'y':
                        print('Provide a new description for task \'' + task + '\'')
                        newdesc = input()
                        tasksInProgress[task]['description'] = newdesc
                        tasks[task]['description'] = newdesc
                except KeyError:
                    try:
                        pop = tasksNotDone.pop([task][0])
                        tasksInProgress.update({task : pop})
                        tasksInProgress[task]['last updated'] = time.ctime(time.time())
                        tasks[task]['last updated'] = time.ctime(time.time())
                        tasksInProgress[task]['status'] = 'inprogress'
                        tasks[task]['status'] = 'inprogress'
                        print('Would you like to change task ID? (Y/N)')
                        if input().lower() == 'y':
                            print('Provide a new ID for task \'' + task + '\'')
                            newid = input()
                            tasksInProgress[task]['id'] = newid
                            tasks[task]['id'] = newid
                        print('Would you like to change task description? (Y/N)')
                        if input().lower() == 'y':
                            print('Provide a new description for task \'' + task + '\'')
                            newdesc = input()
                            tasksInProgress[task]['description'] = newdesc
                            tasks[task]['description'] = newdesc
                    except KeyError:
                        print("Task does not exist.")

        elif progress.lower() == 'notdone':
            try:
                pop = tasksDone.pop([task][0])
                tasksNotDone.update({task : pop})
                tasksNotDone[task]['last updated'] = time.ctime(time.time())
                tasks[task]['last updated'] = time.ctime(time.time())
                tasksNotDone[task]['status'] = 'notdone'
                tasks[task]['status'] = 'notdone'
                print('Would you like to change task ID? (Y/N)')
                if input().lower() == 'y':
                    print('Provide a new ID for task \'' + task + '\'')
                    newid = input()
                    tasksNotDone[task]['id'] = newid
                    tasks[task]['id'] = newid
                print('Would you like to change task description? (Y/N)')
                if input().lower() == 'y':
                    print('Provide a new description for task \'' + task + '\'')
                    newdesc = input()
                    tasksNotDone[task]['description'] = newdesc
                    tasks[task]['description'] = newdesc
            except KeyError:
                try:
                    pop = tasksInProgress.pop([task][0])
                    tasksNotDone.update({task : pop})
                    tasksNotDone[task]['last updated'] = time.ctime(time.time())
                    tasks[task]['last updated'] = time.ctime(time.time())
                    tasksNotDone[task]['status'] = 'notdone'
                    tasks[task]['status'] = 'notdone'
                    print('Would you like to change task ID? (Y/N)')
                    if input().lower() == 'y':
                        print('Provide a new ID for task \'' + task + '\'')
                        newid = input()
                        tasksNotDone[task]['id'] = newid
                        tasks[task]['id'] = newid
                    print('Would you like to change task description? (Y/N)')
                    if input().lower() == 'y':
                        print('Provide a new description for task \'' + task + '\'')
                        newdesc = input()
                        tasksNotDone[task]['description'] = newdesc
                        tasks[task]['description'] = newdesc
                except KeyError:
                    try:
                        pop = tasksNotDone.pop([task][0])
                        tasksNotDone.update({task : pop})
                        print('Task is already marked as: Not Done')
                        print('Would you like to change task ID? (Y/N)')
                        if input().lower() == 'y':
                            print('Provide a new ID for task \'' + task + '\'')
                            newid = input()
                            tasksNotDone[task]['id'] = newid
                            tasks[task]['id'] = newid
                        print('Would you like to change task description? (Y/N)')
                        if input().lower() == 'y':
                            print('Provide a new description for task \'' + task + '\'')
                            newdesc = input()
                            tasksNotDone[task]['description'] = newdesc
                            tasks[task]['description'] = newdesc
                    except KeyError:
                        print("Task does not exist.")

        else:
            print('Invalid Progress Entry: ' + progress)

    #Attempts to remove a given value from all 3 shorter dictionaries
    #Upon success, removes from global dictionary as well.
    def delete_task(tasks, tasksDone, tasksInProgress, tasksNotDone, task):
        try:
            tasksDone.remove(task)
            tasks.remove(task)
        except ValueError:
            try:
                tasksInProgress.remove(task)
                tasks.remove(task)
            except ValueError:
                try:
                    tasksNotDone.remove(task)
                    tasks.remove(task)
                except ValueError:
                    print('Could not locate task: ' + task)

    #Simple iterator to list all tasks in a given dictionary
    def list_tasks(tasks):
        for i in tasks:
            print(i)

#Functions to shorten arguments when calling class functions
def add_task(task, progress):
    TaskTracker.add_task(TaskTracker.tasks, TaskTracker.tasksDone, TaskTracker.tasksInProgress, TaskTracker.tasksNotDone, task, progress)

def update_task(task, progress):
    TaskTracker.update_task(TaskTracker.tasks, TaskTracker.tasksDone, TaskTracker.tasksInProgress, TaskTracker.tasksNotDone, task, progress)

def delete_task(task):
    TaskTracker.delete_task(TaskTracker.tasks, TaskTracker.tasksDone, TaskTracker.tasksInProgress, TaskTracker.tasksNotDone, task)

def list_tasks():
    TaskTracker.list_tasks(TaskTracker.tasks)

def list_tasks_done():
    TaskTracker.list_tasks(TaskTracker.tasksDone)

def list_tasks_in_progress():
    TaskTracker.list_tasks(TaskTracker.tasksInProgress)

def list_tasks_not_done():
    TaskTracker.list_tasks(TaskTracker.tasksNotDone)

try:
    with open('tasks.json', 'r') as file:
        pass
except FileNotFoundError:
    data = {'tasks' : TaskTracker.tasks, 'tasksDone' : TaskTracker.tasksDone, 'tasksInProgress' : TaskTracker.tasksInProgress, 'tasksNotDone' : TaskTracker.tasksNotDone}
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent = 4)

run = True
print('Welcome to your personal task tracking system!')
print('Type \'Help\' for commands')

while run:
    with open('tasks.json', 'r') as file:
        data = json.load(file)
        TaskTracker.tasks = data['tasks']
        TaskTracker.tasksDone = data['tasksDone']
        TaskTracker.tasksInProgress = data['tasksInProgress']
        TaskTracker.tasksNotDone = data['tasksNotDone']

    cmd = input()
    
    #Add Task implementation: Checks for first two words in input on whether to call. Upon calling, checks last word in input for assignment.
    #If assignment not given or assignment not recognized, assigns default assignment: NotDone
    if cmd.split()[0].lower() == 'add' and cmd.split()[1].lower() == 'task':
        tsk = ''
        prg = cmd.split()[len(cmd.split()) - 1]
        if prg.lower() != 'done' and prg.lower() != 'inprogress' and prg.lower() != 'notdone':
            prg = 'notdone'
        for i in range(2, len(cmd.split())):
            tsk += cmd.split()[i] + ' '
        tsk = tsk[:-1]
        if tsk.split()[len(tsk.split()) - 1] == 'done' or tsk.split()[len(tsk.split()) - 1] == 'inprogress' or tsk.split()[len(tsk.split()) - 1] == 'notdone':
            tsk = tsk.split()[:-1]
            tsk = ' '.join(tsk)
        print('Assign a task ID: ')
        id = input()
        print('Describe the task: ')
        desc = input()
        status = prg
        createdAt = time.ctime(time.time())
        updatedAt = time.ctime(time.time())
        tskdic = {tsk : {'id' : id, 'description' : desc, 'status' : status, 'time created' : createdAt, 'last updated' : updatedAt}}
        add_task(tskdic, prg)

    #Delete Task implementation: Checks first two words in input on whether to call.
    #Upon calling, retrieves remaining words to define task to delete.
    if cmd.split()[0].lower() == 'delete' and cmd.split()[1].lower() == 'task':
        tsk = ''
        for i in range(2, len(cmd.split())):
            tsk += cmd.split()[i] + ' '
        tsk = tsk[:-1]
        delete_task(tsk)

    #Update Task Implementation: Checks first two words in input on whether to call.
    #Upon calling, retrieves last word to determine where the task sandwiched goes.
    if cmd.split()[0].lower() == 'update' and cmd.split()[1].lower() == 'task':
        prg = cmd.split()[len(cmd.split()) - 1]
        tsk = ''
        for i in range(2, len(cmd.split()) - 1):
            tsk += cmd.split()[i] + ' '
        tsk = tsk[:-1]
        update_task(tsk, prg)

    #List Tasks implementation: Checks for first two words in input on whether to call. Returns global dictionary.
    if cmd.split()[0].lower() == 'list' and cmd.split()[1].lower() == 'tasks':
        list_tasks()

    #List Tasks Done implementation: Checks for first three words in input on whether to call. Returns tasksDone dictionary.
    if cmd.split()[0].lower() == 'list' and cmd.split()[1].lower() == 'tasksdone':
        list_tasks_done()

    #List Tasks In Progress implementation: Checks for first four words in input on whether to call. Returns tasksInProgress dictionary.
    if cmd.split()[0].lower() == 'list' and cmd.split()[1].lower() == 'tasksinprogress':
        list_tasks_in_progress()

    #List Tasks Not Done implementation: Checks for first four words in input on whether to call. Returns tasksNotDone dictionary.
    if cmd.split()[0].lower() == 'list' and cmd.split()[1].lower() == 'tasksnotdone':
        list_tasks_not_done()

    #In-console command repository
    if cmd.lower() == 'help':
        print('Commands:')
        print('Add Task: \'Add Task\' + \'Your Task Here\' + progress (NotDone, InProgress, Done) : adds a task to the dictionary and assigns a progress status. (default: NotDone)')
        print('Update Task: \'Update Task\' + \'Your Task Here\' + new progress (NotDone, InProgress, Done) : updates status of task')
        print('Delete Task: \'Delete Task\' + \'Your Task Here\' : deletes task from all dictionaries.')
        print('List Tasks: \'List Tasks\' : lists all tasks')
        print('List Tasks Done: \'List TasksDone\' : lists all tasks marked as \'Done\'')
        print('List Tasks In Progress: \'List TasksInProgress\' : lists all tasks marked as \'InProgress\'')
        print('List Tasks Not Done: \'List TasksNotDone\' : lists all tasks marked as \'NotDone\'')

    data = {'tasks' : TaskTracker.tasks, 'tasksDone' : TaskTracker.tasksDone, 'tasksInProgress' : TaskTracker.tasksInProgress, 'tasksNotDone' : TaskTracker.tasksNotDone}

    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent = 4)

    #Program run time terminator
    if cmd.lower() == 'quit' or cmd.lower() == 'exit':
        run = False

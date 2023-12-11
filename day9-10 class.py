
def todos():
    print('==== TODO#1/4 ====')
    # TODO#1/4-Write a Task class so that when running the test code below, the
    #       following output will be produced:
    # Task: Save the world
    #         Difficulty: 7.3
    #         Done: False
    # Task: Learn Python
    #         Difficulty: 8.7
    #         Done: False
    class Task:
        def __init__(self, name, difficulty):
            self.name = name
            self.difficulty = difficulty
            self.done = False
        def set_done(self, done):
            self.done = done
        def get_name(self):
            return self.name
        def __str__(self): 
            return f'Task: {self.name}\n\tDifficulty: {self.difficulty}\n\tDone:{self.done}'

    task1 = Task(name='Save the world', difficulty='7.3')
    task2 = Task(name='Learn Python', difficulty='8.7')
    print(task1)
    print(task2)

    print('\n==== TODO#2/4 ====')
    # TODO#2/4-Write a SuperHero class so that when running the test code below, the 
    #       following output will be produced:
    # SuperHero: Spiderman
    #         Strength: 8.7
    #         Skills: ['time travel', 'fly', 'joking', 'eat pizza']

    class SuperHero:
        def __init__(self, name, strength, skills):
            self.name, self.strength, self.skills = name, strength, skills
            self.tasks = []
        def assign_task(self,task):
            if task not in self.tasks:
                self.tasks.append(task.name)
        def complete_task(self, task):
            if task.get_name() in self.tasks:
                task.set_done(True)
        def __str__(self): 
            return f'SuperHero: {self.name}\n\tStrength: {self.strength}\n\tSkills:{self.skills}\n\tTasks:{self.tasks}'

    hero1 = SuperHero(name='Spiderman', strength='8.7', 
        skills=['time travel', 'fly', 'joking', 'eat pizza'])
    print(hero1)

    print('\n==== TODO#3/4 ====')
    # TODO#3/4-Add code to SuperHero class so that when running the test code
    #       below, the following output will be produced:
    # SuperHero: Spiderman
    #         Strength: 8.7
    #         Skills: ['time travel', 'fly', 'joking', 'eat pizza']
    #         Tasks: ['Save the world', 'Learn Python']
        

    hero1.assign_task(task1)
    hero1.assign_task(task2)
    print(hero1)

    print('\n==== TODO#4/4 ====')
    # TODO#4/4-Add more code to the two classes so that when running the test
    #       code below, the following output will be produced:
    # SuperHero: Spiderman
    #         Strength: 8.7
    #         Skills: ['time travel', 'fly', 'joking', 'eat pizza']
    #         Tasks: ['Save the world', 'Learn Python']
    # Task:   Save the world
    #         Difficulty: 7.3
    #         Done: True
    hero1.complete_task(task1)
    print(hero1)
    print(task1)

todos()
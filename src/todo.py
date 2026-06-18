#Обьявление класса с задачами
class TodoList:
    #Инициализация конструктора
    def __init__(self):
        self.tasks = []
    #Метод добавление новой задачи
    def add_task(self, task):
        self.tasks.append(task)
    #Метод удаления новой задачи
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return
        
        raise ValueError("Task not found")
    #Метод возвращения кол-ва задача
    def count_tasks(self):
        return len(self.tasks)
    
    #Метод возвращение обьекта класса(задачи)
    def get_task(self):
        return self.tasks
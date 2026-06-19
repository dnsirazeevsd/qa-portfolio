class Counter:
    #Инициализация контруктора
    def __init__(self):
        self.value_ = 0

    #Увелечие счетчика
    def increment(self, value):
        self.value_ += value
        return self.value_
    
    #Уменьшение счетчика
    def decrement(self, value):
        if value > self.value_:
            raise ValueError("Negative value not allowed")

        self.value_ -= value
        return self.value_
    
    #Сбрасывания счетчика = 0
    def reset(self):
        self.value_ = 0
    
    #Возращает текущее значения счетчика
    def get_value(self):
        return self.value_
    
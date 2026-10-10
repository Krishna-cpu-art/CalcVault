class Calc:
    def __init__(self):
        pass

    def __str__(self):
        return f"{self._add}"
    
    def add(self, numbers):
        num = list(numbers.split("+"))
        total = 0 
        for i in num:
            i = int(i)
            total+=i
        return total
numbers = input("Numbers: ")
add = Calc()
print(add.add(numbers))
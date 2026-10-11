# CalcVault is a calculator basic cli tool
class Calc:
    def __init__(self):
        self._total = 0
       
    def __str__(self):
        return f"{self._total}"
    
    def add(self, numbers):
        num = list(numbers.split("+"))
        if numbers.startswith("+"):
            for i in num[1:]:
                  
                numbers = int(numbers.replace("+",""))
                self._total+=numbers
                return self._total
                
                
        
        for i in num:
            i = int(i)
            self._total+=i
        
        return self._total 
    def sub(self, numbers):
        num = (numbers.split("-"))
        if numbers.startswith("-"):
            for i in num[1:]:
                i = int(i)
                self._total-=i
            return self._total
        
        for i in num[1:]:
            i = int(i)
            first = int(num[0])
            self._total=self._total + first -i
        return self._total 
    def multi(self, numbers):
        num = numbers.split("*")
        if numbers.startswith("*"):
            for i in num[1:]:
                i = int(i)
                self._total*=i
            return self._total
        for i in num[1:]:
            i = int(i)
            self._total=int(num[0])*i
        return self._total 
    def div(self, numbers):
        
            num = numbers.split("/")
            if numbers.startswith("/"):
                
                for i in num[1:]:
                        i = int(i)
                        self._total/=i
                return self._total
            for  i in num[1:]:
                            
                i = int(i)
                self._total = int(num[0])/i
            return self._total
        
            

add = Calc()
while True:
    try:    
        numbers = (input("Numbers: ").lower())
        if numbers == "q":
                break
        if "+" in numbers:
            num = add.add(numbers)
            print(num)
        elif "-" in numbers:
            num = add.sub(numbers)
            print(num)
        elif "*" in numbers:
            num = add.multi(numbers)
            print(num)
        try:
            if "/" in numbers:
                num = add.div(numbers)
                print(num)
        except ZeroDivisionError:
            print(f"""Denominator in division can't be 0 \n Total={add}""")
    except ValueError:
        print("Enter only Integers")
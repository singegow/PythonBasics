try:
    age = int(input("Age : "))
    salary = 20000
    income = salary / age
    print(income)
    # any code except exit 0 means crash
    print(age)
except ZeroDivisionError:
    print("Ae cant be 0")
except ValueError:
    print("Invalide value")


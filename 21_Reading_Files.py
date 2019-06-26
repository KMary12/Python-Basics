employees_var = open("employees.txt", "r")
print(employees_var.readable())
print(employees_var.readline())
print(employees_var.read())
employees_var.close()


#
employees_var = open("employees.txt", "r")

for for_var in employees_var.readlines():
    print(for_var)
employees_var.close()

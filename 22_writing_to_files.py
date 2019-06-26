employees_var = open("employees.txt", "a")

employees_var.write("Lukasz - Tower Head")
employees_var.close()
#print(employees_var)

employees_var = open("employees.txt", "a")
employees_var.write("\nKelly -hr")
#employees_var.close()

employees_var= open("employees1.txt", "w")
employees_var.write("\nKelly - HR")
employees_var.close()


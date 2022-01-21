def create_employee(name, salary, position):
    obj = {"name": name, "salary": salary, "position": position, "get_employee": 0}

    def get_salary():
        print(obj.get("salary"))

    def update_salary(new_salary):
        obj.update({"salary": new_salary})

    def get_employee():
        return "{0} gets {1} and is working as a {2}".format(obj.get("name"), obj.get("salary"), obj.get("position"))

    obj.update({"get_employee": get_employee, "get_salary": get_salary, "update_salary": update_salary})
    return obj


# create_employee("Tal", 100, "Fullstack developer")
emp1 = create_employee("Tal", 100, "Fullstack developer")
emp1.get("update_salary")(2000)
emp1.get("get_salary")()
res = emp1.get("get_employee")()
print(res)

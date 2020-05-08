#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("Loki", 1)
cat2 = Cat("Shadow", 1)
cat3 = Cat("Willow", 2)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(*args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)}")






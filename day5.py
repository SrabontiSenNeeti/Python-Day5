#ClassWork Day5
user_name = input("Enter your name: ")
user_pass = input("Enter your Password: ")
star = "*" * len(user_pass)
print(f"Hi {user_name}. Your password {star} is {len(user_pass)} Charecter long")

#step value output
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
print(my_cart[::-2])
print(my_cart[::-1])

#replace by index value
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
my_cart[0] = 'Berry'
print(my_cart)

#lenth of my cart
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
print(len(my_cart))

#using copy function
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
new_cart = my_cart.copy()
print(new_cart)

#using append function
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
my_cart.append(1230)
print(my_cart)


#JUST LIKE APPEND ADDED IN LAST VALUE
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
print(my_cart + [3])


#using extend function
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
my_cart.extend(["A", "B", "C"])
print(my_cart)

#using insert fumction
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
my_cart.insert(3, 'WaterMelon')
print(my_cart)

#using index function
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
print(my_cart.index('Milk'))

#Using Pop function
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
my_cart.pop(5)
print(my_cart)


#Using Remove Function
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
my_cart.remove('Milk')
print(my_cart)

#using Clear Function
my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
my_cart.clear()
print(my_cart)

#Class Work
my_list = [1, 2, 3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)


#class work
basket = ['Bananas', 'Apples', 'Orange', 'Blubarries',"Apples"]
basket.count('Apples')
print(basket)
basket.remove('Bananas')
print(basket)
basket.append('Kiwi')
print(basket)
basket[0] = 'Apples'
print(basket)
basket.clear()
print(basket)


#sorted
my_list = [1, 4, 5, 6, 2, 7, 3,11,50,30,12,60,100]
my_list.sort()
print(my_list)

#REverse
my_list = [1, 4, 5, 6, 2, 7, 3,11,50,30,12,60,100]
my_list.reverse()
print(my_list)

#Sort and reverse
my_list = [1, 4, 5, 6, 2, 7, 3,11,50,30,12,60,100]
my_list.sort(reverse=True)
print(my_list)

#Using in function
my_list = [1, 4, 5, 6, 2, 7, 3,11,50,30,12,60,100]
print(4 in my_list)


#Using min function
my_list = [1, 4, 5, 6, 2, 7, 3,11,50,30,12,60,100]
print(min(my_list))

list =["neeti","Me","you"]
print(min(list))

#Using Max function
my_list = [1, 4, 5, 6, 2, 7, 3,11,50,30,12,60,100]
print(max(my_list))

#using Sum Function
my_list = [1, 4, 5, 6, 2, 7, 3,11,50,30,12,60,100]
print(sum(my_list))

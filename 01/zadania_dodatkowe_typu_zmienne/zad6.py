# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

l_height = float(input("Please provide the lift's height (m): "))
l_width = float(input("Please provide the lift's width (m): "))
l_depth = float(input("Please provide the lift's depth (m): "))

l_capacity = l_height * l_width * l_depth

print("The lift capacity is: ", l_capacity, "m3")

f_height = float(input("Please provide the fridge's height (m): "))
f_width = float(input("Please provide the fridge's width (m): "))
f_depth = float(input("Please provide the fridge's depth (m): "))

f_capacity = f_height * f_width * f_depth

print("The fridge capacity is: ", f_capacity, "m3")

space = l_capacity - f_capacity
print ("You're left with: ", space, "m3 to use.")


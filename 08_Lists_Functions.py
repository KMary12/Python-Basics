lucky_numbers = [ 4, 8, 9, 18, 42, 56]
friends = ["Kevin", "jack", "Jane", "Oscar", "Toby"]
print(friends)
print(lucky_numbers)
friends.extend(lucky_numbers)
print(friends)
lucky_numbers = [ 4, 8, 9, 18, 42, 56]
friends = ["Kevin", "jack", "Jane", "Oscar", "Toby"]
friends.append("Olek")
print(friends)
results= int(lucky_numbers[0])+int(lucky_numbers[3])
#results= lucky_numbers[0])+friends[3]
print(results)
friends.insert(1, "Aleksander")
print(friends)
friends.remove("Olek")
print(friends)
print(len(friends))
friends.clear()
print(friends)
lucky_numbers = [ 4, 8, 9, 18, 42, 56]
friends = ["Kevin", "jack", "Jane", "Oscar", "Toby"]
results2 = friends.pop()
print(results2)
print(friends.index("Jane"))
print(friends.count("Jim"))
friends.sort()
lucky_numbers.sort()
print(lucky_numbers)
friends.reverse()
print(friends)
friends2= friends.copy()
print(friends2)
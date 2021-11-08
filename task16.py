set1 = {"green", "blue"}
set2 = {"blue", "yellow"}

set3 = set1.intersection(set2)
set4 = set1.difference(set2)
set5 = set1.symmetric_difference(set2)
print(f'გაერთიანება {set1.union(set2)}')
print(f'თანაკვეთა {set3}')
print(f'სხვაობა A\B {set4}')
print(f'სიმეტრიული სხვაობა {set5}')

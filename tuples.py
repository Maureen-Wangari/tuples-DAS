# creating a tuple with state names

states = ("Chicago", "Michigan", "NewYork", "SanFransisco")

# creating a list out of a defined tupple
moreStates = list(states)


#Tuple methods
print(states)
print(moreStates)
print(type(moreStates))
print(states.count("Chicago"))
print(states.index("NewYork"))
print(states*2)
print(list(states))
print(type(states))
print(states[1:])
print(states[0:2])
print(states[-1])
print(moreStates.pop())
moreStates.append("Hollywood")
print(moreStates)
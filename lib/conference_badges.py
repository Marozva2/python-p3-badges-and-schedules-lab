def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

#def batch_badge_creator(names):
#    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    assignments = []
    for index, name in enumerate(names):
        assignments.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
    return assignments

#def assign_rooms(names):
#    return [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(names)]

def printer(names):
    for name in names:
        print(badge_maker(name))
    for assignment in assign_rooms(names):
        print(assignment)

#def printer(names):
#    [print(badge_maker(name)) for name in names]
#    [print(assignment) for assignment in assign_rooms(names)]


from collections import deque

def find_leader(factions):
    students = deque(factions)
    
    # This loop continues until only one faction is left
    while len(set(students)) > 1:  # set(students) will give us unique factions left
        current_student = students.popleft()
        
        # Find and remove the next student from the opposite faction
        for i in range(len(students)):
            if students[i] != current_student:
                students.remove(students[i])
                break
        
        # Rotate the deque to simulate the next student's turn
        students.append(current_student)
    
    # Determine which faction the last remaining student belongs to
    leader_faction = students[0]
    if leader_faction == 'S':
        return "SAKAYANAGI"
    else:
        return "KATSURAGI"

# Example usage
print(find_leader("KSKS"))  # Output: KATSURAGI
print(find_leader("SSKKK"))  # Output: SAKAYANAGI

# *
# *
# *
# + 6
# - 9
# + 6
# + 3
# + 6
# - 0

# !
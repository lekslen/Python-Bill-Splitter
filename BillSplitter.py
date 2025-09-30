import random

print("Enter the number of friends joining (including you):")
friends = int(input())

if friends <=0:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")
participants = {}
for f in range(friends):
    participants.update({input(): 0})

print("Enter the total bill value:")
total = float(input())
split_nr = round(total/len(participants), 2)

for p in participants:
    participants[p] = split_nr

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
if_lucky = input().lower()
lucky_name = ''
if if_lucky == "yes":
    lucky_name = random.choice(list(participants.keys()))
    print(f"{lucky_name} is the lucky one!")
    split_nr = round(total/(len(participants)-1), 2)
    for p in participants:
        participants[p] = split_nr
    participants[lucky_name] = 0
else:
    print("No one is going to be lucky")
    
print(participants)

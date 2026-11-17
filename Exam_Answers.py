'''
#Cricket Scorecard
runs = list(map(int,input().split()))
total_runs,boundaries,dot_balls,invalid = 0,0,0,0
for run in runs:
    if run in (0,1,2,3,4,6):
        total_runs += run
    if run == 4 or run == 6:
        boundaries += 1
    if run == 0:
        dot_balls += 1
    if run not in (0,1,2,3,4,6):
        invalid += 1
print(f'Total Runs: {total_runs}')
print(f'Boundaries: {boundaries}')
print(f'Dot Balls: {dot_balls}')
print(f'Invalid Entries: {invalid}')

#Email Report
emails = list(map(str,input().split()))
codegnan_emails = 0
for email in emails:
    if 'codegnan.com' in email:
        codegnan_emails += 1
    t = email.split('@')
    print(t[1])
print(f'Codegnan Emails: {codegnan_emails}')

#ATM PIN
attempts = list(map(str,input().split()))
count,wrong,grant = 0,0,False
string = "1234"
for attempt in attempts:
    count += 1
    if attempt == string:
        grant = True
        break
    else:
        wrong += 1
        if wrong == 3:
            break
if grant:
    print("Access Granted")
else:
    print("Card Blocked")
print(f'Attempts Used: {count}')

#Guessing Game
guesses = list(map(int,input().split()))
guess_used = 0
for guess in guesses:
    if guess < 25 and guess > 0:
        guess_used += 1
        print("Too Low")
    if guess == 0:
        print("Game Cancelled")
        break
    if guess == 25:
        guess_used += 1
        print("Correct Guess")
        break
    if guess > 25:
        guess_used += 1
        print("Too High")
print(f'Guesses Used: {guess_used}')

#Food Counter
orders = list(map(str,input().split(',')))
item_ordered,invalid_order,total= 0,0,0
burger,pizza,fries = 80,150,60
for order in orders:
    order = order.strip()
    if order == 'Burger':
        item_ordered += 1
        total += burger
    elif order == 'Pizza':
        item_ordered += 1
        total += pizza
    elif order == 'Fries':
        item_ordered += 1
        total += fries
    elif order == 'EXIT':
        break
    else:
        invalid_order += 1
print(f'Items Ordered: {item_ordered}')
print(f'Total Bill: {total}')
print(f'Invalid Orders: {invalid_order}')
'''
#Quiz Game
answers = list(map(str,input().split(',')))
lives,score,ans = 3,0,0
correct = "Python"
for answer in answers:
    answer = answer.strip()
    ans += 1
    if answer == correct:
        score += 10
    else:
        lives -= 1
    if score == 30:
        print("You Win")
        break
    if lives == 0:
        print("Game Over")
        break
print(f'Score: {score}')
print(f'Lives Remaining: {lives}')
print(f'Answers Used: {ans}')









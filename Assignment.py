
#Instagram Verification Status
account = bool(input("Eligible Account: "))
subscription = bool(input("Meta Verified Subscription: "))
if account and subscription:
    print("Verified Badge Granted")
else:
    print("None")

#Username and Password Login
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "admin123":
    print("Login Successful")
else:
    print("Invalid Credentials")

#Product Search
available_products = ['Laptop','Mobile','Watch']
search_product = input("Search Product:\n")
if search_product in available_products:
    print("Product Found")
else:
    print("Product Not Found")

#Greeting Based on Time
current_hour = int(input("Enter the current hour:"))
if current_hour>=5 and current_hour<=11:
    print("Good Morning")
elif current_hour>=12 and current_hour<=16:
    print("Good Afternoon")
elif current_hour>=17 and current_hour<=20:
    print("Good Evening")
else:
    print("Good Night")

#Hostinger Hosting Plan
customer_budget = int(input("Enter the customer's budget:"))    
if customer_budget > 10000:
    print("Cloud Hosting")
elif customer_budget > 5000:
    print("Business Hosting")
elif customer_budget > 2000:
    print("Premium Hosting")
else:
    print("Single Hosting")

#Instagram Story Visibility
follow_account = bool(input("Follows Account: "))
close_friend = bool(input("Close Friend: "))
if follow_account:
    if close_friend:
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account First")

#BGMI Tournament Entry
registered = bool(input("Registered: "))
fee_paid = bool(input("Fee Paid: "))
if registered:
    if fee_paid:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")

#Google Drive File Access
file_link_active = bool(input("Link Active: "))
grant_permission = bool(input("Permission Granted: "))
if file_link_active:
    if grant_permission:
        print("File Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")


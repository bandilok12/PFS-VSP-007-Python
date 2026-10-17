#Python String Practice Questions
'''
#1)Basic String Manipulation
#1. Student Name Formatter

name = "sAkEtH kAlLePu"
print(name.title())     #Output:Saketh Kallepu

#2. Customer Email Cleanup

email = " Saketh.KALLEPU@GMAIL.COM "
print(email.strip().lower())    #Output:saketh.kallepu@gmail.com

#3. Product Code Replacement

product_code = "OLD-101-OLD-202"
print(product_code.replace('OLD','NEW'))    #Output:NEW-101-NEW-202

#4. Username Generator

first_name = "SAKETH";year = 2027
print(f'{first_name.lower()}_{year}')   #Output:saketh_2027

#5. Sentence Character Count

sentence = "Python makes coding easy"
print(len(sentence))    #Output:24

#2)Indexing and Slicing
#6. Employee ID Extraction

employee_id = "EMP582741"
print(employee_id[3:])  #Output:582741

#7. Mask a Bank Account Number

account_number = "123456789012"
print('*'*(len(account_number)-4)+ account_number[-4:])     #Output:********9012

#8. Alternating Character Extraction

text = "CODEGNANPYTHON"
print(text[::2])    #Output:CDGAPTO

#9. Reverse a Product Serial Number

serial_number = "PYTHON123"
print(serial_number[::-1])  #Output:321NOHTYP

#10. Extract a File Extension

filename = "student_report.pdf"
print(filename[-3:])    #Output:pdf

#3)Searching, Splitting, and Joining
#11. Search for a Course Name

description = "Python is easy. I love PYTHON. Learn python today."
print(description.lower().count("python"))  #Output:3

#12. Convert a Sentence into Words

sentence = "Learn Python Full Stack Development"
print(sentence.split()) #Output:['Learn', 'Python', 'Full', 'Stack', 'Development']

#13. Generate a Formatted Address

house = "12-4";street = "MG Road";city = "Vijayawada";state = "Andhra Pradesh"
print(house,street,city,state,sep=', ')   #Output:12-4, MG Road, Vijayawada, Andhra Pradesh

#14. Count Words in a Message

message = "Your application has been successfully submitted"
print(len(message.split()))     #Output:6
'''
#15. Validate a Coupon Code

coupon_code = "CODEGNAN"
print(coupon_code.isalpha())    #Output:True
# Additional test
coupon_code = "CODEGNAN123"
print(coupon_code.isalpha())    #Output:False






'''
Task: Create your Student Profile with fields as ID number
#Email id,Mobile Number,Parent WhatsApp number,subjects,
#batch no,daily exam marks,weekly exam marks,batch rank,
#githuburl,linkedinid
#Make sure you apply methods also to it(Lists/Sets)
'''
student = {"student_id": "CGVI0233",
            "full_name": "Lokesh Bandi",
            "email_id": "bandisailokesh@gmail.com",
            "mobile_number": "9876543210",
            "parent_whatsapp_number": "9123456780",
            "institute": "Codegnan",
            "course": "Python Full Stack Development",
            "batch_number": "PFS-VSP-007",
            "subjects": {"Python", "MYSQL", "Aptitude", "Soft Skills"},
            "daily_exam_marks": [8, 9, 7, 10, 8],
            "weekly_exam_marks": [82, 88, 91, 85],
            "batch_rank": 5,
            "attendance_percentage": 92.5,
            "github_url": "https://github.com/lokesh-bandi",
            "linkedin_url": "https://www.linkedin.com/in/lokesh-bandi",
            "resume_file": "lokesh_resume.pdf",
            "certifications": ["Python Fundamentals", "SQL Basics"],
            "skills": {"Python", "MySQL", "Git"},
            "placement_status": "Preparing",
            "fees_status": "Paid",
            "profile_completion": 90,
            "student_details": ("CGVI0233","Lokesh Bandi",
                                "Codegnan","PFS-VSP-007"),}

print(student["student_id"])
print(student["full_name"])
print(student["course"])

print(type(student))
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

print(student.get("email_id"))
print(student.get("address"))
print(student.get("address", "Not provided"))

student["city"] = "Visakhapatnam"
student["placement_status"] = "Interview Preparation"

student.update({"profile_completion": 95,
                "certifications": student["certifications"] + ["Git Basics"]})
print(student)

student.setdefault("alternate_email", "Not provided")
student.setdefault("city", "Unknown")

fields = ["student_id", "full_name", "email_id", "course"]
new_student = dict.fromkeys(fields)
print(new_student)

student_copy = student.copy()
print(student_copy["student_id"])

print(student.pop("city"))

last_item = student.popitem()
print(last_item)

print("email_id" in student)
print("Not a key" in student)

student.pop("unknown_field", None)

student["city"] = "Visakhapatnam"
student["profile_completion"] = 95

empty_profile = student.copy()
empty_profile.clear()
print(empty_profile)

marks = student["daily_exam_marks"]

marks.append(9)
print(marks)

marks.extend([6, 10])
print(marks)

marks.insert(1, 10)
print(marks)

marks.remove(6)
print(marks)

print(marks.pop())

removed_mark = marks.pop(2)
print(removed_mark)

print(marks.count(10))

print(marks.index(8))

marks.sort()
print(marks)

marks.reverse()
print(marks)

marks_copy = marks.copy()
marks_copy.append(100)
print(marks)
print(marks_copy)

print(marks[:3])
print(marks[-2:])
print(marks[::2])
print(marks[::-1])

temporary_marks = marks.copy()
temporary_marks.clear()
print(temporary_marks)

subjects = student["subjects"]
skills = student["skills"]

subjects.add("Flask")
print(subjects)

subjects.add("Python")
print(subjects)

subjects.update(["FastAPI", "HTML", "CSS"])
print(subjects)

print("Python" in subjects)
print("Java" in subjects)

subjects.remove("CSS")
print(subjects)

subjects.discard("Java")
subjects.discard("Java")
print(subjects)

print(subjects.pop())

name = student["full_name"]
email = student["email_id"]
batch = student["batch_number"]
course = student["course"]
resume = student["resume_file"]

print(name)
print(name.title())
print(name.upper())
print(name.lower())

print(course.replace("Python", "Advanced Python"))

print(len(name))
print(len(course))

print(name[0])
print(name.split()[0])
print(name.split()[-1])
print(student["student_id"][:4])
print(student["mobile_number"][-4:])
print(batch[::-1])

print(course.lower().count("python"))

course_words = course.split()
print(course_words)
print(len(course_words))
print("-".join(course_words))

print(student["student_id"].isalnum())
print("@" in email)
print(batch.isalpha())
print(batch.isalnum())

student["student_details"] = (
    "CGVI0233",
    "Lokesh Bandi",
    "Codegnan",
    "PFS-VSP-007"
)

details = student["student_details"]

print(details)
print(type(details))
print(len(details))

print(details[1])
print(details[-2])
print("Every second element:", details[::2])

print(details.count("Codegnan"))

print(details.index("Lokesh Bandi"))

print("Lokesh Bandi" in details)
print("Python" not in details)

print(details[:2] * 2)

updated_details = (
    details[0],
    "Lokesh Bandi",
    details[2],
    details[3]
)

student["student_details"] = updated_details
print(student["student_details"])

details_list = list(student["student_details"])
details_list.append("Visakhapatnam")

student["student_details"] = tuple(details_list)

print(student["student_details"])

student["exam_details"] = (
    student["daily_exam_marks"],
    student["weekly_exam_marks"]
)

print(student["exam_details"])
print(student["exam_details"][0])
print(student["exam_details"][1])

student["exam_details"][0].append(9)
print(student["exam_details"][0])

print(student["student_details"])
print(student.keys())

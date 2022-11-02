import json


def load_students_from_json():
    with open('students2021.json', encoding='utf-8') as file:
        content_py = json.load(file)

    return content_py


def load_results_1_from_json():
    with open('tests1_result2021.json', encoding='utf-8') as file:
        content_py = json.load(file)

    return content_py


def load_results_2_from_json():
    with open('tests2_result2021.json', encoding='utf-8') as file:
        content_py = json.load(file)

    return content_py

# print(len(load_students_from_json()))
# print(load_students_from_json())


# def get_all_students():
#     students = load_students_from_json()
#     return students


def get_student_by_userid(userid):
    students = load_students_from_json()
    for student in students:
        if student.get("userID") == str(userid):
            return student


def get_student_by_userid(userid):
    students = load_students_from_json()
    for student in students:
        if student.get("userID") == str(userid):
            return student["fio"]


# print(get_student_by_userid(2009071514))


def get_students_id(userid):
    students = load_students_from_json()
    for student in students:
        if student.get("userID") == str(userid):
            return student["id"]


# print(get_students_id(2009071514))


def get_students_ball_1(userid):
    students = load_results_1_from_json()
    students_id = get_students_id(userid)
    for student in students:
        if student.get('id') == students_id:
            return student["ball"]


# print(get_students_ball_1(2009071514))


def get_students_ball_2(userid):
    students = load_results_2_from_json()
    students_id = get_students_id(userid)
    for student in students:
        if student.get('id') == students_id:
            return student["ball"]


# print(get_students_ball_2(2009071514))


#123 def get_students_by_name(student_name):
#     students = load_students_from_json()
#     students_list = []
#     for student in students:
#         if student_name.lower() in student.get('fio').lower():
#             students_list.append(student)
#     return students_list


# candidates_name = 'Aзаматов'
# print(get_students_by_name(candidates_name))


# def get_candidates_by_skill(skill_name):
#     skill_name = skill_name.lower()
#     students = load_students_from_json()
#     students_list = []
#     for student in students:
#         skills = student.get('skills')
#         list_of_skills = skills.lower().split(', ')
#         if skill_name in list_of_skills:
#             students_list.append(student)
#     return students_list


# skill_to_find = 'very iMporTant face'
# print(get_candidates_by_skill(skill_to_find))







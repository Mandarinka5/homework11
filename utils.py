import json


def load_candidates_from_json():
    with open('candidates.json', encoding='utf-8') as file:
        content_py = json.load(file)

    return content_py

# print(len(content_py))
# print(load_candidates_from_json())

def get_all_candidates():
    candidates = load_candidates_from_json()
    return candidates


def get_candidate_by_id(candidate_id):
    condidates = load_candidates_from_json()
    for candidate in condidates:
        if candidate.get('id') == candidate_id:
            return candidate

# print(get_candidate_by_id(4))


def get_candidates_by_name(candidate_name):
    condidates = load_candidates_from_json()
    candidates_list = []
    for candidate in condidates:
        if candidate_name.lower() in candidate.get('name').lower():
            candidates_list.append(candidate)
    return candidates_list


# candidates_name = 'Austin'
# print(get_candidates_by_name(candidates_name))


def get_candidates_by_skill(skill_name):
    skill_name = skill_name.lower()
    condidates = load_candidates_from_json()
    candidates_list = []
    for candidate in condidates:
        skills = candidate.get('skills')
        list_of_skills = skills.lower().split(', ')
        if skill_name in list_of_skills:
            candidates_list.append(candidate)
    return candidates_list


# skill_to_find = 'very iMporTant face'
# print(get_candidates_by_skill(skill_to_find))




import json
from config import PATH_TO_CANDIDATES_JSON


def load_json(path_to_file: str) -> list[dict]:
    """загружает данные из файла"""
    with open(path_to_file, 'r', encoding='utf-8') as candidates_file:
        data = json.load(candidates_file)

    return data


def get_all_candidate() -> list[dict]:
    """получает список всех кандидатов"""
    all_candidates = load_json(PATH_TO_CANDIDATES_JSON)

    return all_candidates


def get_candidate_by_id(candidate_id: int) -> list[dict]:
    """получает кандидата с указанным id !возвращает список!"""
    candidates = load_json(PATH_TO_CANDIDATES_JSON)
    candidates_by_id = [candidate for candidate in candidates if candidate['id'] == candidate_id]

    return candidates_by_id


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """получает список кандидатов с указанным именем"""
    candidates = load_json(PATH_TO_CANDIDATES_JSON)

    candidates_by_name = [candidate for candidate in candidates if candidate_name.lower() in candidate['name'].lower()]
    print(candidates[0]['name'])
    print(candidate_name.lower())
    return candidates_by_name


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """получает список кандидатов с указанным навыком"""
    candidates = load_json(PATH_TO_CANDIDATES_JSON)

    candidates_by_skill = []
    skill_name = skill_name.lower().strip()
    for candidate in candidates:
        if skill_name in candidate['skills'].lower().split(', '):
            candidates_by_skill.append(candidate)

    return candidates_by_skill



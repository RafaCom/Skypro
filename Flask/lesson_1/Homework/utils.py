import json


def load_candidates():
    with open('/Users/rafaelsirinan/Project_Demo_Flask/lesson_1 /homework/candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
        return candidates

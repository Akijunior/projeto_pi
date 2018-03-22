from fuzzywuzzy import process

def get_search_matches(query, choices, limit=3):
    results = process.extract(query, choices, limit=limit)

    return results
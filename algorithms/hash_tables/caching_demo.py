cache = {}


def get_data(url):
    return []


def get_page(url):
    if cache.get(url):
        return cache[url] # Return data in cache

    data = get_data(url)
    cache[url] = data # Saves the data in cache
    return data

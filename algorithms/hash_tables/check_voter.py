def verify_voter(voted: dict[str, bool], name: str):
    if voted.get(name):
        print('Já votou!')
    else:
        voted[name] = True
        print('Ainda não votou')

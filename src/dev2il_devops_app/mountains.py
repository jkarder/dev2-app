def highest_mountain(mountains):
    if not mountains:
        return None

    return max(mountains, key=lambda mountain: mountain['height'])

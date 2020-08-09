def is_full_house(hand):
    return all([hand.count(i) >= 2 for i in hand])


print(is_full_house(['A', 'A', 'A', 'Q', 'Q']))


def text(txt):
    return sum([1 for i in txt.lower() if i in 'aoieu'])


print(text('asdasd'))

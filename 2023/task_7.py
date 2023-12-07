from measure_time import run_with_measurment

card_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
joker_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def get_combination_strength(cards: str):
    card_map = {e:cards.count(e) for e in set(cards)}
    max_same_cards = max(card_map.values())
    unique_cards_length = len(card_map)
    if max_same_cards == 1:
        return "high_card"
    if max_same_cards == 2:
        if unique_cards_length == 4:
            return "one_pair"
        if unique_cards_length == 3:
            return "two_pair"
    if max_same_cards == 3:
        if unique_cards_length == 3:
            return "three_of_kind"
        if unique_cards_length == 2:
            return "full_house"
    if max_same_cards == 4:
        return "four_of_kind"
    if max_same_cards == 5:
        return "five_of_kind"
    
def get_combination_strength_with_joker(cards: str):
    card_map = {e:cards.count(e) for e in set(cards)}
    max_same_cards = max(card_map.values())
    unique_cards_length = len(card_map)
    joker_count = card_map.get("J", 0)
    if joker_count == 5:
        return "five_of_kind"
    if joker_count == 4:
        return "five_of_kind"
    if joker_count == 3:
        if unique_cards_length == 2:
            return "five_of_kind"
        if unique_cards_length == 3:
            return "four_of_kind"
    if joker_count == 2:
        if unique_cards_length == 2:
            return "five_of_kind"
        if unique_cards_length == 3:
            return "four_of_kind"
        if unique_cards_length == 4:
            return "three_of_kind"
    if joker_count == 1:
        if max_same_cards == 1:
            return "one_pair"
        if max_same_cards == 2:
            if unique_cards_length == 4:
                return "three_of_kind"
            if unique_cards_length == 3:
                return "full_house"
        if max_same_cards == 3:
            if unique_cards_length == 3:
                return "four_of_kind"
        if max_same_cards == 4:
            return "five_of_kind"

    if max_same_cards == 1:
        return "high_card"
    if max_same_cards == 2:
        if unique_cards_length == 4:
            return "one_pair"
        if unique_cards_length == 3:
            return "two_pair"
    if max_same_cards == 3:
        if unique_cards_length == 3:
            return "three_of_kind"
        if unique_cards_length == 2:
            return "full_house"
    if max_same_cards == 4:
        return "four_of_kind"
    if max_same_cards == 5:
        return "five_of_kind"


def get_hands_from_input():
    lines = open("2023/inputs/task7.txt").read().split("\n")
    return [(line.split()[0], int(line.split()[1])) for line in lines]


def part_one(hands: list[tuple[str, int]]):
    combination_map = {
        "five_of_kind": [],
        "four_of_kind": [],
        "full_house": [],
        "three_of_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": []
    }

    for cards, bid in hands:
        hand_strength = get_combination_strength(cards)
        combination_map[hand_strength].append((cards, bid))

    max_points = len(hands)

    result = 0
    for combination in combination_map.values():
        sorted_combination = sorted(combination, key=lambda s: [card_values.index(char) for char in s[0]])
        for cards, bid in sorted_combination:
            result += bid*max_points
            max_points -= 1
    return result


def part_two(hands: list[tuple[str, int]]):
    combination_map = {
        "five_of_kind": [],
        "four_of_kind": [],
        "full_house": [],
        "three_of_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": []
    }

    for cards, bid in hands:
        hand_strength = get_combination_strength_with_joker(cards)
        combination_map[hand_strength].append((cards, bid))

    max_points = len(hands)

    result = 0
    for combination in combination_map.values():
        sorted_combination = sorted(combination, key=lambda s: [joker_order.index(char) for char in s[0]])
        for cards, bid in sorted_combination:
            result += bid*max_points
            max_points -= 1
    return result

if __name__ == '__main__':
    hands = run_with_measurment(get_hands_from_input)
    run_with_measurment(part_one, hands=hands, print_result=True)
    run_with_measurment(part_two, hands=hands, print_result=True)

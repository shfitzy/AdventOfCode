import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util



class Hand:

    def __init__(self, hand, bid, use_jokers=False):
        self.use_jokers = use_jokers
        self.hand = self.calc_card_values(hand)
        self.bid = int(bid)
        self.rank = self.calc_rank(hand)

    def calc_card_values(self, hand):
        return [self.get_card_value(card) for card in hand]
    
    def get_card_value(self, card):
        if card.isdigit(): return int(card)
        if card == 'T': return 10
        if card == 'J': return 11 if not self.use_jokers else 1
        if card == 'Q': return 12
        if card == 'K': return 13
        if card == 'A': return 14

    def calc_rank(self, hand):
        grouped_cards = {}
        for char in hand:
            grouped_cards[char] = grouped_cards.get(char, 0) + 1

        num_jokers = 0
        if self.use_jokers and not grouped_cards.get('J') in [None, 5]:
            num_jokers = grouped_cards.pop('J')

        grouped_cards = sorted([v for _, v in grouped_cards.items()], reverse=True)
        grouped_cards[0] += num_jokers

        return sum([10**c for c in grouped_cards])
    
    def __gt__(self, other):
        if not self.rank == other.rank:
            return self.rank > other.rank
        
        for i in range(len(self.hand)):
            if not self.hand[i] == other.hand[i]:
                return self.hand[i] > other.hand[i]



def solution_1(data):
    hands = sorted([Hand(line[0], line[1]) for line in data], reverse=True)
    return sum([hands[i].bid * (len(hands) - i) for i in range(len(hands))])

def solution_2(data):
    hands = sorted([Hand(line[0], line[1], True) for line in data], reverse=True)
    return sum([hands[i].bid * (len(hands) - i) for i in range(len(hands))])

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt', split=True, split_str=' ')

    print(solution_1(data))
    print(solution_2(data))
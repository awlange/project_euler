def get_hands():
    hands = []
    with open('/Users/alange/programming/projectEuler/files/poker.txt') as f:
    # with open('/Users/alange/programming/projectEuler/files/poker_examples.txt') as f:
        for line in f:
            tmp = line.split()
            hands.append([sort_hand(tmp[0:5]), sort_hand(tmp[5:10])])
    return hands


def sort_hand(hand):
    for i in range(0, len(hand)):
        hival = VALUES[hand[i][0]]
        hi_index = i
        for j in range(i+1, len(hand)):
            jval = VALUES[hand[j][0]]
            if jval > hival:
                hival = jval
                hi_index = j

        tmp = hand[i]
        hand[i] = hand[hi_index]
        hand[hi_index] = tmp

    return hand


VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

HAND_RANKS = [
    'High Card',
    'One Pair',
    'Two Pairs',
    'Three of a Kind',
    'Straight',
    'Flush',
    'Full House',
    'Four of a Kind',
    'Straight Flush',
    'Royal Flush'
]


def get_hand_rank(hand):
    rank = 'High Card'  # Default to lowest rank

    # Bucket the cards by value, also get high card
    high_card = 2
    buckets = [0] * 15
    for card in hand:
        val = VALUES[card[0]]
        buckets[val] += 1
        if val > high_card:
            high_card = val

    # Set the default rank_value for High Card
    rank_value = high_card

    #print buckets

    # Check for pairs, three of a kind, full house, four of a kind
    n_pairs = 0
    n_trios = 0
    n_quartets = 0
    pair_rank_value = 2
    trio_rank_value = 2
    quartet_rank_value = 2
    for b in range(0, 15):
        bv = buckets[b]
        if bv == 2:
            n_pairs += 1
            pair_rank_value = b if b > pair_rank_value else pair_rank_value
        elif bv == 3:
            n_trios += 1
            trio_rank_value = b if b > trio_rank_value else trio_rank_value
        elif bv == 4:
            n_quartets += 1
            quartet_rank_value = b if b > quartet_rank_value else quartet_rank_value

    if n_pairs == 1:
        rank = 'One Pair'
        rank_value = pair_rank_value
    elif n_pairs == 2:
        rank = 'Two Pairs'
        rank_value = pair_rank_value

    if n_trios == 1:
        rank = 'Three of a Kind'
        if n_pairs == 1:
            rank = 'Full House'
            rank_value = trio_rank_value

    if n_quartets == 1:
        rank = 'Four of a Kind'
        rank_value = quartet_rank_value

    # Straight or flush cannot happen with above combos
    if n_pairs == n_trios == n_quartets == 0:
        # Check for a straight
        straight = False
        straight_high_value = 0
        in_a_row_count = 0
        for b in range(0, 15):
            bv = buckets[b]
            if bv > 0:
                in_a_row_count += 1
            else:
                in_a_row_count = 0

            if in_a_row_count == 5:
                straight = True
                straight_high_value = b

        # Check for flush
        flush = False
        flush_high_value = high_card
        if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
            flush = True

        if straight and not flush:
            rank = 'Straight'
            rank_value = straight_high_value
        elif flush and not straight:
            rank = 'Flush'
            rank_value = flush_high_value
        elif straight and flush:
            rank = 'Straight Flush'
            rank_value = straight_high_value
            if straight_high_value == VALUES['A']:
                rank = 'Royal Flush'
                rank_value = straight_high_value

    return rank, rank_value


def get_hand1_wins(p1_hand, p1_rank, p1_rank_value, p2_hand, p2_rank, p2_rank_value):
    """
    Returns 1 if p1 wins the hand, 0 else
    """
    if HAND_RANKS.index(p1_rank) > HAND_RANKS.index(p2_rank):
        return 1
    elif HAND_RANKS.index(p1_rank) < HAND_RANKS.index(p2_rank):
        return 0

    # Ranks are equal
    if p1_rank_value > p2_rank_value:
        return 1
    elif p1_rank_value < p2_rank_value:
        return 0

    # Ranks and rank values are equal, go by highest card until one hand wins
    for i in range(0, 5):
        val1 = VALUES[p1_hand[i][0]]
        val2 = VALUES[p2_hand[i][0]]
        if val1 > val2:
            return 1
        elif val1 < val2:
            return 0

    print "WTF"
    return 0


def main():
    p1_wins = 0
    for hand in get_hands():
        p1_rank, p1_rank_value = get_hand_rank(hand[0])
        p2_rank, p2_rank_value = get_hand_rank(hand[1])
        # print hand[0], p1_rank, p1_rank_value, hand[1], p2_rank, p2_rank_value, win
        p1_wins += get_hand1_wins(hand[0], p1_rank, p1_rank_value, hand[1], p2_rank, p2_rank_value)

    print "Player 1 wins:", p1_wins

if __name__ == '__main__':
    main()
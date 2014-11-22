def make_bins(n_dice, max_val):
    max_bin_val = max_val*n_dice
    bins = [0 for _ in range(max_bin_val + 1)]
    dice = [1 for _ in range(n_dice)]

    tot = 0
    while tot < max_bin_val:
        tot = sum(dice)
        bins[tot] += 1

        dice[0] += 1

        # carry the one..
        for i in range(n_dice):
            if dice[i] > max_val:
                dice[i] = 1
                if i+1 < n_dice:
                    dice[i+1] += 1


    # Now convert each bin to a probability
    n_rolls = float(sum(bins))
    probs = [float(x) / n_rolls for x in bins]

    return probs


def compute_cumulative(l):
    # sum up probs for a given n less than n
    # in other words, what is the probability of rolling the dice such the the value is less than n
    cumulative = [0.0 for _ in range(len(l))]
    running_sum = 0.0
    for i in range(len(l)):
        cumulative[i] += running_sum
        running_sum += l[i]
    return cumulative



pete_probs = make_bins(9, 4)
colin_probs = make_bins(6, 6)
cumulative_pete_probs = compute_cumulative(pete_probs)
cumulative_colin_probs = compute_cumulative(colin_probs)
print pete_probs
print cumulative_colin_probs

pete_wins = 0.0
for i in range(len(pete_probs)):
    pete = pete_probs[i]
    colin = cumulative_colin_probs[i]
    pete_wins += pete * colin

print pete_wins


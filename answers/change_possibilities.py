def change_possibilities(coins, amount):
	# returns number of possible combinations of coins to add up to value
	# ([1,2,3], 4) => 4
	# ([1,2], 5) => 2
	# ([2], 9) => 0
	# ([], 5) => 0
	# ([1,2,3], 0) => 0

	# reverse sort array
	reverse_coins = reverse_sort(coins)
	solves = 0
	
	for i in range(len(reverse_coins)):
		potential_solves = []
		if reverse_coins[i] > amount:
			continue
		else:
			potential_solves.append(reverse_coins[i])
			new_amount = amount - reverse_coins[i]
			j = i
			while True:
				if reverse_coins[j] > new_amount:
					if j != len(reverse_coins) - 1:
						j += 1
						continue
					else:
						break
				elif reverse_coins[j] == new_amount:
					potential_solves.append(reverse_coins[j])
				else:
					potential_solves.append(reverse_coins[j])
					new_amount -= reverse_coins[j]

				if sum(potential_solves) == amount:
					solves += 1
					if j == len(reverse_coins)-1:
						break
					else:
						
						potential_solves = [reverse_coins[i]]
						j += 1
						continue
				else:
					continue
	return solves



def reverse_sort(coins):
	# bubble reverse sort
	swap_made = True
	swaps = 0
	if len(coins) < 2:
		return coins
	else:
		while swap_made:
			for i in range(len(coins)-1):
				if coins[i] < coins[i+1]:
					temp = coins[i+1]
					coins[i+1] = coins[i]
					coins[i] = temp
					swaps += 1
				if i == len(coins)-2:
					if swaps == 0:
						swap_made = False
					else:
						swaps = 0
		return coins

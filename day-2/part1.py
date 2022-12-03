def main():
	with open('input.txt') as f:
		rounds = f.readlines()
		score = 0
		for r in rounds:
			moves = r.split()
			score += get_score(moves)
		print(score)

def get_score(moves):
	score = 0
	shape_scores = {'X': 1, 'Y': 2, 'Z': 3}
	score += shape_scores[moves[1]]
	# transform move values to 0, 1 or 2
	moves[0] = ord(moves[0]) - ord('A')
	moves[1] = ord(moves[1]) - ord('X')
	move_scores = {0:3, -1:0, 1:6, 2:0, -2:6}
	move = moves[1] - moves[0]
	score += move_scores[move]
	return score
	

if __name__ == "__main__":
	main()
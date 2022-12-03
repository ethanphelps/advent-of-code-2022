def main():
    with open('input.txt') as f:
        rounds = f.readlines()
        score = 0
        for r in rounds:
            moves = r.split()
            shape, outcome_points = get_shape(moves)
            score += outcome_points
            score += get_score(shape)
        print(score)

# returns shape to choose and score associated with outcome
def get_shape(moves):
    shapes_to_index = {'A': 0, 'B': 1, 'C': 2}
    shapes = ['A', 'B', 'C']
    if moves[1] == 'X':
        # lose: choose shape that precedes opponent's shape (wrapping to 2 with negative index)
        return shapes[shapes_to_index[moves[0]] - 1], 0
    elif moves[1] == 'Y':
        # draw: choose same shape as opponent
        return moves[0], 3
    else:
        # win: choose shape that follows opponent's shape (wrapping to 0 with modulo operator)
        return shapes[(shapes_to_index[moves[0]] + 1) % 3], 6

def get_score(shape):
	shape_scores = {'A': 1, 'B': 2, 'C': 3}
	return shape_scores[shape]

if __name__ == "__main__":
	main()
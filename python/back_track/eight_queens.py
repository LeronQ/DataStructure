# 棋盘尺寸
BOARD_SIZE = 8

solution_count = 0
queen_list = [0] * BOARD_SIZE



def eight_queens(cur_column):
	"""
		输出所有符合要求的八皇后序列
		用长度为8的数组代表棋盘的列，数组的数字则表示为当前列上的皇后所在的行数
	"""
	if cur_column >= BOARD_SIZE:
		global solution_count
		solution_count += 1
		# 打印出一种解
		print(queen_list)
	else:
		for i in range(BOARD_SIZE):
			if is_valid_pos(cur_column,i):
				queen_list[cur_column] = i
				eight_queens(cur_column +1)



def is_valid_pos(cur_column,pos):
	"""
		采取的是每一列放置一个皇后的做法，所以检查的时候不必检查猎德合法性，只需要检查行和对角是否符合要求
		1: 检查行：检查数组在下标为cur_column之前的元素是否已经存在pos
		2：检查对角：检查数组在下标为cur_column之前的元素，其行的间距为pos - QUEEN_LIST[i]
		和列的间距为cur_column - i是否一致
	"""
	i = 0
	while i < cur_column:
		# 是否同行
		if queen_list[i] == pos:
			return False
		# 对角线
		if cur_column - i == abs(pos - queen_list[i]):
			return False
		i += 1
	return True


if __name__ == '__main__':
	print("all soutions sequence")
	eight_queens(0)

	print("the number of soutions")
	print(solution_count)


import os

def _preprocess_add_path(home_path, dest_path):
	dest_path = dest_path.strip().lstrip('/')
	if dest_path[0] =='/':
		return dest_path

	home_path = home_path.strip().rstrip('/')
	if home_path[0] == '~':
		home_path = os.path.expanduser("~")+home_path[1:]
	elif home_path[0] == '/':
		home_path = '/'+ home_path.strip('/')
	else:
		home_path = os.getcwd() + '/' + home_path
	return home_path +'/'+ dest_path


def _get_final_path(final_path):
	Stack = []
	splitted_path = final_path.split('/')
	for x in splitted_path:
		if x == '.':
			pass

		elif x == '..':
			if Stack != []:
				Stack.pop()
		else:
			Stack.append(x)
	# print(Stack)
	return ('/'.join(Stack))

def join(home_path, dest_path):
	final_path = _preprocess_add_path(home_path, dest_path)
	abs_path = _get_final_path(final_path)
	print(abs_path)
	return abs_path

if __name__ == '__main__':
	join('/home/raja', 'a/b/c/./../d/e/f/../g/../h')
	join('cnd c/ cd/ cd/ home/raja', '../../../../../././../../')
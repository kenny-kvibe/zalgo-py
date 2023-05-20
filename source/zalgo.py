from constants import POSITION_KEYS, POSITION_OPTS, STRENGTH_KEYS, STRENGTH_OPTS, TEXT_CONCAT_KEYS, TEXT_CONCAT_OPTS
import random
import re


def transform(text:str, strength:str = 'normal', position:str = 'random', text_concat:str = 'after') -> str:
	"""
	Add zalgo characters to a string.\n
	---
	:param `text`: string – text to process
	:param `strength`: string – "normal", "small", "big", "extreme"
	:param `position`: string – "above", "middle", "below", "random", "all"
	:param `text_concat`: string – "before", "after", "random", "all"
	"""
	string = ''
	skip = ('\n', '\r', '\0')
	if strength in STRENGTH_KEYS and position in POSITION_KEYS and text_concat in TEXT_CONCAT_KEYS:
		set_char = TEXT_CONCAT_OPTS[text_concat]
		for char in text:
			if char not in skip:
				min = STRENGTH_OPTS[strength]['min']
				max = STRENGTH_OPTS[strength]['max']
				for _ in range(random.randint(min, max)):
					char = set_char(char, POSITION_OPTS[position]())
			string += char
	return string


def clear(text:str) -> str:
	"""
	Remove the zalgo characters from a string.\n
	---
	:param `text`: string – text to process
	"""
	return re.sub(r'[\u0300-\u036f]', '', text)


def print_transform(text:str, count:int = 1, strength:str = 'normal', position:str = 'random', text_concat:str = 'after') -> None:
	"""
	Print text with zalgo characters.\n
	---
	:param `text`: string – text to process with `transform()`
	:param `count`: integer – number of times to process text
	:param `strength`: string – "normal", "small", "big", "extreme"
	:param `position`: string – "above", "middle", "below", "random", "all"
	:param `text_concat`: string – "before", "after", "random", "all"
	"""
	if count == 1:
		print('\n '+transform(text, strength, position, text_concat)+'\n')
	elif count > 1:
		texts = [transform(text, strength, position, text_concat) for _ in range(count)]
		print('\n '+'  '.join(texts)+'\n')


if __name__ == '__main__':
	print_transform('EXAMPLE', 5, 'normal', 'random', 'before')
	print_transform('EXAMPLE', 5, 'normal', 'random', 'after')
	print_transform('EXAMPLE', 5, 'normal', 'above', 'random')
	print_transform('EXAMPLE', 5, 'normal', 'below', 'random')
	print_transform('EXAMPLE', 1, 'extreme', 'random', 'random')
	raise SystemExit(0)

import random
import re

from constants import (
	POSITION_KEYS,
	POSITION_OPTS,
	REGEX_NON_ZALGO_PATTERN,
	REGEX_ZALGO_PATTERN,
	STRENGTH_KEYS,
	STRENGTH_OPTS,
	TEXT_CONCAT_KEYS,
	TEXT_CONCAT_OPTS
)


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
		concat_char = TEXT_CONCAT_OPTS[text_concat]
		for char in text:
			if char not in skip:
				min = STRENGTH_OPTS[strength]['min']
				max = STRENGTH_OPTS[strength]['max']
				for _ in range(random.randint(min, max)):
					char = concat_char(char, POSITION_OPTS[position]())
			string += char
	return string


def replace(text:str, new_chars:str) -> str:
	"""
	Replace the non-zalgo characters with the new characters.\n
	---
	:param `text`: string – text to process
	:param `new_chars`: string – new text within param `text`
	"""
	len_nchars = len(new_chars)
	text_count = 0
	for ch in text:
		if re.match(REGEX_NON_ZALGO_PATTERN, ch):
			text_count += 1
	if text_count != len_nchars:
		print(len(text), len_nchars)
		raise ValueError('Length of `text` is not equal to length of `new_chars`')
	new_i = 0
	new_text = ''
	for ch in text:
		if re.match(REGEX_NON_ZALGO_PATTERN, ch):
			if new_i < len_nchars:
				new_text += re.sub(REGEX_NON_ZALGO_PATTERN, new_chars[new_i], ch, 1)
				new_i += 1
		else:
			new_text += ch
	return new_text


def clear(text:str) -> str:
	"""
	Remove the zalgo characters from a string.\n
	---
	:param `text`: string – text to process
	"""
	return re.sub(REGEX_ZALGO_PATTERN, '', text)


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
	print('\n\n\n', transform('EXAMPLE', 'extreme', 'random', 'random')+'\n\n\n')
	print('', replace(transform('EXAMPLE', 'small', 'random', 'random'), '1234567'))
	raise SystemExit(0)

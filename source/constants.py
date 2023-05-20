import random

Z_CHARS = {
	'above':  ['\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307', '\u0308', '\u0309', '\u030a', '\u030b', '\u030c', '\u030d', '\u030e', '\u030f', '\u0310', '\u0311', '\u0312', '\u0313', '\u0314', '\u031a', '\u033d', '\u033e', '\u033f', '\u0340', '\u0341', '\u0342', '\u0343', '\u0344', '\u0346', '\u034a', '\u034b', '\u034c', '\u0350', '\u0351', '\u0352', '\u0357', '\u0358', '\u035b', '\u035d', '\u035e', '\u0360', '\u0361', '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', '\u0368', '\u0369', '\u036a', '\u036b', '\u036c', '\u036d', '\u036e', '\u036f'],
	'middle': ['\u0315', '\u031b', '\u0334', '\u0335', '\u0336', '\u0337', '\u0338'],
	'below':  ['\u0316', '\u0317', '\u0318', '\u0319', '\u031c', '\u031d', '\u031e', '\u031f', '\u0320', '\u0321', '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u0329', '\u032a', '\u032b', '\u032c', '\u032d', '\u032e', '\u032f', '\u0330', '\u0331', '\u0332', '\u0333', '\u0339', '\u033a', '\u033b', '\u033c', '\u0345', '\u0347', '\u0348', '\u0349', '\u034d', '\u034e', '\u0353', '\u0354', '\u0355', '\u0356', '\u0359', '\u035a', '\u035c', '\u035f', '\u0362']
}

POSITION_OPTS = {
	'above':  lambda: random.choice(Z_CHARS['above']),
	'middle': lambda: random.choice(Z_CHARS['middle']),
	'below':  lambda: random.choice(Z_CHARS['below']),
	'random': lambda: random.choice(Z_CHARS[random.choice(Z_CHARS_KEYS)]),
	'all':    lambda: POSITION_OPTS['above']() +\
					  POSITION_OPTS['middle']() +\
					  POSITION_OPTS['below']()
}

STRENGTH_OPTS = {
	'normal':  {'max': 7,   'min': 1},
	'small':   {'max': 3,   'min': 0},
	'big':     {'max': 16,  'min': 3},
	'extreme': {'max': 100, 'min': 20}
}

TEXT_CONCAT_OPTS = {
	'after':  lambda ch, z: ch+z,
	'before': lambda ch, z: z+ch,
	'all':    lambda ch, z: z+ch+z,
	'random': lambda ch, z: random.choice((z+ch, ch+z, z+ch+z))
}

Z_CHARS_KEYS = tuple(Z_CHARS.keys())
POSITION_KEYS = tuple(POSITION_OPTS.keys())
STRENGTH_KEYS = tuple(STRENGTH_OPTS.keys())
TEXT_CONCAT_KEYS = tuple(TEXT_CONCAT_OPTS.keys())

separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
             '|', '^', '++', '--', ',']
reservedWords = ['rd', 'wrt', 'nmbr','char', 'strng','array','chck', 'is', 'true', 'false', 'let', 'and']

tot= separators + operators + reservedWords
codification = dict([(tot[i], i + 2) for i in range(len(tot))])
codification['identifier'] = 0
codification['constant'] = 1
import re


class NameTooShortError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


email = input()
EMAIL_MINIMUM = 4
DOMAINS = ['com', 'bg', 'org', 'net']
pattern_name = r'\w+'

while email != 'End':
    if email.count('@') > 1:
        raise MustContainAtSymbolError('Email must contain only one @ symbol!')

    elif '@' not in email:
        raise MustContainAtSymbolError('Email must contain only an @ symbol!')

    elif len(email.split('@')[0]) <= EMAIL_MINIMUM:
        raise NameTooShortError(f'Name must be more than {EMAIL_MINIMUM} characters')

    elif email.split('.')[-1] not in DOMAINS:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join("." + d for d in DOMAINS)}')

    elif re.findall(pattern_name, email.split('@')[0])[0] != email.split('@')[0]:
        raise InvalidNameError('Name must contain only letters, digits and underscores!')

    print('Email is valid')

    email = input()

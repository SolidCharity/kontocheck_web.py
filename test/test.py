# to run:
# source ~/pyenv/bin/activate
# python3 test.py

import kontocheck
print(dir(kontocheck))
kontocheck.lut_load()
print(kontocheck.lut_is_valid())
bankname = kontocheck.get_name('37040044')
print(bankname)
iban = kontocheck.create_iban('37040044', '532013000')
print(iban)
print(kontocheck.check_iban(iban))
bic = kontocheck.get_bic(iban)
bankname = kontocheck.scl_get_bankname('VBOEATWW')


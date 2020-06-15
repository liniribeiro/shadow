import re

import requests
from validate_docbr import CNPJ

from alura.data_validation.brazilian_phones import BrazilianPhone
from alura.data_validation.brazilians_date import BrazilianDate
from alura.data_validation.address import SearchAddress
from alura.data_validation.cpf_cnpj_handler import CpfCnpj, DocumentType


# exemplo_cpf = '06721735903'
# exemplo_cnpj = '01401082000149'
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
#
#
# cpf = CpfCnpj(exemplo_cnpj, DocumentType.cnpj)
# print(cpf)

#
# padrao_molde = '(xx) aaaa-wwww'
# pad = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
# texto = 'eu gosto de 47992334930 e 988456798'
#
# phone = '5547992334567'
# output = BrazilianPhone(phone)
#
# print(output.fortmat_number())


# a = BrazilianDate()
# print(a.month())
# print(a.week_day())
# print(a)

#

cep = '89150000'
v = SearchAddress(cep)
print(v.get_by_cep())

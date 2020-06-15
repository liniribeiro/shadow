from enum import Enum

from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def create_document(document):
        if len(document) == 11:
            DocCPF(document)
        elif len(document) == 14:
            DocCNPJ(document)
        else:
            raise ValueError('Quantidade de dígitos incorreta!')


class DocCPF:
    def __init__(self, document):
        if self.validate(document):
            self.cpf = document
        else:
            raise ValueError("CPF Inválido")

    def __str__(self):
        return self.format()

    @staticmethod
    def validate(document):
        validator = CPF()
        return validator.validate(document)

    def format(self):
        mask = CPF()
        return mask.mask(self.cpf)


class DocCNPJ:
    def __init__(self, document):
        if self.validate(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ Inválido")

    def __str__(self):
        return self.format()

    @staticmethod
    def validate(cnpj):
        validator = CNPJ()
        return validator.validate(cnpj)

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)


class DocumentType(Enum):
    cpf = 'cpf'
    cnpj = 'cnpj'

    def __eq__(self, other):
        return self.name == other.name


class CpfCnpj:

    def __init__(self, document, document_type: DocumentType):

        if document_type == document_type.cpf:
            if not self.is_cpf_valid(document):
                raise ValueError("CPF Inválido")

            self.document = document
        elif document_type == document_type.cnpj:
            if not self.is_cnpj_valid(document):
                raise ValueError("CNPJ Inválido")

            self.document = document
        self.document_type = document_type

    def __str__(self):
        if self.document_type == DocumentType.cpf:
            return self.format_cpf()
        elif self.document_type == DocumentType.cnpj:
            return self.format_cnpf()

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self.document)

    def format_cnpf(self):
        mask = CNPJ()
        return mask.mask(self.document)

    @staticmethod
    def is_cpf_valid(document):
        if not len(document) == 11:
            raise ValueError('Quantidade de dígitos errada!')
        validator = CPF()
        return validator.validate(document)

    @staticmethod
    def is_cnpj_valid(cnpj):
        if not len(cnpj) == 14:
            raise ValueError('Quantidade de dígitos errada!')
        validator = CNPJ()
        return validator.validate(cnpj)
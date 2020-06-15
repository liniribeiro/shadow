from datetime import datetime, timedelta


class BrazilianDate:
    def __init__(self):
        self.date = datetime.today()

    def __str__(self):
        return self.format_data()

    def month(self):
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
                 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                 'Outubro', 'Novembro', 'Desembro']
        return meses[self.date.month - 1]

    def week_day(self):
        days = ['Segunda', 'Terça', 'Quarta', 'Quinta',
                'Sexta', 'Sábado', 'Domingo']
        return days[self.date.weekday()]

    def format_data(self):
        return self.date.strftime("%d/%m/%Y  %H:%M")

    def time_from_registration(self):
        return (datetime.today() - timedelta(days=30)) - self.date

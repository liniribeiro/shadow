class URLExtractor:
    def __init__(self, url):
        if self.valid_url(url):
            self.url = url
        else:
            raise LookupError('URL INVáLIDA!!!!!')

    @staticmethod
    def valid_url(url):
        return True if url else False


url_string = 'https://www.youtube.com/watch?v=UVLyStyYEG4'
# url_string = ''
print(URLExtractor(url_string))



email1 = 'alinididid'
email2 = ' falie comigo xanana'
email3 = 'aham, xasas'
email4 = 'aliniribeiroo@gmail.com'


padrao = ''
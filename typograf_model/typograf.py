# coding: utf-8
from .http import request


class Typograf():
    url = "http://typograf.artlebedev.ru/webservices/"
    post_url = url + 'typograf.asmx'
    action_url = url + 'ProcessText'
    entity_type = 3
    use_br = 0
    use_p = 1
    max_nobr = 3
    timeout = 10

    def __init__(self, timeout=15):
        self.timeout = timeout

    def process(self, text):
        headers = {
            'Content-Type': 'text/xml',
            'SOAPAction': self.action_url,
        }
        soap_body = '<?xml version="1.0" encoding="UTF-8"?>\n'
        soap_body += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' \
                     'xmlns:xsd="http://www.w3.org/2001/XMLSchema" ' \
                     'xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n'
        soap_body += '<soap:Body>\n'
        soap_body += ' <ProcessText xmlns="http://typograf.artlebedev.ru/webservices/">\n'
        soap_body += '  <text>%s</text>\n' % text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        soap_body += '     <entityType>%s</entityType>\n' % self.entity_type
        soap_body += '     <useBr>%s</useBr>\n' % self.use_br
        soap_body += '     <useP>%s</useP>\n' % self.use_p
        soap_body += '     <maxNobr>%s</maxNobr>\n' % self.max_nobr
        soap_body += '	</ProcessText>\n'
        soap_body += ' </soap:Body>\n'
        soap_body += '</soap:Envelope>\n'
        soap_body = soap_body.encode('utf-8')
        status_code, response = request('POST', self.post_url, data=soap_body, headers=headers, timeout=self.timeout)
        response = response[(response.find('<ProcessTextResult>') + 19):response.find('</ProcessTextResult>')]
        response = response.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        return response


typograf = Typograf()


def typo(text, is_para=True):
    typograf.use_p = is_para
    try:
        return typograf.process(text)
    except:
        return text
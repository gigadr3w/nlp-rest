import talon, json
from talon import quotations
from talon.signature.bruteforce import extract_signature

class EmailDataModel:
    def __init__(self, content, sender) -> None:
        self.Content = content
        self.Sender = sender

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
def get_reply_from_plain_text(mail_body:str) -> str:
    talon.init()
    return quotations.extract_from_plain(mail_body)

def get_reply_from_html(mail_body:str) -> str:
    talon.init()
    return quotations.extract_from_html(mail_body)

def get_text_and_signature(mail_body:str, sender:str) -> EmailDataModel:
    talon.init()
    content, signature = extract_signature(mail_body)
    if(content==signature or signature is None):
        from talon import signature
        content, signature = signature.extract(mail_body, sender)
    return  EmailDataModel(content, signature)
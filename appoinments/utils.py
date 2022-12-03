import base64
import hashlib
import hmac


def webhookSignature(receivedSignature: str, payload):
    WEBHOOK_SECRET = "admin3450"
    digest = hmac.new(WEBHOOK_SECRET.encode('utf-8'), payload, hashlib.sha256).digest()
    e = base64.b64encode(digest).decode()
    if(e == receivedSignature):
        return True
    return False 

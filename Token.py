import hashlib
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/your-url', methods=['GET'])
def wechat_auth():
    token = "0750"  # 填写您在公众平台上设置的Token
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echostr = request.args.get('echostr', '')
    s = [timestamp, nonce, token]
    s.sort()
    s = ''.join(s).encode('utf-8')
    if hashlib.sha1(s).hexdigest() == signature:
        return echostr
    else:
        return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# api/index.py
from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_response():
    url = request.args.get('url')
    if not url:
        return Response("❌ لم يتم إرسال الرابط (url)", status=400, content_type="text/plain; charset=utf-8")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        res = requests.get(url, headers=headers, timeout=15)
        res.encoding = 'utf-8'

        return Response(res.text, content_type="text/plain; charset=utf-8")
    except requests.exceptions.RequestException as e:
        return Response(f"❌ حدث خطأ أثناء جلب الرابط:\n{str(e)}", status=500, content_type="text/plain; charset=utf-8")

# ملاحظة: لا تضع app.run() في Vercel

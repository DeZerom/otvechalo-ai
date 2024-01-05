from flask import Flask, request
from ai import get_answer

app = Flask(__name__)


@app.post('/answer-question')
def answer_question():
    context = request.get_json()['context']
    query = request.get_json()['query']

    return {'answer': get_answer(context, query)}


if __name__ == '__main__':
    app.run(debug=True, port=5001)

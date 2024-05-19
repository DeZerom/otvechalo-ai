from flask import Flask, request
from ai import get_answer

app = Flask(__name__)


@app.post('/answer-question')
def answer_question():
    print('Received request')
    context = request.get_json()['context']
    query = request.get_json()['query']

    print('Query is ', query)
    print('Context is ', context)

    answer = get_answer(context, query)
    print('Answer is ', answer)

    return {'answer': answer}


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')

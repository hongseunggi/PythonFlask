from flask import Flask

app = Flask(__name__)


@app.route("/")
def http_prepost_response():
    return "/"


@app.before_first_request
def before_first_request():
    print("first http request")


@app.before_request
def before_request():
    print("요청 처리 전 실행")


@app.after_request
def after_request(response):
    print("요청 처리 후 실행")
    return response


@app.teardown_request
def teardown_request(exception):
    print("매 요청의 결과가 브라우저에 응답하고 나서 호출")


@app.teardown_appcontext
def teardown_appcontext(exception):
    print("애플리케이션 컨텍스트가 종료될 때 실행")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
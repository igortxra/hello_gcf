from main import hello


def test_hello(request):
    hello_message = "Hello World!"
    assert hello(None) == ({'message': 'Hello World'}, 200)

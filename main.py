def hello(request):
    hello_message = "Hello World!"
    print('[INFO]', hello_message)
    return {"message": "Hello World"}, 200

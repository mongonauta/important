import requests

print(requests.post(
    url='http://127.0.0.1:5000/post_loader',
    data="""
def hello():
    return 'esto me ha llegado por post'
    
    """
))

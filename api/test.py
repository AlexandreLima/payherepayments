from .http_re import HttpRequest
import pytest

def test():
    http = HttpRequest()
    response = http.get("https://jsonplaceholder.typicode.com/posts/1", None, None)
    assert  len(response) > 0            
#encoding: utf-8

from urllib.parse import urlparse,urljoin
from flask import request

def is_safe_url(target):
    #  将urlstring解析成6个部分，它从urlstring中取得URL，
    #  并返回元组 (scheme, netloc, path, parameters, query, fragment)
    #  netloc 服务器位置,域名
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
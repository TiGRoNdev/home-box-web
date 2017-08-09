#! /usr/bin/python

def wsgi_app(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	body = "\n".join(environ["QUERY_STRING"][2:].split(sep="&"))
	start_response(status, headers)
	return [body]

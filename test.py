import webapp2

def main_page_test():
	app = webapp2.get_app()
	res = app.get_response('/')
	assert res.status_int == 200
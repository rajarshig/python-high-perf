from bottle import route, run
from utils.split import split_file

@route('/')
def index():
    return "index"


@route('/large-file-split')
def large_file_split():
    status = split_file()
    return str(status)

run(host='localhost', port=8080)
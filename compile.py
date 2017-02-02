#  coding=utf-8
import sys, getopt
import os
import re

project_path = os.path.dirname(os.path.abspath(__file__))
dist_path = os.path.join(project_path, 'static/dist')
template_path = os.path.join(project_path, 'templates/template.html')
index_path = os.path.join(project_path, 'templates/index.html')

str_replaced = r'{# gadu.js #}'
help = '''
    -h      help
    --debug debug mode
    --build production mode
'''


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["debug", "build"])
    except getopt.GetoptError:
        print help
        return
    opt, arg = opts[0]
    if opt == '--debug':
        return debug()
    if opt == '-h':
        print help
        return
    if opt == '--build':
        production()


def write(str='gadu.js'):
    with open(template_path, 'r') as f:
        html = f.read()
        html = re.sub(str_replaced, str, html)

    with open(index_path, 'w') as f:
        f.write(html)
    print 'success'


def debug():
    print "it's debug"
    write()


def production():
    print "it's production"
    files = os.listdir(dist_path)
    try:
        for file in files:
            if re.match(r'gadu-\w{8}\.js', file):
                file_name = file
                print 'chunkname is ', file_name
                write(file_name)
                return
        print "not found"
    except:
        print 'error'


if __name__ == '__main__':
    main(sys.argv[1:])

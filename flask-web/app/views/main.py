#encoding:utf8

from flask import abort
from flask import Blueprint
from flask import current_app
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/floatdemo')
def float_demo():
    #for k in dir(request):
    #    print k,getattr(request,k)
    return render_template('float-demo.html')

@bp.route('/angulardemo')
def angular_demo():
    return render_template('angular-demo.html')

@bp.route('/backbonedemo')
def backbone_demo():
    print 'dfde'
    return render_template('backbone-demo.html')

@bp.route('/css_selector_demo')
def css_selector_demo():
    print 'dfde'
    return render_template('css-selector-demo.html')

@bp.route('/html_demo')
def html_demo():
    print 'dfde'
    return render_template('html-demo.html')

@bp.route('/xieruhuause/upload.php', methods=['GET', 'POST'])
def xieruhuause():
    print 'xieruhuause'
    print request.files
    print request.form
    print request.args
    #print dir(request)
    print type(request.data), len(request.data)
    
    print request.headers
    #fo=request.files['userfile']
    #print dir(fo)
    #fo.save('temp.txt')
    #fo.close()
    #print dir(request.files)
    for item in request.files:
        print item
    for k,v in request.files.items():
        #print k, v
        if k.endswith('[]'):v=request.files.getlist(k)
        print k, v
        
    return 'xxx'

@bp.route('/xml_http_request_demo', methods=['GET', 'POST'])
def xml_http_request_demo():
    if request.method=='GET':
        return render_template('xml_http_request_demo.html')

@bp.route('/bootstrap_demo', methods=['GET', 'POST'])
def bootstrap_demo():
    return render_template('bootstrap/button.html')

@bp.route('/table_demo', methods=['GET', 'POST'])
def table_css_demo():
    return render_template('table_css_demo.html')
        
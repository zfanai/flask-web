#encoding:utf8

from flask import abort
from flask import Blueprint
from flask import make_response
from flask import current_app
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import jsonify

from app import cache
from app.forms.auth import LoginForm

bp = Blueprint('main', __name__)

@bp.route('/xxx')
def xxx():
    return 'dfdfff'

# 测试前后端分离，跨域访问。
@bp.route('/login2', methods=['GET', 'POST'])
def login2():
    #return 'dfef'
    response=make_response('dfasfefasdfefasdfef')
    response.headers['Access-Control-Allow-Origin']='*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-request-with,content-type'
    #print 'headers2:', response.headers
    
    return response

@bp.route('/')
def index():
    #for k in dir(request):print 'request:', k
    print 'host:', request.host
    print 'host_url:', request.host_url
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


@bp.route('/auto_margin_demo', methods=['GET', 'POST'])
def auto_margin_demo():
    return render_template('auto_margin_demo.html')

@bp.route('/font_unit_demo')
def font_unit_demo():
    return render_template('font_unit_demo.html')

@bp.route('/pseudo_class_element_demo')
def pseudo_class_element_demo():
    return render_template('pseudo_class_element_demo.html')

@bp.route('/echarts_study')
def echarts_study():
    return render_template('echarts_study.html')

@bp.route('/test_cache', methods=['POST', 'GET'])
def test_cache():
    cache.set('aa', 123)    
    return jsonify({
        'error':0
    })

@bp.route('/test_cache2', methods=['POST', 'GET'])
def test_cache2():
    print cache.get('aa')    
    return jsonify({
        'error':0
    })

@bp.route('/xss_study', methods=['POST', 'GET'])
def xss_study():
    if 'GET'==request.method:
        return render_template('xss_study.html')
    return render_template('xss_study.html')


@bp.route('/wtf_demo', methods=['POST', 'GET'])
def wtf_demo():
    if 'GET'==request.method:
        g.login_form=LoginForm()
        #print dir(g.login_form)
        #print 'csrf_token:', g.login_form.csrf_enabled, g.login_form.csrf_token
        #print 'validate on submit:',  g.login_form.validate_on_submit()
            
        return render_template('wtf_demo.html')

    g.login_form = LoginForm()
    print 'post validate on submit:', g.login_form.validate_on_submit()
    
    return render_template('wtf_demo.html')
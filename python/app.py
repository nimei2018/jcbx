#!/usr/local/python27/bin/python 
# -*- coding:UTF-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, render_template, request, flash, url_for, redirect, session, json,jsonify
import  os
import  requests
import  re
import subprocess


app = Flask(__name__,static_url_path='/static')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


# 监控url
try:
    app.config.from_pyfile('watchlist.py')
    watchlist = app.config.get('WATCHLIST')
except (RuntimeError, IOError):
    watchlist = []


def sess_check(func):
    def sess(*args,**kw):
        if username in session:
            return  func(*args,**kw)
        else:
            return redirect('/')
    return sess


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login',methods=['GET','POST'])
def login():
    global username
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "dev"  and  password == "dev":
            # session[username] = username
            return redirect('/test')
        elif username == "admin" and  password == "admin":
            session[username] = username
            return redirect('/updata')
        else:
            return redirect('/')
    return redirect('/')


@app.route('/updata')
# @sess_check
def updata():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/xsl')
def xsl():
    return render_template('xsl.html')

@app.route('/hjha')
def hjha():
    return render_template('hjha.html')

@app.route('/eitem')
def eitem():
    return render_template('eitem.html')


@app.route('/online')
# @sess_check
def online():
    return render_template('updata.html')


# for taiwan
@app.route('/tw')
def tw():
    return render_template('tw.html')


###### 比对开始


@app.route('/deploy', methods=['GET','POST'])
def deploy():
    if request.method == 'POST':
        diffitem = request.form['diffitem']
        diffsubitem = request.form['diffsubitem']
        #env = request.form['env']
        env = 'diff'
        print ''
        print diffitem, diffsubitem, env
        cmd = 'sh /auto/auto.sh'
        print cmd + ' -I ' + diffitem + ' -T '+ diffsubitem + ' -A ' + env
        cmdinfo = os.popen( cmd + ' -I ' + diffitem + ' -T ' + diffsubitem + ' -A ' + env ).read()
        #return  json.dumps({'diff':'ok', 'cmddiff':cmd})
        return  cmdinfo
       


@app.route('/pull', methods=['GET','POST'])
def pull():
    if request.method == 'POST':
        pullitem2 = request.form['pullitem']
        pullsubitem2 = request.form['pullsubitem']
        env = 'pull'
        cmd = 'sh /auto/auto.sh'
        print ''
        print cmd + ' -I ' + pullitem2 + ' -T ' + pullsubitem2 + ' -A ' + env
        print ''
        #cmdpull = os.popen(cmd + ' -I ' + pullitem2 + ' -T ' + pullsubitem2 + ' -A ' + env).read()
        cmdpull = subprocess.check_output(cmd + ' -I ' + pullitem2 + ' -T ' + pullsubitem2 + ' -A ' + env, shell=True)
        #cmdpull = subprocess.Popen([cmd + ' -I ' + pullitem2 + ' -T ' + pullsubitem2 + ' -A ' + env], shell=True, stdout=subprocess.PIPE).communicate()

        #print '/usr/bin/ansible ' + pullitem2 + '_' + pullsubitem2 + ' -m raw -a ' + "'" + '/bin/bash ' + '/home/tomcat/' + pullitem2 + '_' + pullsubitem2 + '.sh' + "'"

        #cmdpull += os.popen('/usr/bin/ansible ' + pullitem2 + '_' + pullsubitem2 + ' -m shell -a ' + "'" + '/bin/bash ' + '/home/tomcat/' + pullitem2 + '_' + pullsubitem2 + '.sh' + "'").read()
	#print cmdpull

        print '/usr/bin/ansible ' + pullitem2 + '_' + pullsubitem2 + ' -m shell -a ' + "'" + '/bin/bash ' + '/home/tomcat/' + pullitem2 + '_' + pullsubitem2 + '.sh' + "'"
        cmdpull += subprocess.check_output('/usr/bin/ansible ' + pullitem2 + '_' + pullsubitem2 + ' -m shell -a ' + "'" + '/bin/bash ' + '/home/tomcat/' + pullitem2 + '_' + pullsubitem2 + '.sh' + "'", shell=True)
        #cmdpull += subprocess.Popen(['/usr/bin/ansible ' + pullitem2 + '_' + pullsubitem2 + ' -m shell -a ' + "'" + '/bin/bash ' + '/home/tomcat/' + pullitem2 + '_' + pullsubitem2 + '.sh' + "'"], bufsize=1000, shell=True, stdout=subprocess.PIPE).communicate()

        return cmdpull


######## 发布开始


@app.route('/testfabu', methods=['GET','POST'])
def  testfabu():
    if request.method == 'POST':
        # EO3_
        s_item= request.form.get('testsenv')
        # unpull_t
        #test_seclet_pull = request.form.get('select_test_pull')
        test_seclet_pull = 'diff'
        # webuk
        subitem = request.form.get('zixiang')
        print ''
        print s_item,subitem,test_seclet_pull
        fabuinfo = 'Hi,我是测试发布！'
        ip = '192.168.1.204'
        cmd = 'sh /auto/three.sh-20150707'
        #print 'ssh tomcat@' + ip + ' ' + cmd + ' -I ' + s_item + ' -T ' + subitem + ' -P ' + test_seclet_pull + ' -A ' + 'upgrade'
        #fabuinfo = os.popen('ssh tomcat@' + ip + ' ' + cmd + ' -I ' + s_item + ' -T ' + subitem + ' -P ' + test_seclet_pull + ' -A  ' + 'upgrade' ).read()

        print 'ssh tomcat@' + ip + ' ' + cmd + ' -I ' + s_item + ' -T '+ subitem + ' -A ' + test_seclet_pull
        print ''
        fabuinfo = os.popen('ssh tomcat@' + ip + ' ' + cmd + ' -I ' + s_item + ' -T ' + subitem + ' -A ' + test_seclet_pull ).read()
        #return  json.dumps({'pull':'ok', 'fabuinfo':fabuinfo})
        return  fabuinfo


@app.route('/onlinefabu', methods=['GET','POST'])
def  onlinefabu():
    if request.method == 'POST':
        o_item = request.form.get('onlineenv')
        o_subitem = request.form.get('onlinezixiang')
        online_seclet_pull = request.form.get('select_online_pull')
        print ''
        print o_item, o_subitem, online_seclet_pull
        zhengshifabuinfo='gegwegwegwergergergergergege'
        ip = '192.168.1.204'
        cmd = 'sh /auto/three.sh-20150707'
        print 'ssh tomcat@' + ip + ' ' + cmd + ' -I ' + o_item + ' -T ' + o_subitem + ' -P ' + online_seclet_pull + ' -A ' + 'upgrade'
        print ''
        #zhengshifabuinfo = os.popen('ssh tomcat@' + ip + ' ' + cmd + ' -I ' + o_item + ' -T ' + o_subitem + ' -P ' + online_seclet_pull + ' -A ' + 'upgrade').read().strip('\n')
        zhengshifabuinfo = os.popen('ssh tomcat@' + ip + ' ' + cmd + ' -I ' + o_item + ' -T ' + o_subitem + ' -P ' + online_seclet_pull + ' -A ' + 'upgrade').read()
        #return  json.dumps({'pull':'ok', 'zhengshifabuinfo':zhengshifabuinfo})


        print 'ssh tomcat@' + ip + ' ' + '"' + '/usr/bin/ansible ' + o_item + '_' + o_subitem + ' -m shell -a ' + "'" + '/bin/bash ' + '~/' + o_item + '_' + o_subitem + '.sh' + "'" + '"'
        zhengshifabuinfo += os.popen('ssh tomcat@' + ip + ' ' + '"' + '/usr/bin/ansible ' + o_item + '_' + o_subitem + ' -m shell -a ' + "'" + '/bin/bash ' + '~/' + o_item + '_' + o_subitem + '.sh' + "'" + '"').read()
        return zhengshifabuinfo


## CDN
#@app.route('/onlinefabu', methods=['GET','POST'])
#def  onlinefabu():
#    if request.method == 'POST':
#        o_item = request.form.get('onlineenv')
#        o_subitem = request.form.get('onlinezixiang')
#        cdn_ip = request.form.get('cdnSource')
#        print o_item, o_subitem, cdn_ip
#
        #print 'ssh tomcat@' + ip + ' ' + '"' + '/usr/bin/ansible ' + o_item + '_' + o_subitem + ' -m shell -a ' + "'" + '/bin/bash 
        # + o_item + '_' + o_subitem + '.sh' + "'" + '"'
        #zhengshifabuinfo += os.popen('ssh tomcat@' + ip + ' ' + '"' + '/usr/bin/ansible ' + o_item + '_' + o_subitem + ' -m shell         #" + '/bin/bash ' + '~/' + o_item + '_' + o_subitem + '.sh' + "'" + '"').read()
        #return zhengshifabuinfo
        #return zhengshifabuinfo2



@app.route('/huigun', methods=['GET','POST'])
def  huigun():
    if request.method == 'POST':
        roll_seclet_pull = request.form.get('select_roll')
        print roll_seclet_pull
        roll_ver = request.form.get('roll_ver')
        print roll_ver
    return  render_template('updata.html')


@app.route('/cdn', methods =['GET','POST'])
def cdn():
    return  render_template('cdn.html')


@app.route('/restart', methods =['GET','POST'])
def restart():
    if request.method == 'POST':
        ipadd = request.get_data()
        ip =  re.compile('[0-9]+(?:\.[0-9]+){3}').findall(ipadd)
        str_ip = ''.join(ip)
        # print 'python ssh.py '+ip
        # restartinfo = os.popen('python ssh.py '+ip).read()
        # print restartinfo
        print str_ip
        print 'python ssh.py '+str_ip
        restartinfo = os.popen('python ssh.py '+str_ip).read()
        return restartinfo


@app.route('/testStart', methods=['GET','POST'])
#@auth.login_required
def  testStart():
    if request.method == 'POST':
        ipaddr = request.form['retartId']
        print " python  ssh_shutdown.py '+ipaddr+ '&& sleep 4 ; python  ssh_start.py '+ipaddr'"
        restartinfo = os.popen('python  ssh_shutdown.py '+ipaddr+ '&& sleep 4 ; python  ssh_start.py '+ipaddr).read()
        return  restartinfo


@app.route('/searchLog', methods=['GET','POST'])
def  searchLog():
    if request.method == 'POST':
        ipaddr = request.form['logId']
        print 'python  ssh_log.py '+ipaddr
        loginfo = os.popen('python  ssh_log.py '+ipaddr).read()
        return  loginfo


@app.route('/go')
def go():
#    for element in watchlist:
#        urls = element.get('urls')
#        if urls:
#            for url in urls:
#                print url
#                try:
#                    r = requests.get(url.get('url', ''),headers=element.get('headers', ''))
#                   
#                    url['status'] = r.status_code
#
#                except AttributeError:
#                    r = requests.get(url, headers=element.get('headers', ''))
#                    index = urls.index(url)
#                    urls[index] = {'url': url}
#                    urls[index]['status'] = r.status_code
#                    print urls[index]
#
#    context = {
#        'watchlist': watchlist,
#    }
#    return render_template('go.html', **context)
    return render_template('go.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect('/')


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)

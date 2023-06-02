from flask import Flask, render_template,request,redirect,url_for #追加
from bbsthread import Thread as bbst
from bbsthread import Post as bbpos
import bbsystem
import datetime

app = Flask(__name__)

global bbs
bbs=bbsystem.BBS()
bbs.load_threads()
#bbs.make_top_page()

@app.route('/')
def bbstop():
    #return name
    return render_template('index.html', title='Orca bbs-top',
                           bbsname="Orca BBS",
                           listname="List of thread",
                           threads=bbs.list_threads)

@app.route('/threads/<tid>',methods=["GET","POST"])
def threadpage(tid):
    if request.method=="POST":
        name=request.form['name']
        content=request.form['content']
        DIFF_JST_FROM_UTC = 9
        log_time=(datetime.datetime.utcnow())\
        +datetime.timedelta(hours=DIFF_JST_FROM_UTC)
        log_time=str(log_time)
        ps=bbpos("fakeuid",name,log_time,content)
        bbs.map_threads[tid].add_post(ps)
        bbs.map_threads[tid].save()
    
    return render_template('thread.html',
                           title=bbs.map_threads[tid].name,
                           posts=bbs.map_threads[tid].posts,tid=tid)

@app.route('/new_thread',methods=["GET","POST"])
def new_thread():
    if request.method=="POST":
        thread_title=request.form["thread_title"]
        posters_name=request.form["posters_name"]
        content=request.form["content"]
        DIFF_JST_FROM_UTC = 9
        log_time=(datetime.datetime.utcnow())\
        +datetime.timedelta(hours=DIFF_JST_FROM_UTC)
        log_time=str(log_time)
        th=bbst(thread_title)
        ps=bbpos('fake_uid',posters_name,log_time,content)
        bbs.add_threads(th,bbs.alloc_new_tid())
        th.add_post(ps)
        th.save()
        return redirect(url_for('bbstop'))
    return render_template('new_thread.html', title='Post new thread')

## おまじない
if __name__ == "__main__":
    app.run(debug=False)

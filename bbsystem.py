import random
import bbsthread
import json
class BBS:
    def __init__(self):
        self.list_threads=[]
        self.map_threads={}
    def alloc_new_tid(self):
        while(1):
            s=""
            for i in range(15):
                s=s+str(random.randint(0,10))
            if not(s in self.map_threads):
                break
        return s
    def add_threads(self,th:bbsthread.Thread,tid):
        self.map_threads[tid]=th
        th.reg_tid(tid)
        self.list_threads.append(th)
    def save_thread(self,th:bbsthread.Thread):
        with open("threads/{}.json".format(th.tid),"w") as j:
            json.dump(th.get_dict(),j)
    def make_top_page(self):
        f=""
        for thread in self.list_threads:
            f=f+'''
<tr>
    <td bgcolor="#000044"><font color="#FFFFFF"><a href="threads/{}">
    <font color="#FFFF00">{}</font></a></font></td>
    <td bgcolor="#000044"><font color="#FFFFFF">{}</font></td>
    <td bgcolor="#000044"><font color="#FFFFFF">{}</font></td>
</tr>
            '''.format(thread.tid,thread.name,len(thread.posts),"0000/00/00 00:00")

        s=r'''
{% extends "index_pre.html" %}
{% block content %}
<table border="1" width="50%" style="table-layout: fixed;">
<tr>
<th bgcolor="#000044"><font color="#FFFFFF">タイトル</font></th>
<th bgcolor="#000044"><font color="#FFFFFF">レス数</font></th>
<th bgcolor="#000044"><font color="#FFFFFF">作成日時</font></th>
</tr>'''+f+r'''
</table>
{% endblock %}'''
        with open("templates/index.html","w") as o:
            o.write(s)        
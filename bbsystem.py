import random
import bbsthread
import json
import os
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
    def load_threads(self):
        tids=[jn.replace(".json","") for jn in os.listdir("threads")]
        for tid in tids:
            with open("threads/{}.json".format(tid),"r") as f:
                dct=json.load(f)
            th=bbsthread.Thread("unknown").from_dict(dct)
            self.add_threads(th,tid)
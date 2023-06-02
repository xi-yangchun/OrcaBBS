import json
class Thread:
    def __init__(self,name):
        self.name=name
        self.tid=""
        self.posts=[]
        self.num_posts=0
        self.uid="unknown"
        self.time="time_hidden"
        self.poster="anonymous"
    def check_cond_post(self,post):
        return True
    def add_post(self,ps):
        if len(self.posts)==0:
            self.time=ps.time
            self.uid=ps.uid
            self.poster=ps.name
        self.posts.append(ps)
        self.num_posts+=1
        ps.num=str(len(self.posts))
        doma=['>>{}'.format(1000-i) for i in range(1000)]
        for i in range(1000):
            if doma[i] in ps.content:
                ps.content=ps.content.replace(doma[i],'>>0000'+str(1000-i))
                ps.add_anchor_to(1000-i)
        ps.content=ps.content.replace('>>0000','>>')
    def reg_tid(self,tid):
        self.tid=tid
    def get_dict(self):
        d={   
            "thread_title":self.name,
            "thread_id":self.tid,
            "uid":self.uid,
            "poster":self.poster,
            "time":self.time,
            "num_posts":self.num_posts,
            "posts":[
                post.get_dict() for post in self.posts
            ]            
        }
        return d
    def save(self):
        d=self.get_dict()
        with open("threads/{}.json".format(self.tid),"w") as j:
            json.dump(d,j,indent=4)
    def from_dict(self,dct):
        self.name=dct["thread_title"]
        self.tid=dct["thread_id"]
        self.uid=dct["uid"]
        self.poster=dct["poster"]
        self.time=dct["time"]
        self.num_posts=int(dct["num_posts"])
        self.posts=[]
        for i in range(self.num_posts):
            self.posts.append(Post(0,0,0,0).from_dict(dct["posts"][i]))
        return self

class Post:
    def __init__(self,uid,name,time,content):
        self.num=-1
        self.uid=uid
        self.name=name
        self.time=time
        self.content=content
        self.anchor_to=[]
        self.anchor_from=[]
    def add_anchor_to(self,number):
        self.anchor_to.append(number)
    def get_dict(self):
        d={
            "num":self.num,
            "uid":self.uid,
            "name":self.name,
            "time":self.time,
            "content":self.content,
            "anchor_to":[ato for ato in self.anchor_to],
            "anchor_from":[afr for afr in self.anchor_from]
        }
        return d
    def from_dict(self,dct):
        self.num=int(dct["num"])
        self.uid=dct["uid"]
        self.name=dct["name"]
        self.time=dct["time"]
        self.content=dct["content"]
        self.anchor_to=[int(dct["anchor_to"][i]) 
                        for i in range(len(dct["anchor_to"]))]
        self.anchor_from=[int(dct["anchor_from"][i]) 
                        for i in range(len(dct["anchor_from"]))]
        return self
#coding=utf-8
from __future__ import annotations

'''
if_an=False
try:
    from tqdm import tqdm
    import requests
    from retry import retry
    import multitasking
except ImportError as e:
    print("Cant found pack.download now.")
    try:
        import pip
        pip.main(["install","retry","requests","tqdm","multitasking"])
        if_an=True
    except ImportError:
        print("Cant import pip pack.You can: pip install tqdm requests retry multitasking")
        exit(1)
    except Exception as ee:
        print(ee)
        exit(1)
if if_an:
    try:
        from tqdm import tqdm
        import requests
        from retry import retry
        import multitasking
    except ImportError:
        print("Cant import pip pack.You can: pip install tqdm requests retry multitasking")
        exit(1) 
'''

from tqdm import tqdm
from retry import retry
import requests,os,multitasking,signal,json

class Easy_Download(object):
    MB = 1024**2
    
    def __init__(self,BASE_DIR,WEB_ROOT,headers=None):
        signal.signal(signal.SIGINT, multitasking.killall)
        if headers==None:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
            }
        else:
            self.headers = headerserror_c=0
            
        self.DOWNLIST=[]

        print("Easy Download Setup ...")
        print("Will down this dir:",BASE_DIR)

        self.download(WEB_ROOT+"list.json", os.path.join(BASE_DIR,"list.json"))
        with open(os.path.join(BASE_DIR,"list.json"),"r") as fp:
            DOWNLIST=json.loads(fp.read())
        print("Get from",WEB_ROOT,",file count:",len(DOWNLIST))
        print("----------------------------------------")

        for i in DOWNLIST:
            try:
            # print(WEB_ROOT+i[0],os.path.join(BASE_DIR,i[1]))
                self.download(WEB_ROOT+i[0],os.path.join(BASE_DIR,i[1]))
            except Exception as e:
                error_c+=1
                print("Error but catch",e)
                
        print("----------------------------------------")
        print("ok...")
        print("But Error count:",error_c)
    
    def split(self,start,end,step):
        parts = [(start, min(start+step, end))
                for start in range(0, end, step)]
        return parts
    
    def get_file_size(self,url,raise_error=True):
        response = requests.head(url)
        file_size = response.headers.get('Content-Length')
        if file_size is None:
            if raise_error is True:
                raise ValueError('ERROR NOT Length')
            return file_size
        return int(file_size)
    
    def download(self,url,file_name,retry_times=3,each_size=16*1024**2):# MB=1024**2
        f=None
        try:
            f = open(file_name, 'wb')
        except FileNotFoundError as e:
            os.makedirs(os.path.dirname(file_name))
            f = open(file_name, 'wb')
        file_size = self.get_file_size(url)
    
        @retry(tries=retry_times)
        @multitasking.task
        def start_download(start: int, end: int) -> None:
            _headers = self.headers.copy()
            _headers['Range'] = f'bytes={start}-{end}'
            response = session.get(url, headers=_headers, stream=True)
            chunk_size = 128
            chunks = []
            for chunk in response.iter_content(chunk_size=chunk_size):
                chunks.append(chunk)
                bar.update(chunk_size)
            f.seek(start)
            for chunk in chunks:
                f.write(chunk)
            del chunks
        session = requests.Session()
        each_size = min(each_size, file_size)
        parts = self.split(0, file_size, each_size)
        file_nameee=os.path.basename(file_name)
        bar = tqdm(total=file_size, desc=f'download file:{file_nameee}')
        for part in parts:
            start, end = part
            start_download(start, end)
        multitasking.wait_for_tasks()
        f.close()
        bar.close()
    
if __name__ == "__main__":
    # In server you can 'python -m http.server {port}'
    Easy_Download("/example/","http://example.com/")

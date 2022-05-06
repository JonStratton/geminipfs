#!env python3
import subprocess, re, requests
from gemeaux import App, Handler, TextResponse, DocumentResponse, NotFoundResponse
# Simple gemini wrapper around IPFS. If there is no local version, it will attempt to get files from ipfs.io.
# pip install -r requirements.txt
# openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem -subj "/CN=localhost" -addext "subjectAltName=IP:127.0.0.1"

clean_path = re.compile(r"[^A-Za-z0-9/.-]+")
remove_prefex = re.compile(r"^/ipfs/")
ipfs_local = 0
ipfs_remote_url = 'https://ipfs.io/ipfs/%s'

class IPFSHandler(Handler):
   def get_response_local(self, path):
      ipfs_cmd = 'ipfs cat %s' % path
      ipfs_return = ''
      # TODO, deal with binary files
      p = subprocess.Popen(ipfs_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      for line_bytes in p.stdout.readlines():
         ipfs_return = ipfs_return + line_bytes.decode('utf-8')
      retval = p.wait
      return TextResponse(path, ipfs_return)

   def get_response_remote(self, path):
      request_url = ipfs_remote_url % path
      ipfs_response = requests.get(request_url)
      return TextResponse(request_url, ipfs_response.content.decode('utf-8'))

   def handle(self, url, path):
      path = clean_path.sub("", path)
      path = remove_prefex.sub("", path)
      if ipfs_local:
         response = self.get_response_local(path)
      else:
         response = self.get_response_remote(path)
      return response

if __name__ == "__main__":
   try:
      subprocess.call(['ipfs', '--version'])
      ipfs_local = 1
   except FileNotFoundError:
      print("local ipfs not found. Using %s for content." % ipfs_remote_url)

   urls = {
      "/ipfs": IPFSHandler(),
      "": NotFoundResponse("Not Found"),
   }
   app = App(urls)
   app.run()

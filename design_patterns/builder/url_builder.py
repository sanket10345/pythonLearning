"""
URLBuilder - Used to create URL objects given some parameters.

This builder pattern helps in constructing a well-formed URL step-by-step.
It supports both essential and optional components of a URL.

Example URL:
  https://mywebsite:8080/companies?companyName=xyz

Parts of the URL:
  - Protocol      (Optional, default = "http")
  - Hostname      (Essential) ❗ Must be set before using the URL
  - Port          (Optional)
  - Path Param    (Optional)
  - Query Param   (Optional)

If hostname is not set, a ValueError will be raised when trying to build the URL.
"""

class urlBuilder:
    def __init__(self):
        self.protocol = "http"
        self.domain = ""
        self.port = None
        self.path = ""
        self.params = {}
    def set_protocol(self,protocol):
        self.protocol = protocol
        return self

    def set_domain(self,domain):
        self.domain = domain
        return self

    def set_port(self,port):
        self.port = port
        return self

    def set_path(self,path):
        self.path = path
        return self

    def add_param(self,key,value):
        self.params[key] = value
        return self

    def build(self):
        if not self.domain:
            raise ValueError("Domain must be specified before building the URL.")
        
        url = f'{self.protocol}://{self.domain}'
        
        if self.port:
            url += f':{self.port}'
        if self.path:
            url += f'/{self.path}'
        if self.params:
            query_string = "&".join(f"{k}={v}" for k, v in self.params.items())
            url += f'?{query_string}'
        return url

    def __str__(self):
        return self.build()
    
builder = urlBuilder()
url = (builder
       .set_protocol("https")
       .set_domain("example.com")
       .set_port(8080)
       .set_path("search")
       .add_param("query", "python")
       .add_param("category", "programming")
       .add_param("sort_by", "relevance")
       .add_param("page", "1"))

print(url)   
    


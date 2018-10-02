from Pendings.PendingsRequest import PendingsRequest
from Utils.Services import Services

class Pendings(Services):
    def __init__(self, url, token = None, user = None, password = None):
        super(Pendings,self).__init__(url, token, user, password)
    
    def pendings(self, rfc):
        return PendingsRequest.pendingsbyRfc(self.url, self.token, rfc)
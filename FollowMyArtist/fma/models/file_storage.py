'''
Created on Mar 24, 2016

@author: TBener
'''
from django.core.files.storage import Storage 

class AppEngineBlobStorage(Storage):

    def exists(self, name):
        pass

    def size(self, name):
        pass

    def url(self, name):
        pass

    def delete(self, name):
        pass

    def listdir(self, path):
        raise NotImplementedError()
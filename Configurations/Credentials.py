from configparser import ConfigParser

baseDir = 'Configurations/Credentials.ini'

class HereConf:
    def __init__(self):
        self._cfg = ConfigParser()
        self._cfg.read(baseDir)
        self._appId = self._cfg['HERE']['appId']
        self._appCode = self._cfg['HERE']['appCode']

    @property
    def appId(self):
        return self._appId

    @property
    def appCode(self):
        return self._appCode

class UberConf:
    def __init__(self):
        self._cfg = ConfigParser()
        self._cfg.read(baseDir)
        self._serverToken = self._cfg['UBER']['serverToken']

    @property
    def serverToken(self):
        return self._serverToken

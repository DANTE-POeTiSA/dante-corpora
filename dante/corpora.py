import pandas as pd
import pkg_resources

class Dante():

    def __init__(self, option):
        self.pos = option
        self.base = option
        self.freq = option
        self.freq_indi = option
        self.freq_tweet = option


    def __str__(self):
        return self.pos


    @property
    def pos(self):
        return self._pos


    @pos.setter
    def pos(self, option):
        try:
            path = pkg_resources.resource_filename(__name__, f'data/{option}/POS.conllu')
            with open(path, 'r', encoding='utf-8') as f:
                data = f.read()
            self._pos = data
        except FileNotFoundError:
            print('Arquivo nao encontrado! Verifique se o valor passado esta em [...]')


    @property
    def base(self):
        return self._base


    @base.setter
    def base(self, option):
        try:
            path = pkg_resources.resource_filename(__name__, f'data/{option}/base.csv')
            self._base = pd.read_csv(path, encoding='utf-8')
        except FileNotFoundError:
            print('Arquivo nao encontrado! Verifique se o valor passado esta em [...]')


    @property
    def freq(self):
        return self._freq


    @freq.setter
    def freq(self, option):
        try:
            path = pkg_resources.resource_filename(__name__, f'data/{option}/base.csv')
            self._freq = pd.read_csv(path, encoding='utf-8')
        except FileNotFoundError:
            print('Arquivo nao encontrado! Verifique se o valor passado esta em [...]')


    @property
    def freq_indi(self):
        return self._freq_indi


    @freq_indi.setter
    def freq_indi(self, option):
        try:
            path = pkg_resources.resource_filename(__name__, f'data/{option}/base.csv')
            self._freq_indi = pd.read_csv(path, encoding='utf-8')
        except FileNotFoundError:
            print('Arquivo nao encontrado! Verifique se o valor passado esta em [...]')


    @property
    def freq_tweet(self):
        return self._freq_tweet


    @freq_tweet.setter
    def freq_tweet(self, option):
        try:
            path = pkg_resources.resource_filename(__name__, f'data/{option}/base.csv')
            self._freq_tweet = pd.read_csv(path, encoding='utf-8')
        except FileNotFoundError:
            print('Arquivo nao encontrado! Verifique se o valor passado esta em [...]')        
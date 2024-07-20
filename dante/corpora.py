import pandas as pd
import pkg_resources

class Dante():

    def __init__(self, corpus):
        self.corpora = ['dantestocks', 'danteshots']
        self.corpus = corpus


    @property
    def corpus(self):
        return self._corpus
    
    
    @corpus.setter
    def corpus(self, corpus):
        try:
            print(f'Returning {corpus} corpus.')
            self._corpus = corpus
        except FileNotFoundError:
            print(f'Wasn\'t able to find "{corpus}" named corpus. Check documentation on: https://pypi.org/project/dante-corpora/')
            self._corpus = None


    def get_data(self, filename):
        try:
            path = pkg_resources.resource_filename(__name__, f'data/{self.corpus}/{filename}.csv')
            return pd.read_csv(path, encoding='utf-8', low_memory=False)
        except FileNotFoundError:
            print(f'Wasn\'t able to find "{filename}" named file inside "{self.corpus}". Check documentation on: https://pypi.org/project/dante-corpora/')
            return False
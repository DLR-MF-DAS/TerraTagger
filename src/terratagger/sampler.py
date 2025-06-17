import random

class RandomItemSampler:
    def __init__(self, datasource):
        self.datasource = datasource

    def get(self):
        return random.choice(self.datasource)

if __name__ == '__main__':
    pass

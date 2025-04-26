



class RepoClassifier:
    def __init__(self, model):
        # model has to be an sklearn model
        self.name = str(model)
        self.model = model

    def train(self, training_vectors: list, training_labels: list):
        pass

    def predict(self, repo):
        return 0
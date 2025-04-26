from repo2vec import Repo2Vec


class DirectoryStructureVectorizer:
    """This uses Repo2Vec, a vectorizer proposed by Rokon et al in [doi.org/10.1109/ICSME52107.2021.00038]
    """

    def __init__(self):
        self.name = "DirectoryStructureVectorizer"
        self.vectors = list()

    def vectorize(self, repo_paths: list):
        for repo_path in repo_paths:
            repo2vec = Repo2Vec(
                repo_path,
                vector_size=128,
                combination_method='weighted_sum',
                weights=(1, 1, 1),  # wieghts for metadata, structural data, and source vectors
                normalize=True
            )

            self.vectors.add(repo2vec.generate_embedding())
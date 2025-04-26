from sklearn.linear_model import LogisticRegression

from vectorizer import DirectoryStructureVectorizer as ds_vect
from model import RepoClassifier




repo_paths = []


def main():
    vectorizers = [ds_vect]
    models = [LogisticRegression]

    for vectorizer in vectorizers:
        vectors = vectorizer.vectorize(repo_paths)

        # need to split training / testing data

        for model in models:
            classifier = RepoClassifier(model)
            classifier.train()  # insert training set
            results = classifier.predict() # insert test set









if __name__ == "__main__":
    main()
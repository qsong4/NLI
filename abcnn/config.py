class Config(object):

    def __init__(self):
        self.embedding_size = 128  # 词向量维度
        self.l2_lambda = 0.004
        self.lr = 0.05
        self.K = 2

        self.epoch = 20
        self.Batch_Size = 256

        self.train_data = "data/train.txt"
        self.dev_data = "data/dev.txt"
        self.vocab_path = "save_model/abcnn/vocab.pickle"
        self.model_path = "/abcnn/save_model/abcnn/"
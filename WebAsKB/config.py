import os

import warnings

warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=RuntimeWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)


class Config:
    def __init__(self):
        # Neural param
        self.LR = 0.007
        self.ADA_GRAD_LR_DECAY = 1e-6
        self.ADA_GRAD_L2 = 3e-4
        self.MAX_LENGTH = 28
        self.NUM_OF_ITER = 1000000
        self.hidden_size = 512
        self.NUM_OF_SAMPLES = None
        self.TEST_TRAIN_SPLIT = 0.9
        self.print_every = 1000
        self.evaluate_every = 3000
        self.dropout_p = 0.25
        self.EMBEDDING_VEC_SIZE = 50
        self.MINI_BATCH_SIZE = 10
        self.output_size = 29
        self.use_teacher_forcing = True
        self.teacher_forcing_full_until = 10000
        self.teacher_forcing_partial_until = 30000

        # used to limit size of dev set when training
        self.max_evalset_size = 4000

        # Number of training iteration with no substantial dev accuracy improvement to stop training ("early stopping")
        self.NO_IMPROVEMENT_ITERS_TO_STOP = 50000

        # manual seeding for run comparison

        self.SOS_token = 0
        self.EOS_token = 1

        # Neural Options
        self.use_cuda = False
        self.USE_GLOVE = True
        self.LOAD_SAVED_MODEL = True
        self.PERFORM_TRAINING = False

        # choose dev or test
        self.EVALUATION_SET = 'train'

        # Stanford NLP
        os.environ["CLASSPATH"] = "Lib/stanford-ner-2016-10-31"
        os.environ["STANFORD_MODELS"] = "Lib/stanford-ner-2016-10-31/classifiers"
        self.StanfordCoreNLP_Path = 'http://127.0.0.1:9003'

        # Paths
        self.data_dir = '../../data/'
        self.complexwebquestions_dir = self.data_dir
        self.noisy_supervision_dir = self.data_dir + 'noisy_supervision/'
        self.golden_supervision_dir = self.data_dir
        self.neural_model_dir = self.data_dir + "ptrnet_model/"
        self.split_points_dir = self.data_dir + "split_points/"
        self.rc_answer_cache_dir = self.data_dir + "RC_answer_cache/"

        # Data
        self.glove_50d = self.data_dir + "embeddings/glove/glove.6B.50d.txt.zip"
        self.glove_300d_sample = self.data_dir + "embeddings/glove/glove.sample.300d.txt.zip"

        # question decomp settings
        self.use_my_decomp = True
        self.split_model = 'golden'
        self.my_rc_answer_dir = self.data_dir + 'rc_ans/'
        self.my_decomp_res_dir = self.data_dir + 'split_res/'


config = Config()

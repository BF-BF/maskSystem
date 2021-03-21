from business.spider import spider
from business.analyze import dataAnalyse

class getAll:
    def get_all_comments(self):
        all_comments = spider.main()
        return all_comments

    def get_all_pos_nav(self):
        all_pos_com, all_nav_com = dataAnalyse.snownlp(self.get_all_comments())
        return all_pos_com, all_nav_com

    def get_stopwords(self):
        stopwords = dataAnalyse.stopwords_list()
        return stopwords

    def get_all_tokens(self):
        all_tokens = dataAnalyse.tokenize(self.get_all_comments(), self.get_stopwords())
        return all_tokens

    def get_all_tfs(self):
        all_word_tf = dataAnalyse.tf(self.get_all_tokens())
        return all_word_tf

    def get_all_adj_words(self):
        all_adj_words = dataAnalyse.adj_words(self.get_all_comments())
        return all_adj_words

    def get_all_keywords(self):
        all_keywords = dataAnalyse.keywords(self.get_all_comments(), self.get_all_adj_words())
        return all_keywords

    def get_all_topics(self):
        all_na_tokens = dataAnalyse.pos_tag(self.get_all_comments(), self.get_stopwords())
        all_theme = dataAnalyse.model_train(all_na_tokens)  # [["a b c", "a b", ,],[]]
        return all_theme

    def get_all_bigram(self):
        all_word_pairs = dataAnalyse.bigrams(self.get_all_tokens(), self.get_all_topics())
        return all_word_pairs

    def get_all_wc(self):
        dataAnalyse.make_word_cloud(self.get_all_bigram())

    def get_all_urls(self):
        all_urls = ['spm=a230r.1.14.21.7b4335196NzEiX&id=18483428998&ns=1&abbucket=13',
                    'spm=a230r.1.14.24.49f375e4mI6ddC&id=605448737579&ns=1&abbucket=13',
                    'spm=a230r.1.14.4.40b11ceevoa1sF&id=594932506002&cm_id=140105335569ed55e27b&abbucket=13&skuId=4208889372980',
                    'spm=a230r.1.14.41.64b65a64qpga5m&id=581410608410&ns=1&abbucket=13&skuId=4652075570735',
                    'id=638462715559&rn=be9c638af777b3394e6ea648fb8c2449&abbucket=14&skuId=4572926728991&ali_trackid=41_ce44b731353c3b151db89b7045bf28c5',
                    'tbpm=1&spm=a220m.1000858.1000725.1.1ff81b34D9po82&id=605441157623&skuId=4651184946686&user_id=2095455386&cat_id=2&is_b=1&rn=52a187cf4401dbad711e5041a3ecc1ac',
                    'tbpm=1&spm=a230r.1.14.20.641461d0sGIXJ8&id=620965870548&ns=1&abbucket=13',
                    'id=616567613998&rn=25c1cd122c7ce43ef7c176d8c5ed58e0&abbucket=19&ali_trackid=41_7163d933aa003fdc55c18bb0e1959909',
                    'spm=a1z10.3-b-s.w4011-21158210945.45.5692547ejmRzp6&id=583184933292&rn=4407f8bee01e7856dc2b5b58c3f5a307&abbucket=11',
                    'id=535576218349&ali_refid=a3_430583_1006:1123665977:N:FyISXVpvFt4SAyB42sotmUSUinzIusZP:7da03c856d976741e8116863f15bb1aa&ali_trackid=1_7da03c856d976741e8116863f15bb1aa&spm=a230r.1.14.3&skuId=3194939939638',
                    ]
        return all_urls




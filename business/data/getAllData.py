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
        all_urls = ['id=523027819179&ali_refid=a3_430673_1006:1105793915:N:8k/7QsyIQJ89zxL475o00USUinzIusZP:99529ed8649466beb36032688270e640&ali_trackid=1_99529ed8649466beb36032688270e640&spm=a2e0b.20350158.31919782.5',
                    'id=42861838038&ali_refid=a3_430673_1006:1104952529:N:HZYGzM8vo2blJiR1o+vpUUSUinzIusZP:1ac61ad2677f4d7252b8254ca2f46fde&ali_trackid=1_1ac61ad2677f4d7252b8254ca2f46fde&spm=a2e0b.20350158.31919782.1&skuId=4552389392977',
                    'id=539339147058&ali_refid=a3_430673_1006:1105528571:N:6qxlEW5rFIdJJsVnkmjCIUSUinzIusZP:7023b66802ce73957a93752070d73649&ali_trackid=1_7023b66802ce73957a93752070d73649&spm=a2e0b.20350158.31919782.1&skuId=4571541867149',
                    'id=536104696285&ali_refid=a3_430673_1006:1122585386:N:XJriWrvBZgp9ipngvt+LZESUinzIusZP:1c02cf8b5fa97dbf97d030b2405a9860&ali_trackid=1_1c02cf8b5fa97dbf97d030b2405a9860&spm=a2e0b.20350158.31919782.4',
                    'id=534305594544&ali_refid=a3_430673_1006:1110409601:N:OxuEkPHuTPfjuvCQ5QZ5S0SUinzIusZP:e7211e2ff56ef105a82baf0f2888584d&ali_trackid=1_e7211e2ff56ef105a82baf0f2888584d&spm=a2e0b.20350158.31919782.1',
                    'id=576644195365&ali_refid=a3_430673_1006:1103099510:N:OQnAsDqYnQkn6jTHhWtXhUSUinzIusZP:84dee084209101a9fe0e009604f9b029&ali_trackid=1_84dee084209101a9fe0e009604f9b029&spm=a2e0b.20350158.31919782.1',
                    'id=525872510577&ali_refid=a3_430673_1006:1121503846:N:ng+zQao7EfPumsSx3ebnaJkHA1NUJuCB:2005b41f36548e9e995506da190a5434&ali_trackid=1_2005b41f36548e9e995506da190a5434&spm=a2e0b.20350158.31919782.2&skuId=4490239723187',
                    'tbpm=1&spm=a220m.1000858.1000725.1.371f3471q1q1RB&id=553133804175&skuId=3561268215125&user_id=2549841410&cat_id=2&is_b=1&rn=71b918a184271fe74e4430809b992bd0',
                    'id=577145913309&ali_refid=a3_430673_1006:1195910182:N:wJNY9SWnAU/jPWl4UWjgpUSUinzIusZP:45076d634b28fa0f401585773fbd7c6c&ali_trackid=1_45076d634b28fa0f401585773fbd7c6c&spm=a2e0b.20350158.31919782.2',
                    'spm=a220m.1000858.1000725.2.7d3b54cf6s50QP&id=608104972592&user_id=2095455386&cat_id=2&is_b=1&rn=34f44b657f8ad46621a822be39db4e25',
                    'id=545473839106&ali_refid=a3_430673_1006:1125371784:N:m0QM1lB3EvzwzedRQYMHn0SUinzIusZP:bbd88c8c117fbf4f2ab6769ce4ce07ab&ali_trackid=1_bbd88c8c117fbf4f2ab6769ce4ce07ab&spm=a2e0b.20350158.31919782.1&skuId=3486289911663',
                    'id=606623539943&ali_refid=a3_430673_1006:1227310051:N:a5hCO4LAAkikS9whmxVhMESUinzIusZP:3d4d1aebdadc1a6304934ac43f5534f1&ali_trackid=1_3d4d1aebdadc1a6304934ac43f5534f1&spm=a2e0b.20350158.31919782.3',
                    'id=544309421928&ali_refid=a3_430673_1006:1124976736:N:fLlmd8SOMTwgrKb8X/87EzApQaLNGNfa:9ff9d0442548002f6d9b2616d8ff6190&ali_trackid=1_9ff9d0442548002f6d9b2616d8ff6190&spm=a2e0b.20350158.31919782.2',
                    'id=577801645059&ali_refid=a3_430673_1006:1124725300:N:LYPDjVb5DbbUrmFQpQ5p10SUinzIusZP:7791375f38d2a3763c8a3af164b8ece6&ali_trackid=1_7791375f38d2a3763c8a3af164b8ece6&spm=a2e0b.20350158.31919782.1',
                    'id=15657673602&ali_refid=a3_430673_1006:1104596492:N:TwkYivj/bnUNRuGi27DTEQ==:f744941f70be336021edb284fb8333ca&ali_trackid=1_f744941f70be336021edb284fb8333ca&spm=a2e0b.20350158.31919782.1&skuId=3113269370027',
                    ]
        return all_urls




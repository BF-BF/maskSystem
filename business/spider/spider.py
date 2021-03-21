import requests
import re
import time

filename = ['E:\\backend\\business\\comments\\yunifang',
            'E:\\backend\\business\\comments\\yiyezi',
            'E:\\backend\\business\\comments\\zirantang',
            'E:\\backend\\business\\comments\\queling',
            'E:\\backend\\business\\comments\\dijiating',
            'E:\\backend\\business\\comments\\olaiya',
            'E:\\backend\\business\\comments\\meidihuier',
            'E:\\backend\\business\\comments\\chunyu',
            'E:\\backend\\business\\comments\\erjia',
            'E:\\backend\\business\\comments\\jm',
            'E:\\backend\\business\\comments\\keyanshi',
            'E:\\backend\\business\\comments\\gelai',
            'E:\\backend\\business\\comments\\leishi',
            'E:\\backend\\business\\comments\\swisse',
            'E:\\backend\\business\\comments\\lanzhi',
            ]

# request url的response
class Spider():
    def url_info(self, cookie, itemId, sellerId, page_num):
        url = "https://rate.tmall.com/list_detail_rate.htm"
        header = {
            "cookie": cookie,
            "referer": "https://detail.tmall.com/item.htm",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        }
        # 必带信息
        params = {
            "itemId": itemId,          # 商品id
            "sellerId": sellerId,
            "currentPage": page_num,   # 页码
        }

        req = requests.get(url, params, headers=header).content.decode('utf-8')[12:-1]

        # 因为response太大，不能直接使用json的loads()加载，这里用一个文本先储存着
        with open('response.txt', 'w', encoding='utf8') as f_res:
            f_res.write(req)

    def get_info(self):
        cookie = ["lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=cmLVB0qRmq32S37svZ_aCFqt_IEAZp6Gdz5Fm3xk9JwIOTIciSyOZbwOa1WKrif..; l=eBOiEkiqjTguzO4hBOfwhurza77OhIRAguPzaNbMiOCPO3fM8oIfW6NNdYLHCnGVh6x9R35VLnk3BeYBqIq0x6aNa6Fy_6kmn; isg=BExMEa6ZQNV1gFR37Yj6Dk5pHap-hfAvDTXVD6YNNveGMew7zpWovW2H0TkJeSiH",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=c_8GB7G86hS6adSHVV_61Tu14QGdZ9oNCE8e8EfHOueXUQYFi1EU4cNttOpMko1..; l=eBOiEkiqjTguzv4fBOfwnurza77ttIRAguPzaNbMiOCPOo19JXiPW6NNdrLpCnGVh6cBR35VLnk3BeYBqIq0x6aNa6Fy_nDmn; isg=BE1Nn_EoEWas87UURPcLfcd-XGnHKoH89EI0LI_SzORHhm04V3rkzUkQ8BrgRpm0",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=cw0ABP6FWLv0CyF-TmKl17nPQyoOZh1YIswOWIHxpsXXv7bOiCunJDZHc5WYyQC..; l=eBOiEkiqjTguzmHhBO5ZPurza77t3IRb8sPzaNbMiInca1ldsefMjNCQ_tRv-dtjgtfUZetPg9-qKR3p-ma38K_ceTwhKXIpB4v9-; isg=BA4O0yTu4jPMjlZJ07JY6PhDX-TQj9KJG09XkThX7JHCm6_1oB5hmPNd08f3g8qh",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=cdMRBP_NpEYuROrxbbdcAohcn7nRZ5s8-gadp33-51zRPo6diJkiBfNMNk78HnC..; l=eBOiEkiqjTguzP83BOfZhurza77THIRfguPzaNbMiOCPOX5J-0LcW6NN3bTvCnGVn6PJR35VLnk3B4Yn2y4ehZXRFJXn9Mpt4dLh.; isg=BNXVCvCvGV4bvj18fF_zlQ8W5NGP0onkrJq8xFd66syJrvSgHyPRtaFoeLIYrqGc",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=cXgOB0XPkpvgJ5VKacKhGWnL1_cOZi1Tn1wAkCHtU-Ihlo_AiIuoy0ZkfSWTJBC..; l=eBOiEkiqjTguzxHfBO5aourza77T3IOb8sPzaNbMiInca6ZFwEgmSNCQ_toJkdtjgtfEietPg9-qKRFk-PzLRK_ceTwhKXIpBxv9-; isg=BN_f69p5w9zlYcee2imZ18F4bjNpRDPmsoTmJnEtYQ7-AP6CeRX7NsHWwpB-mAte",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=c9cNBsXLICdaiSNXe5NVcjbAPxZOZ3Z0V6zzIvDnkytDXkwGiPSY-esY8rrJtRf..; l=eBOiEkiqjTguzA98BO5aFurza77OuIRb4sPzaNbMiInca69fTEGcDNCQ_tyw7dtjgt1nhetPg9-qKRLHR3A0mkfQ7_5LaC8onxf..; isg=BHd3H9s12wTNl1_WAiFxH5ngBmvBPEue2gwe7skkA8a6eJe60Q2L7kxeWtgmkCMW",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=clwRBOYwpZbo_OoYb7CDAmFfZyVdZrt--3gppgU8S9yfnDJdiJygB5GGND8-HiC..; l=eBOiEkiqjTguzxvXBO5aourza77T6IRb8sPzaNbMiInca1-5sUxCyNCQ_tfB-dtjgtfEFetPg9-qKR3B-Ja38K_ceTwhKXIpBcp9-; isg=BKqqB3w-vi-JDzId36Z0hLyf-xBMGy5134Nz5TRjrv2_Z0shHKo8hMuR95P7l6YN",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; isg=BPb2Fygyigtl2H6xKzrgIKBbRyz4FzpRc0e_SWDfH1lMo5c9yKbIYGcSu3_PCzJp",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=c7PRBVxw9ijlxGuY78BDRqEUVVrdZdL-xUip9aE8eyLGTDAdikPg6RMGF2--MZC..; l=eBOiEkiqjTguzgkwBOfZhurza77TGIRfguPzaNbMiOCPOa5WJIEAW6NNnw8XCnGVn6o9R35VLnk3B4TnMy4ehZXRFJXn9MptDdLh.; isg=BMHBNd66RVoWIakwKLPfEZPy0A3b7jXgoH4ICCMW1EgrCuDcaz8PsYkM7H5MAs0Y",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; isg=BKys9htx4DXbvvRXDaiaLq5JfYreZVAPrRW1LwbtKdf2EU0bLnRqnsTgMdmpmYhn",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=cq9hBimYvB5Cqx1MGv6BAZoI-2gOZQlFRLJwQLjMnE9OVMpNiuFagXZKjwLHe71..; l=eBOiEkiqjTguzBijBOfwhurza77O9IRAguPzaNbMiOCPOx1elqnRW6NNnHLwCnGVh6xvR35VLnk3BeYBqIq0x6aNa6Fy_Qkmn; isg=BPPzot2gl9DojVvaLrXNKz2cgvcdKIfqvqAa4qWQcpJTpBNGLfljOrsyXtRKBN_i",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=cXCCBPVmVDmIlayrTwaZauO7iidlZ_E6SJtdRtiYGSBaMH_CiMc2cFuhEcc9HF1..; l=eBOiEkiqjTguzXbvBOfZnurza77TTIRAguPzaNbMiOCPOwfeldDfW6NNnjLwCnGVh6cXR35VLnk3BeYBqIq0x6aNa6Fy_3Dmn; isg=BBwcr8efkGUrpGTnHXgqnp557TrOlcC_vSUFf_Ydcof8QbzLHqT9T2b3oam5SfgX",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=cQ-ABRVUXbcDQVXJLE3uCTdOEi8OZc2As-1TXxdvu6RzttEOiR-Hve_nlOPA2YC..; l=eBOiEkiqjTguz4hhBO5CFurza7790IRb8sPzaNbMiInca6g5sENkzNCQ_tmX-dtjgtfEletPg9-qKR3M-u4LRK_ceTwhKXIpBmp9-; isg=BISEdUbfuD3DHQyv9WAyVsbxVQJ2nagHld3tt54lhc8yySWTxqw8lztvCWERUeBf",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; isg=BBMTTE2qd3CIMzt6DhWti108opc9yKeKnkA6QsUwmDJIRDLmTZlz2vDVfrQqZP-C",
                  "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=16b00c0db35eb2918c10a97b99080c5b; tracknick=themagicofsmile; _tb_token_=e343de361e333; cookie2=199cbd031001ff296d70c37c88cec975; xlly_s=1; _m_h5_tk=ac6e26458b0a0cd4d406c08a995be19a_1615521358671; _m_h5_tk_enc=ff0167d1f1f03296d92716c9626f45c1; x5sec=7b22726174656d616e616765723b32223a2232636138643834613936346562363837346562666335613739643866356538354350577371344947454a69716c4a364c6d6f7238447a447475662f632f762f2f2f2f3842227d; tfstk=c--RBiVavjclHzBvQU30dtdLGEORZFeRt81LvYdJzRnKd6ZdiW-MXF_iP9PRDxC..; l=eBOiEkiqjTguzUNFBOfZhurza77TGIRfguPzaNbMiOCPOM5w5LvNW6NNnR8eCnGVn6kDR35VLnk3BvY3nyzHhZXRFJXn9Mpt8dLh.; isg=BDIybm55hgdB4Lpllw58vAS3g3gUwzZdl9v7ffwLN-XZj9OJ5FLmbI3pfysz_671",
                  ]
        itemId = ["523027819179",
                  "42861838038",
                  "539339147058",
                  "536104696285",
                  "534305594544",
                  "576644195365",
                  "525872510577",
                  "553133804175",
                  "577145913309",
                  "608104972592",
                  "545473839106",
                  "606623539943",
                  "544309421928",
                  "577801645059",
                  "15657673602",
                  ]
        sellerId = ["1710977178",
                    "1050505647",
                    "1652554937",
                    "2770381889",
                    "2301367418",
                    "533497499",
                    "2649573952",
                    "2549841410",
                    "4008346408",
                    "2095455386",
                    "3164711246",
                    "2201478422910",
                    "3074019282",
                    "2978398582",
                    "1023696028",
                    ]

        # 收集100页的评论
        for x in range(0, 15):
            comments = ""
            for page_num in range(1, 101):
                self.url_info(cookie[x], itemId[x], sellerId[x], str(page_num))
                # 获取rateContent,格式为“rateContent”：“好评”
                with open('response.txt', 'r', encoding='utf8') as f_con:
                    for line in f_con.readlines():
                        content = re.findall(r"\"rateContent\".*?,", line)

                # 获取rateContent的内容
                for i in range(len(content)):
                    comments = comments + str(content[i]).split(":")[1] + "\n"
                print("已爬取" + str(page_num) + "页...")
                time.sleep(1)

            comments = str(bytes(comments, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
            with open(filename[x], 'w', encoding='utf8') as f:
                f.write(comments)

def main():
    all_commments = []
    for x in range(len(filename)):
        with open(filename[x], 'r', encoding='utf8') as f:
            comments = f.readlines()
        all_commments.append(comments)
    return all_commments

import requests
import re
import time

# request url的response
def url_info(cookie, itemId, sellerId, page_num):
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

def get_info(filename):
    cookie = ["lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=be1456f3d19940248377464982c9be00_1615914364003; _m_h5_tk_enc=6f38c3ae2f58dfc99bf94b559a42e55e; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; tfstk=cavCBOD0Py4IFWGzLHiaUTvE_F6AZ501jX_pAIG-CsA0jNtCi92VlGrHZP2OMG1..; l=eBOiEkiqjTguza08BOfZlurza779AIRAguPzaNbMiOCPOHf65MIOW6wzdxLBCnGVh6RwR3yf4eUaBeYBqIq0x6aNa6Fy_LHmn; isg=BBERSF3QFXaUP3kg2COP4WMCIB2rfoXwAwXyXfOmLlj1mjHsO8_CwZz8PG58kh0o",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=be1456f3d19940248377464982c9be00_1615914364003; _m_h5_tk_enc=6f38c3ae2f58dfc99bf94b559a42e55e; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; l=eBOiEkiqjTguz_cUBOfwlurza77tDIRfguPzaNbMiOCP99CW8BqcW6wzQCYXCnGVnsOpR3yf4eUaB7TnUyUBhZXRFJXn9MptUdLh.; tfstk=cM11B2Voccm6Y5wq_NaEgIjNUXROZ7EB-RtO5TwYt-08bI71iZcyVeuGnDcpee1..; isg=BNraecfOboMMueJtr7ZENGyPK4D8C17l_HgJ0ORT8W0JV3uRzJqU9VChJyNLh9Z9",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=be1456f3d19940248377464982c9be00_1615914364003; _m_h5_tk_enc=6f38c3ae2f58dfc99bf94b559a42e55e; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; isg=BB4er_1f8h-osiY5Q2JIOIgTb7Rg3-JZWFRNZMimBmF567zFMG9mabrN4_dnU9px; tfstk=cOUGBQ1J6lo_MIo3VNg_1oWmJGacaNIZCrzU8r4iziaUDNaE_sc9Y3S666DTIrKf.; l=eBOiEkiqjTguzVIfBO5Cnurza77ToIdbzsPzaNbMiInca6gfNe8OaNCQURopldtjgtCfjetzhg8L7RIii34dgZqhuJ1REpZZDxvO.",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=be1456f3d19940248377464982c9be00_1615914364003; _m_h5_tk_enc=6f38c3ae2f58dfc99bf94b559a42e55e; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; l=eBOiEkiqjTguzu-WBO5Zourza77OeIRb8sPzaNbMiInca6ff_eEQTNCQURPD8dtjgtCfdetzhg8L7RILO3apgZqhuJ1REpZZfxvO.; tfstk=cUM5BVvGRab7-9dFU0tVLJ2fyseGZYTbmQa-VfOpA3bwWRi5iYXa5oSotZXY6o1..; isg=BHx8g-6pMFlexwTHvZjKvv5ZTRoudSCfju7vOlb9NmdjIR2rfoWjLkKXAUlZaVj3",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; tk_trace=1; _m_h5_tk=3b58add69eaf77a4cf7af68fb42b6582_1616260878313; _m_h5_tk_enc=51abd3a6ba087a505028b1a4e5a16608; x5sec=7b22726174656d616e616765723b32223a223737306632623166643661343834363462326133383732323436393364613433434a625a32494947454e7256704c76456f662b423841457737626e2f3350372f2f2f2f2f41513d3d227d; l=eBOiEkiqjTguz3V8BOfwnurza77tLIRAguPzaNbMiOCP9XfHWcklW6wz7DYMCnGVh67MR3yf4eUaBeYBqIq0x6aNa6Fy__Mmn; tfstk=c2TcB3GLMnSfbPIkAq_XGho35amdZNnVhF8yzFYmMTkOhOLPitEzYmNxZtpDWl1..; isg=BA8PUfdus1DBGrfuqjlpR3FonqMZNGNW0X-8EyEc_X6M8C_yKQWPppHm8iDOiDvO",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; _m_h5_tk=3b58add69eaf77a4cf7af68fb42b6582_1616260878313; _m_h5_tk_enc=51abd3a6ba087a505028b1a4e5a16608; x5sec=7b22726174656d616e616765723b32223a223863383938333634383739653832356439353331386562623336653338333466434d473832494947454f547235714f4d33656936466967434d4f32352f397a2b2f2f2f2f2f77453d227d; isg=BLa23ArAyldi975x63ogYGCbB-y41_oRYOz1LCCf0Bk6Y1f9iGcFIW1aez8PS_Ip",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; _m_h5_tk=3b58add69eaf77a4cf7af68fb42b6582_1616260878313; _m_h5_tk_enc=51abd3a6ba087a505028b1a4e5a16608; x5sec=7b22726174656d616e616765723b32223a223863383938333634383739653832356439353331386562623336653338333466434d473832494947454f547235714f4d33656936466967434d4f32352f397a2b2f2f2f2f2f77453d227d; isg=BLa23ArAyldi975x63ogYGCbB-y41_oRYOz1LCCf0Bk6Y1f9iGcFIW1aez8PS_Ip",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; tk_trace=1; _m_h5_tk=3b58add69eaf77a4cf7af68fb42b6582_1616260878313; _m_h5_tk_enc=51abd3a6ba087a505028b1a4e5a16608; x5sec=7b22726174656d616e616765723b32223a223863383938333634383739653832356439353331386562623336653338333466434d473832494947454f547235714f4d33656936466967434d4f32352f397a2b2f2f2f2f2f77453d227d; tfstk=cLMNBnfLsdpa5JeXwRwVlrHjq35OZsz0P9rzsX4iU26X5yVGil7YxH_YYozJK5f..; l=eBOiEkiqjTguz-xWBO5Zourza77tFIRb8sPzaNbMiInca6wlse-GONCQU5Ew-dtjgtfXyetzhg8L7R3X-oU_WK_ceTwhKXIpBmp9-; isg=BAAA-FSrdJUougjTkfSOYlqt0Y7SieRTqprjDnqRapu69aEfIpj64dDDDV01xZwr",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; _m_h5_tk=3b58add69eaf77a4cf7af68fb42b6582_1616260878313; _m_h5_tk_enc=51abd3a6ba087a505028b1a4e5a16608; x5sec=7b22726174656d616e616765723b32223a223863383938333634383739653832356439353331386562623336653338333466434d473832494947454f547235714f4d33656936466967434d4f32352f397a2b2f2f2f2f2f77453d227d; isg=BNbWdt41qveDI54Ry9oAwIA7J4zYdxqxQEyVTEA-g7l3A3edqAYkwzqym5_vqxLJ",
              "lid=themagicofsmile; enc=5NJ%2FuElP%2FY2GpN8nd9T2LQRbo%2F6EBhMeAJ5CSDX%2BJgZ5qVeN476Sk8v%2Ff1T%2FHkMENk8KZ4uE6hu4RkPdNwr%2FQA%3D%3D; cna=AzAkF/NfDFQCAd9KMFtPL+gE; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E%2FvGVyk6d9wIZyneqfw5Z; t=d72e1163ffdc07e0faf9162cae405c89; tracknick=themagicofsmile; _tb_token_=56b395e7e93be; cookie2=1977a6fc108aa6cb6db95ff45c36bbfb; xlly_s=1; tk_trace=1; _m_h5_tk=3b58add69eaf77a4cf7af68fb42b6582_1616260878313; _m_h5_tk_enc=51abd3a6ba087a505028b1a4e5a16608; x5sec=7b22726174656d616e616765723b32223a223863383938333634383739653832356439353331386562623336653338333466434d473832494947454f547235714f4d33656936466967434d4f32352f397a2b2f2f2f2f2f77453d227d; tfstk=cxPNBQ9KI1CajZcfefG2cme69pvOZUimVBurIJmgZYn2icDGiP-x-wtx8qoRtAf..; l=eBOiEkiqjTguz_t8BO5CFurza77ToIRb8sPzaNbMiInca6ZdsFzMZNCQU5_e-dtjgtffzetzhg8L7RF2-SU38K_ceTwhKXIpB099-; isg=BK2tf_O6sVrE3VX05BernSdevEknCuHcR8me6e-yZ8SpZswYt1vMrd0wUDqAZvmU",
              ]
    itemId = ["18483428998",
              "605448737579",
              "594932506002",
              "581410608410",
              "638462715559",
              "605441157623",
              "620965870548",
              "616567613998",
              "583184933292",
              "535576218349",
              ]
    sellerId = ["917264765",
                "653243179",
                "353026386",
                "1122313708",
                "2207467945974",
                "2095455386",
                "2973741383",
                "379424083",
                "4263377845",
                "2926596407",
                ]

    # 收集100页的评论
    for x in range(4, 5):
        comments = ""
        for page_num in range(1, 101):
            url_info(cookie[x], itemId[x], sellerId[x], str(page_num))
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

if __name__ == '__main__':
    filename = ['E:\\backend\\recommend\\data\\comments\\sk2',
                'E:\\backend\\recommend\\data\\comments\\hanshu',
                'E:\\backend\\recommend\\data\\comments\\mg',
                'E:\\backend\\recommend\\data\\comments\\pangshi',
                'E:\\backend\\recommend\\data\\comments\\wanzixx',
                'E:\\backend\\recommend\\data\\comments\\xiaobding',
                'E:\\backend\\recommend\\data\\comments\\youtlan',
                'E:\\backend\\recommend\\data\\comments\\bolaiya',
                'E:\\backend\\recommend\\data\\comments\\farmacy',
                'E:\\backend\\recommend\\data\\comments\\niuxzmi',
                ]

    get_info(filename)

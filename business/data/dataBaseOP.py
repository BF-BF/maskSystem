from business.data import dataAPI

# 商品评论入库(list)
dataAPI.insert_all_coms()
print("商品评论入库成功")

# 商品好评入库(list)
dataAPI.insert_pos_com()
print("商品好评入库成功")

# 商品差评入库(list)
dataAPI.insert_nav_com()
print("商品差评入库成功")

# 形容词入库(list)
dataAPI.insert_adj_word()
print("商品形容词入库成功")

# 词频入库
dataAPI.insert_words_tf()
print("词频入库成功")

# 商品主题入库(list)
dataAPI.insert_theme()
print("商品主题入库成功")

# 商品二元词组入库(list)
dataAPI.insert_bigram()
print("商品二元组入库成功")

# 商品词云图片名称入库
dataAPI.insert_wc_name()
print("商品词云图片名称入库成功")

# 商品对应天猫商城的url入库
dataAPI.insert_urls()
print("商品对应天猫商城的url入库成功")

# 用户
dataAPI.insert_user()
print("用户入库成功")

# 搜索面膜次数
dataAPI.insert_click_num()
print("搜索面膜次数入库成功")
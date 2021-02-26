import MeCab
from bs4 import BeautifulSoup

for j in range(1,66):
    file_path = "wikipedia/" + str(j)
    path_flat = file_path + "/flat_text_" + str(j) + ".txt"
    path_wa = file_path + "/wakati_" + str(j) + ".txt"
    for i in range(0,99):
        if i < 10:
            file_num = "0" + str(i)
        else:
            file_num = str(i)

        path = file_path + "/wiki_" + file_num

        with open(path, encoding="utf-8") as f:
            xml = f.read()
            soup = BeautifulSoup(xml, "html.parser")
            docs = soup.get_text(strip=True)
            #ファイルの全文を取得するには.find()を付けずに直接get

        cr_docs = docs.replace("\n", "")
        cr_docs = cr_docs.replace("。", ".")
        cr_docs = cr_docs.replace("、", ",")
        cr_docs = cr_docs.replace('"','')

        #print(cr_docs) 重いから実行しない！！

        #分かち書き
        tagger = MeCab.Tagger("-Owakati")
        wa_text = tagger.parse(cr_docs)

        #MeCabが改行に対応できないため、改めて設定
        unwanted_chars = ["(",")","[","]","'","（","）"]
        for uc in unwanted_chars:
            wa_text = wa_text.replace(uc, "")
        wa_text = wa_text.replace(".",".\n")


        #平文保存
        with open(path_flat, mode="a", encoding="utf-8") as f:
            f.write(cr_docs)

        #分かち書き保存
        with open(path_wa, mode="a", encoding="utf-8") as f:
            f.write(wa_text)

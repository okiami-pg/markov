from sys import argv
import MeCab
import markovify

def main():
    file_name = argv[1]
    #argv[1]とすることで、コマンドプロンプト上で
    #"python generator.py （ファイル名）"と入力するだけで
    #そのファイルをfile_nameとして設定する。
    with open(file_name, "r", encoding="utf-8") as f:
        docs = f.read()
    cr_docs = docs.replace("\n", "")
    tagger = MeCab.Tagger("-Owakati")
    wa_text = tagger.parse(cr_docs)

    wa_text = wa_text.replace('"','')
    unwanted_chars = ["(",")","[","]","'","（","）"]
    for uc in unwanted_chars:
        wa_text = wa_text.replace(uc, "")
    wa_text = wa_text.replace("。","。\n")

    global model
    model = markovify.NewlineText(wa_text, state_size=3)
    #state_sizeでN階マルコフ連鎖を指定できる。今回は3
    sentence = model.make_short_sentence(280)
    sentence = sentence.replace(" ","")
    print(sentence)

def gen_text():
    for i in range(30):
        pro = model.make_short_sentence(280, 50, tries=20)
        pro = pro.replace(".","。")
        pro = pro.replace(",","、")
        pro = pro.replace(" ","")

        with open("product.txt", mode="a", encoding="utf-8") as f:
            f.write(pro)

if __name__ == "__main__":
    if argv[2] == "generate_txt":
        main()
        gen_text()
    else:
        main()

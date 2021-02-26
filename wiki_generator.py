import markovify
from sys import argv

#目標：構築したモデルを使って生成した文章をtxtで出してくれるソフト
#仕様：cmdでpython (this) (ファイルタイトル)で渡すと、ファイルを生成

def make_wiki():
    file_name = argv[1]
    out_path = file_name + ".txt"
    path = "wikimar.json"
    with open(path, "r") as f:
        json = f.read()
        model = markovify.Text.from_json(json)

    for i in range(30):
        sentence = model.make_short_sentence(280, 50, tries=20)
        sentence = sentence.replace(".","。")
        sentence = sentence.replace(",","、")
        sentence = sentence.replace(" ","")

        with open(out_path, mode="a", encoding="utf-8") as f:
            f.write(sentence)

if __name__ == '__main__':
    make_wiki()

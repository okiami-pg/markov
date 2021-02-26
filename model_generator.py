import markovify

#モデルのjsonファイルを生成する
def model_generator(file_num):
    path = "wikipedia/" + str(file_num) + "/wakati_" + str(file_num) + ".txt"
    with open(path, encoding="utf-8") as f:
        wa_text = f.read()

    #モデルの生成とjsonファイルへの保存
    model = markovify.NewlineText(wa_text, state_size=3, retain_original=False)
    path_json = "wikipedia/" + str(file_num) + "/learned_data_" + str(file_num) + ".json"
    with open(path_json, "w") as f:
        f.write(model.to_json())
    sentence = model.make_short_sentence(120)
    print(sentence)


if __name__ == "__main__":
    for i in range(1,66):
        model_generator(i)

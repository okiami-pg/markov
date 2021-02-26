import markovify

def model_combine():
    init_path = "wikipedia/1/learned_data_1.json"
    with open(init_path, "r") as f:
        model_init = f.read()
        model_comb = markovify.Text.from_json(model_init)
    seco_path = "wikipedia/2/learned_data_2.json"
    with open(seco_path, "r") as f:
        model_seco = f.read()
        model_com2 = markovify.Text.from_json(model_seco)
    model_comb = markovify.combine(models=[model_comb, model_com2])
    sentence = model_comb.make_short_sentence(200, 50, tries=10)
    print(sentence)
    last_path = "wikimar.json"
    with open(last_path, "w") as f:
        f.write(model_comb.to_json())

if __name__ == "__main__":
    model_combine()

import markovify

path = "wikipedia/1/learned_data_1.json"
path2 = "wikipedia/2/learned_data_2.json"
with open(path2, "r") as f:
    model_22 = f.read()
    model_2 = markovify.Text.from_json(model_22)
model_no = None
model_comb = markovify.combine(models=[model_no, model_2])
sentence = model_comb.make_short_sentence(200, 50, tries=10)
print(sentence)

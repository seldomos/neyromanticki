from senticnet.senticnet import SenticNet

sn = SenticNet('ru')

word = input('Введите ваш комментарий(например "как дела"): ')

lst = word.split()

#concept_info = sn.concept(word)
#polarity_value = sn.polarity_value(word)
#polarity_intense = sn.polarity_intense(word)
#moodtags = sn.moodtags(word)
#semantics = sn.semantics(word)

print(list(map(lambda x: sn.sentics(x), lst)))
pop = input(" ")

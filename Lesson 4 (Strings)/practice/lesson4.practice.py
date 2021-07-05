# Открываем wikipedia.org, нажимаем случайную страницу, берем первый абзац и к нему
# 1. Через for и list comprehensions:
#  - Применяем удаление буквы 'a'
#
# 2. Удалить ту же букву через replace
# 3. Срез последней строки (найти индекс фразы из последней строки и использовать срез)
# 4. Разбиение по строкам весь абзац
#
# * каждый пункт пишем в отдельную переменную и выводим в конце работы программы

text = "Wikiquote is a free online compendium of sourced quotations from notable people and creative works in every \n" \
       "language, translations of non-English quotes, and links to Wikipedia for further information. Visit the help \n" \
       "page or experiment in the sandbox to learn how you can edit nearly any page right now; or go to the Log in \n" \
       "to start contributing to Wikiquote."

# 1. Через for и list comprehensions:
#  - Применяем удаление буквы 'a'
test_list = [letter for letter in text if letter != 'a']
print("\n" + "".join(test_list))

# 2. Удалить ту же букву через replace

print("\n" + text.replace("a", ""))

# 3. Срез последней строки (найти индекс фразы из последней строки и использовать срез)
# 4. Разбиение по строкам весь абзац

lastSent = text.split("\n")[-1]
indexOfPhrase = lastSent.index("start")
print("Index of find phrase is " + str(indexOfPhrase))





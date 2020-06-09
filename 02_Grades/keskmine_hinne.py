# Ülesanne: tagasta list, kus on list iga aine jaoks. Igas aine listis on aine nimi ja vastav keskmine hinne

fail = open("hinded.csv", encoding="UTF-8")
# for rida in fail:
#     print("Lugesin sellise rea: " + rida)


for rida in fail:
    osad = rida.split(',')
    for osa in osad:
        print(osa)

fail.close()
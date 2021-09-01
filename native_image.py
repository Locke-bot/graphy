from PIL import Image
juju = Image.open("2542.png")
# jujucrop = juju.crop((173, 605, 933, 111))
# jujucrop = juju.crop((173, 111, 933, 605))
jujucrop = juju.crop((172, 110, 934, 606))
jujucrop.show(jujucrop)
jujucrop.save("2542.png")
def titi(tit):
    mini, maxi = float("inf"), 0
    for tup in tit:
        if tup[0] > maxi:
            maxi = tup[0]
            continue
        if tup[0] < mini:
            mini = tup[0]
    return mini, maxi
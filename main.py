import requests

# Fungsi ini akan meneruskan teks pengguna ke model machine learning
# dan mengembalikan hasil teratas dengan probabilitas tertinggi
def classify(text):
    key = "8bbc7840-dcfb-11ed-809b-a3e71b9554887d93e513-00be-4933-8ce0-324db72e5afb"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

'''# GANTI INI menjadi sesuatu yang kamu inginkan untuk diklasifikasikan oleh model machine learning kamu
demo = classify("what foods do owls like?")

label = demo["class_name"]
confidence = demo["confidence"]


# GANTI INI untuk melakukan sesuatu yang berbeda dengan hasilnya
print ("result: '%s' with %d%% confidence" % (label, confidence))'''

def answer_question():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]

    if answerclass == "food":
      print ("invertebrates (such as insects, spiders, earthworms, snails and crabs), fish, reptiles, amphibians, birds and small mammals")
    elif answerclass ==  "countries":
      print ("Owls live in a variety of habitats, including coniferous forests, mountains, deserts, and plains")
    elif answerclass ==  "lifespan":
      print ("Owls have a lifespan of 10 to 30 years, depending on its species.")
    elif answerclass == "species":
      print ("There are nearly 250 owl species in the world, divided into two families.")
    elif answerclass == "size":
      print ("Adult great horned owls range in length from 43 to 64 cm (17 to 25 in), with an average of 55 cm (22 in), and possess a wingspan of 91 to 153 cm (3 ft 0 in to 5 ft 0 in), with an average of 122 cm (48 in). Females are somewhat larger than males.")
    else :
       print("I don't understand. Ask me something else!")

print("what would you like to know about owls? ")
# while True:
for i in range(5):
   answer_question()
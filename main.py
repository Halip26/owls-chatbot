import requests

# Fungsi ini akan meneruskan teks pengguna ke model pembelajaran mesin
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

'''# GANTI INI menjadi sesuatu yang kamu inginkan untuk diklasifikasikan oleh model machine learnig kamu
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
      print ("")
    elif answerclass ==  "lifespan":
      print ("")
    elif answerclass == "species":
      print ("")
    elif answerclass == "size":
      print ("")

print("what would you like to know about owls? ")
while True:
   answer_question()
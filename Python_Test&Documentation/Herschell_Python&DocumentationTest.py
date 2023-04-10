# I will be utilizing .xml file(s) from my current project within the Simpsons Project.
import spacy
import os

# nlp = spacy.cli.download("en_core_web_lg")
# ^Uncomment line above if the language model is required/needed. If already obtained, comment it out.
nlp = spacy.load("en_core_web_lg")

workingDir = os.getcwd()
print("Working Directory: " + workingDir)
# os.listdir will list the files and folders inside a path:
insideDir = os.listdir(workingDir)
print("In the directory are the following files: " + str(insideDir))

CollPath = os.path.join(workingDir, 'XML_Files/XML_samples/Simpsons_S1')
print(CollPath)


def ReadTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        print(readFile)
        stringFile = str(readFile)
        lengthFile = len(readFile)
        print(lengthFile)
        tokens = nlp(stringFile)
        print(tokens)
        listEntities = EntityCollector(tokens)
        print(listEntities)


def EntityCollector(tokens):
    labels = set([w.label_ for w in tokens.ents])
    entities = {}
    for label in labels:
        entities[label] = [ent.text for ent in tokens.ents if ent.label_ == label]
        print(label + ": " + str(entities[label]))
    return entities

for file in os.listdir(CollPath):
    if file.endswith(".xml"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        ReadTextFiles(filepath)

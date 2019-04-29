#!/usr/bin/python3
"""
Pls pay attention to the path of vocab.txt.
This file is in the same folder with vocab.text.
"""
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

with open('vocab.txt', 'r') as vocabfile:
    vocabcontent = vocabfile.read()

doc = nlp(vocabcontent)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
    with open('vocab_cluster.txt', 'a') as outputclusterfile:
        outputclusterfile.write("{}, {} /n".format(entity.text, entity.label_))
import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

def segment_into_edus(text):
    # Tokenize text into sentences using SpaCy
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]

    # Further segment each sentence into EDUs
    edus = []
    for sentence in sentences:
        # Custom logic for EDU segmentation (e.g., based on punctuation)
        edu_tokens = []
        for token in nlp(sentence):
            if token.is_punct:
                # If the token is punctuation, treat it as an EDU boundary
                if edu_tokens:
                    edus.append(" ".join(edu_tokens))
                    edu_tokens = []
            else:
                # Otherwise, add the token to the current EDU
                edu_tokens.append(token.text)

        # Add the remaining tokens as the last EDU
        if edu_tokens:
            edus.append(" ".join(edu_tokens))

    return sentences, edus


# # Example text
# text = "I had a very mixed experience at The Stand. The burger and fries were good. The chocolate shake was divine: rich and creamy. The drive-thru was horrible. It took us at least 30 minutes to order when there were only four cars in front of us. We complained about the wait and got a half–hearted apology. I would go back because the food is good, but my only hesitation is the wait."

# text_test = "My son loved it. It is easy even though my son is in first grade. Highly recommend it."

# # Segment text into EDUs
# sentences, edus = segment_into_edus(text_test)

# sent = "My son loved it."
# sent_lst = sent.strip().split(".")
# if (len(sent_lst) > 1 or (len(sent_lst) == 1 and len(sent_lst[0].split()) > 1)):
#     print("filtered", sent)

# # Print EDUs
# print("Elementary Discourse Units (EDUs):")
# for edu in edus:
#     print("-", edu)

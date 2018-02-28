from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."
print("before: ", example_sentence)
stop_words = set(stopwords.words("english"))

# print(stop_words)
#{'is', 'ourselves', 'herself', "wouldn't", 'through', 'wasn', "you've", 'does', 'if', "haven't", 'having', 'he', 'too', "hadn't", 'between', 'any', 'me', 'after', 'shan', 'an', 'that', 'you', 'what', 'down', 'on', 'further', 'weren', 'its', 'the', 'where', 'ain', "hasn't", "won't", 'nor', 'in', 'it', 'to', 'doesn', "that'll", 'her', 've', 'yourselves', "you're", 'they', 'haven', "don't", 'she', 'can', "couldn't", 'before', 'those', 'of', 'o', 'until', 'aren', 'hasn', 'whom', 'here', 'out', 'about', 'other', 'didn', 'y', 'a', 'him', 'same', 'being', 'then', "wasn't", 'so', "isn't", 'but', 'once', 'few', 'hers', 'needn', 'both', "doesn't", "you'll", 'shouldn', 'these', 'ours', 'doing', 'at', 'some', 'have', 'above', 'd', "should've", 'again', 'do', 'while', 'should', 'over', 'during', "needn't", 'for', "mustn't", 'not', 'll', 'ma', 'all', 'themselves', 'has', "didn't", 'how', "she's", 'won', 'yours', 'my', 'which', 'his', 'each', 'below', 'more', 'will', 'no', 'against', "mightn't", 'm', 'itself', 'why', 'did', 'because', 'wouldn', 'yourself', 'as', 'from', 'very', 'are', "shan't", 'been', 'were', 't', 'such', 're', 'into', 'myself', 'had', 'off', 'hadn', 'am', 'isn', 'our', 'by', 'with', "it's", 'mustn', 'theirs', 'and', "shouldn't", 'i', 's', 'this', 'up', 'we', "you'd", 'just', 'when', "aren't", 'your', 'or', 'couldn', 'be', 'don', 'was', 'them', 'there', 'own', 'their', 'under', 'now', 'only', 'than', "weren't", 'most', 'who', 'mightn', 'himself'}

words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

# filtered_sentence = [w for w in words if not w in stop_words]

print("after filter: ", filtered_sentence)
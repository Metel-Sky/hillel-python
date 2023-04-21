import time

text = """
The diesel engine, named after Rudolf Diesel, is an internal combustion
 engine in which ignition of the fuel is caused by the elevated temperature 
 of the air in the cylinder due to mechanical compression; thus, the diesel 
 engine is called a compression-ignition engine (CI engine). This contrasts 
 with engines using spark plug-ignition of the air-fuel mixture, such as a 
 petrol engine (gasoline engine) or a gas engine (using a gaseous fuel like 
 natural gas or liquefied petroleum gas)."""

text_words = text.split()

clean_text = list()
for word in text_words:
    word = word.lower().strip('.,;()')
    clean_text.append(word)

EXPERIMENT_COUNT = 100000

# SET EXPERIMENT
stopwords_set = {'the', 'of', 'or', 'a', 'an', 'is', 'such', 'by', 'thus', 'like', 'as', 'are', 'am', 'to', 'in', 'which', 'this', 'with', 'due', 'after'}

t0 = time.time()
for i in range(EXPERIMENT_COUNT):
    filtered_words = list()
    for word in text_words:
        if word not in stopwords_set:
            filtered_words.append(word)
print(' '.join(filtered_words))
print(f'Set operation took {round(time.time() - t0, 3)}s')

# LIST EXPERIMENT
stopwords_list = list(stopwords_set)

t0 = time.time()
for i in range(EXPERIMENT_COUNT):
    filtered_words = list()
    for word in text_words:
        if word not in stopwords_list:
            filtered_words.append(word)
print(' '.join(filtered_words))
print(f'List operation took {round(time.time() - t0, 3)}s')
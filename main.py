import nltk
from nltk.corpus import stopwords

#Baixando as atualizações do nltk
#nltk.download()

#nltk.download('rslp')




base = [('eu estou alegre e com confiança','alegria'),
        ('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

#print(base[0])

#stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
#             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
#             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']


stops = stopwords.words('portuguese')

def removestopword(texto):
    frases = []
    for (palavras,emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stops]
        frases.append((semstop,emocao))
    return frases

def aplicastemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras,emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stops]
        frasessstemming.append((comstemming,emocao))
    return frasessstemming

def buscapalavras(frases):
    todaspalavras = []
    for(palavras,emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras

def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = { }
    for palavras in palavrasunicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas






semstopWords = removestopword(base)
#print(semstopWords)

frasescomstemming = aplicastemmer(base)
#print(frasescomstemming)

palavras = buscapalavras(frasescomstemming)
#print(palavras)

frequencia = buscafrequencia(palavras)
#print(frequencia.most_common(50))

palavrasunicas =  buscapalavrasunicas(frequencia)
#print(palavrasunicas)

caracteristicasfrase = extratorpalavras(['am','nov','dia'])
#print(caracteristicasfrase)

basecompleta = nltk.classify.apply_features(extratorpalavras,frasescomstemming)
#print(basecompleta[0])

#Criando a tabela de probabilidades
classificador = nltk.NaiveBayesClassifier.train(basecompleta)
#print(classificador.labels())
#print(classificador.show_most_informative_features(10))

teste = 'estou com alegria e feliz'
testestemmig = []
stemmer = nltk.stem.RSLPStemmer()
for (palavras) in teste.split():
    comstem = [ p for p in palavras.split()]
    testestemmig.append(str(stemmer.stem(comstem[0])))

#print(testestemmig)
novo = extratorpalavras(testestemmig)
#print(novo)

print(classificador.classify(novo))
distribuicao = classificador.prob_classify(novo)
for classe in distribuicao.samples():
    print('%s: %f' %(classe,distribuicao.prob(classe)))



import nltk

def get_afinn_scores(file="AFINN-111.txt"):
    afinn_file = open(file)
    scores = {}
    for line in afinn_file:
      term, score  = line.split("\t")
      scores[term] = int(score)
    return scores


afinn_scores = get_afinn_scores()
# tweets = get_tweets()
tweets = open('tweets.json')

for tweet in tweets:
  ## Tokenize the tweet
  words = nltk.word_tokenize(tweet['text'])

  ## Get the total AFFIN score
  score = 0
  for w in words:
    if w.lower() in afinn_scores:
      score += afinn_scores[w.lower()]

  ## Store the value
  tweet['score'] = score

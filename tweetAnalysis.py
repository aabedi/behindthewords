import json

tweets = []
tweet_file = open('tweets.json')
for line in tweet_file:
  tweet = json.loads(line)
  text = coordinates = place = location = ''

  ## Get the tweet text
  text = tweet[u'text'].encode('utf-8')

  ## Get the tweet location
  if u'coordinates' in tweet and tweet[u'coordinates']:
    coordinates = tweet[u'coordinates'][u'coordinates']

  elif u'place' in tweet and tweet[u'place']:
    place = tweet[u'place'][u'full_name'].encode('utf-8')

  elif u'user' in tweet and tweet[u'user'][u'location']:
    location = tweet[u'user'][u'location'].encode('utf-8')

  tweets.append({'text':text, 'coordinates':coordinates,
                 'place':place, 'location':location})

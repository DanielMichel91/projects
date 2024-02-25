import json
from textblob import TextBlob
import seaborn as sns

# Read Twitter data from a JSON file
with open("data.json", "r") as file:
    twitter = json.load(file)

# Print the first element of the Twitter data
print(twitter[0])

# Filter the Twitter data for tweets related to the topic "obama"
obama_topic = list(filter(lambda x: x["topic"] == "obama", twitter))

# Analyze sentiment and update the "sentiment" field in each tweet
for i in obama_topic:
    tweet = i["tweet"]
    text = TextBlob(tweet)
    print(text)

    polarity = text.sentiment.polarity

    if polarity < -0.2:
        i["sentiment"] = "negative"
    elif polarity > 0.2:
        i["sentiment"] = "positive"
    else:
        i["sentiment"] = "neutral"

# Create a list of sentiments from the filtered Twitter data
obama_sentiments = [x["sentiment"] for x in obama_topic]

# Print the list of sentiments
print(obama_sentiments)

# Save the filtered Twitter data with sentiments to a new JSON file
with open("obama.json", "w") as fh:
    json.dump(obama_topic, fh)

# Set seaborn theme
sns.set_theme()

# Create a histogram plot of sentiments and save it as an image
sns_plot = sns.histplot(data=obama_sentiments)
sns_plot.set_title("sentiments in obama tweets")
sns_plot.set_xlabel("sentiments")
sns_plot.set_ylabel("counter")
sns_plot.figure.savefig('sentiments.png')
sns_plot.figure.clf()
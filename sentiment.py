import argparse
from google.cloud import language
from google.cloud.language import enums,types


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        if(sentence_sentiment==0):
            sentiment_result = '無感情'
        elif((sentence_sentiment<=1)and(sentence_sentiment>=0.5)):
            sentiment_result = 'ポジティブな感情'
        elif((sentence_sentiment>0)and(sentence_sentiment<0.5)):
            sentiment_result = 'ややポジティブな感情'
        elif((sentence_sentiment<0)and(sentence_sentiment>-0.5)):
            sentiment_result = 'ややネガティブな感情'
        else:
            sentiment_result = 'ネガティブな感情'
        print('Sentence {} has a sentiment score of {} 感情：{}'.format(index, sentence_sentiment,sentiment_result))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
    return 0


def analyze(text_name):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(text_name, 'r') as text_file:
        content = text_file.read()

    document = types.Document(
        content = content,
        type = enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document = document)

    print_result(annotations)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = __doc__,
        formatter_class = argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'text_name',
        help = 'The filename of the text youd like to analyze.')
    args = parser.parse_args()
    analyze(args.text_name)

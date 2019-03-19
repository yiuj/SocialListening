from watson_developer_cloud import ToneAnalyzerV3
import simplejson as json
from JSONtoTXT import cleanJSON
import sqlite3


def main():
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='oMsOr-VXaaNU9V5D9Pg0AXrC99jK1gJ4t1DGtgjfuKu7',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )
    text = ""
    try:
        conn = sqlite3.connect("../sentdex/twitter.db")
        c = conn.cursor()
        c.execute("SELECT tweet FROM sentiment")
        tweets = c.fetchall()

        for tweet in tweets:
            text += str(tweet)
    except Error as e:
        print(str(e))

    print("printing text")
    print(text)
    #
    # tone_analysis = tone_analyzer.tone(
    #     {'text': text},
    #     'application/json'
    # ).get_result()
    #
    # jsonFile = json.dumps(tone_analysis, indent=2)
    # cleanJSON(jsonFile, "text.txt")
    # # print(json.dumps(tone_analysis, indent=2))
    #
    #


main()
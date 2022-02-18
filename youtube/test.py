from youtube_transcript_api import YouTubeTranscriptApi
import sys
import json
from requests_html import HTMLSession

id = sys.argv[1]


title = HTMLSession().get('https://www.youtube.com/watch?v=' + id).html.find('title', first=True).text


result = {}
transcript = YouTubeTranscriptApi.get_transcript(id, languages=['de'])
text = ""
lines = []

word_count = 0

for line in transcript:
	word_count += len(line['text'].split())
	lines.append(line['text'])

print("word_count = " + str(word_count))

result['title'] = title.replace(" - YouTube", "")
result['video_id'] = id
result['transcript'] = lines
# result['transcript_was_automatically_generated'] = transcript.is_generated


json_string = json.dumps(result, ensure_ascii=False).encode('utf8')
print(json_string.decode())
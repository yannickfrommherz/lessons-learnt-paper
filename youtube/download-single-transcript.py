from youtube_transcript_api import YouTubeTranscriptApi
import sys
import json
from requests_html import HTMLSession

RESULTS_DIR = "results/"

if len(sys.argv) != 2:
	exit(1)

id = sys.argv[1]

title = HTMLSession().get('https://www.youtube.com/watch?v=' + id).html.find('title', first=True).text

result = {}
transcript = YouTubeTranscriptApi.get_transcript(id, languages=['de'])
text = ""
lines = []

for line in transcript:
	lines.append(line['text'])

result['title'] = title.replace(" - YouTube", "")
result['video_id'] = id
result['transcript'] = lines

json_string = json.dumps(result, ensure_ascii=False, indent=4).encode('utf8')
open(RESULTS_DIR + id + ".json", "w").write(json_string.decode())
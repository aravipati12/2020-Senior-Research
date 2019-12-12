from gensim.summarization.summarizer import summarize

def find_sections(text, segments):
    count, num, bottom_index = 0, 1, 0
    toReturn = []
    for i in range(len(text)):
        if text[i] == ".":
            count += 1
        if(count == (segments * num)):
            section = text[bottom_index:i]
            bottom_index = i + 1
            toReturn.append(section)
            num += 1
    toReturn.append(text[bottom_index:])
    return toReturn


f = open("transcript.txt", "r")
text = f.read()
text = text.replace(" %HESITATION", ".")
#text = "Yesterday I planned to play basketball and football. However, I only played football. It was a sunny and warm day. I went with friends. I scored 2 touchdowns. Afterwards we went to get food at a restaurant. I came home at 10 PM and slept."
#print(text)
count = text.count(".")
segments = (int)(count / 5)
sections = find_sections(text, segments)
summary = ""
for i in sections:
    summary += summarize(i) + " "
f = open("transcript.txt", "w+")
f.write(summary)
f.close()

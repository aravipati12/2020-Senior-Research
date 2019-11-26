# from textteaser import TextTeaser
# tt = TextTeaser()
# tt.summarize("Summary", transcript)

from gensim.summarization.summarizer import summarize
# f = open("transcript.txt", "r")
text = "Yesterday I went to play basketball. It was a sunny and warm day. I went with friends. Afterwards we went to get food at a restaurant. I came hom at 10 PM."

print(summarize(text))
#Yesterday I went to play basketball.

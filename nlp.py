from transformers import pipeline
import textstat
nlp = pipeline("fill-mask")
f = open("CommonWords.txt", "r")



string=input()
print("Input text: "+string)
words=string.split()
for w in words:
    if textstat.flesch_reading_ease(w)<60:
        string=string.replace(w,f"{nlp.tokenizer.mask_token}")



        preds=nlp(string)


        print()
        f.seek(0)
        j=0

        for p in preds:
            f.seek(0)


            while True:
                s = f.readline()
                if not s:
                    break

                if s.strip()==nlp.tokenizer.decode([p['token']]).strip():
                    string=string.replace(f"{nlp.tokenizer.mask_token}",s.strip())

                    j=1

                    break
            if j==1:
                break



print("Output text: "+string)
















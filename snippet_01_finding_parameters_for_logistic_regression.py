# given text
text1 = ["I am happy because I am learning NLP", "I hated that movie", "I love working at DL"]
# defining an all_text variable to store the whole text
all_text = ""
# combining each sentences into one sentence
for i in text1:
    all_text = (all_text +" "+ i)
# getting total wors in the text
total_words = all_text.split()
# getting unique words in the text
unique_words = list(set(total_words))
# getting the number of parameters the logistic regression needs to train
no_of_param = len(unique_words) + 1
print (f"The number of parameters the Logistic Regression needs to learn is: {no_of_param}")



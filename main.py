import streamlit as st  
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('punkt')
nltk.download('brown')


import time
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('sentipy.jpg')
st.image(image, use_column_width=True)
# Fxn
def convert_to_df(sentiment):
	sentiment_dict = {'polarity':sentiment.polarity,'subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['metric','value'])
	return sentiment_df

def analyze_token_sentiment(docx):
	analyzer = SentimentIntensityAnalyzer()
	pos_list = []
	neg_list = []
	neu_list = []
	for i in docx.split():
		res = analyzer.polarity_scores(i)['compound']
		if res > 0.1:
			pos_list.append(i)
			pos_list.append(res)

		elif res <= -0.1:
			neg_list.append(i)
			neg_list.append(res)
		else:
			neu_list.append(i)

	result = {'positives':pos_list,'negatives':neg_list,'neutral':neu_list}
	return result 




		






def main():
	st.title("Pratikriya- A Sentiment Analysis NLP App")
	st.subheader("Pratikriya- A Feedback Analysis Tool")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		with st.form(key='nlpForm'):
			raw_text = st.text_area("Enter Text Here")
			submit_button = st.form_submit_button(label='Analyze')

		# layout
		col1,col2 = st.columns(2)
		if submit_button:

			with col1:
				st.info("Results")
				sentiment = TextBlob(raw_text).sentiment
				st.write(sentiment)

				# Emoji
				if sentiment.polarity > 0:
					st.markdown("Sentiment:: Positive :smiley: ")
				elif sentiment.polarity < 0:
					st.markdown("Sentiment:: Negative :angry: ")
				else:
					st.markdown("Sentiment:: Neutral 😐 ")

				# Dataframe
				result_df = convert_to_df(sentiment)
				st.dataframe(result_df)

				# Visualization
				c = alt.Chart(result_df).mark_bar().encode(
					x='metric',
					y='value',
					color='metric')
				st.altair_chart(c,use_container_width=True)



			with col2:
				st.info("Token Sentiment")

				token_sentiments = analyze_token_sentiment(raw_text)
				st.write(token_sentiments)






	else:
		st.subheader("About")
		col1, col2, col3, col4, col5 = st.columns(5)
		with col1:
			st.subheader("**Supervisor**")
			st.image("pankajsir.jpg", caption='Dr. Pankaj Sharma', use_column_width=True)

		with col2:
			st.subheader("**Co-supervisor**")
			st.image("fink.jpg", caption='Dr. L. Dee Fink',use_column_width=True)

		with col3:
			st.subheader("**Co-supervisor**")
			st.image("manoj.jpg", caption='Dr. Manoj Kannan',use_column_width=True)

		with col4:
			st.subheader("**Creator**")
			st.image("ashish.jpg", caption='Ashish Katyal',use_column_width=True)


		with col5:
			st.subheader("**Special Thanks**")
			st.image("bitslogo.jpg", caption='BITS-Pilani',use_column_width=True)

if __name__ == '__main__':
	main()
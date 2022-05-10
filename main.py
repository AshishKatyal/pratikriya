import streamlit as st  
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('punkt')
nltk.download('brown')

import time
import matplotlib.pyplot as plt
from PIL import Image
st.set_page_config(page_title="Pratikriya-The Sentiment Analysis App")
image = Image.open('sentipy.jpg')

st.image(image, use_column_width=True)


# Fxn
def convert_to_df(sentiment):
	sentiment_dict = {'polarity':sentiment.polarity,'subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['metric','value'])
	return sentiment_df

def convert_to_df1(vs):
	sentiment_dict1 = {'Positive':vs['pos']*100,'Negative':vs['neg']*100,'Neutral':vs['neu']*100}
	sentiment_df1 = pd.DataFrame(sentiment_dict1.items(),columns=['metric','value'])
	return sentiment_df1




		






def main():
	#st.title("Pratikriya- A Sentiment Analysis NLP App")
	#st.subheader("Pratikriya- A Feedback Analysis Tool")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		#st.title("**Please Enter Your FeedBack**")
		with st.form(key='nlpForm'):
			raw_text = st.text_area("Please Enter Your Feedback")
			submit_button = st.form_submit_button(label='Analyze')
			
			
		# layout
		col1,col2 = st.columns(2)
		if submit_button:

			with col1:
				st.write("**Your Feedback has:**")
				sentiment = TextBlob(raw_text).sentiment
				#st.write(sentiment)

				# Emoji
				#if sentiment.polarity > 0:
					#st.markdown("Sentiment:: Positive :smiley: ")
				#elif sentiment.polarity < 0:
					#st.markdown("Sentiment:: Negative :angry: ")
				#else:
					#st.markdown("Sentiment:: Neutral 😐 ")

				# Dataframe
				result_df = convert_to_df(sentiment)
				st.dataframe(result_df)

				# Visualization
				c = alt.Chart(result_df).mark_bar().encode(
					x='metric',
					y='value',
					color='metric')
				st.altair_chart(c,use_container_width=True)
				with st.expander("Polarity"):
					 st.info("""
					 The polarity score is a float within the range of -1.0 to 1.0. Where +1 means Positive Statement and -1 means Negative Statement""")
				with st.expander("Subjectivity"):
					 st.info("""
					 The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective or refers to FACTUAL INFORMATION and 1.0 is very subjective. Subjective sentences generally refers to Personal Opinion, Emotions or Judgement""")


			with col2:
				st.write("**Sentiment Analysis**")
				analyzer = SentimentIntensityAnalyzer()
				vs = analyzer.polarity_scores(raw_text)
				
				

				

				
				#token_sentiments = analyze_token_sentiment(raw_text)
				#st.write(token_sentiments)
				# Dataframe
				result_df1 = convert_to_df1(vs)
				st.dataframe(result_df1)

				# Visualization
				c1 = alt.Chart(result_df1).mark_bar().encode(
					x='metric',
					y='value',
					color='metric')
				st.altair_chart(c1,use_container_width=True)

				#st.write("Overall sentiment dictionary is : ", vs)
				st.write("Feedback was rated as ", vs['neg']*100, "% Negative")
				st.write("Feedback was rated as ", vs['neu']*100, "% Neutral")
				st.write("Feedback was rated as ", vs['pos']*100, "% Positive")
				st.write("**Overall Feedback Rated As**", end = " ")

				# decide sentiment as positive, negative and neutral
				if vs['compound'] >= 0.05 :
					st.markdown("Positive :smiley: ")

				elif vs['compound'] <= - 0.05 :
					st.markdown("Negative :angry: ")

				else :
					st.markdown("Neutral 😐 ")

				#with st.expander("Hindi Translation"):
					#senti = TextBlob(raw_text)
					#st.text(senti.translate(to="hi"))
					#st.success('**Pratikriya** का उपयोग करने के लिए धन्यवाद')
					#st.info("""
					#The compound score is the sum of positive, negative & neutral scores which is then normalized between -1(most extreme negative) and +1 (most extreme positive). The more Compound score closer to +1, the higher the positivity of the text.""")

			



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

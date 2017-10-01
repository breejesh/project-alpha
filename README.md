
# What is Truenet?
In it's core form truenet is an API written in Python(flask). It uses Natural Language Processing (NLTK, Gensim) to make sense out of the input sentence and compares it to news from credible sources and returns a result based on analysis carried out. This API can thus be used to make simple Chrome plugin for checking rumours and likewise for Android.

# Why is it needed?
From currency to salt, very little escaped the reach of fake or fabricated news in 2016. Rumours spread from WhatsApp and other social media into the mainstream media. Institutions such as Unesco and the Reserve Bank of India (RBI) had to step in and tell
us what was true. Even Facebook and Google, two of the worlds biggest internet companies, sat up and took notice.

# How do I use it?
1. Download the repository or clone it 
2. Install all the dependencies
3. Run test.py for command line testing and flask.py for API

OR

Give a POST call to the API http://ryuzaki.pythonanywhere.com/api/v1/analyze with a string input.
e.g.
```javascript
$.ajax({
		url: "http://ryuzaki.pythonanywhere.com/api/v1/analyze",
		type: "post",
		contentType: "application/json; charset=UTF-8",
		data: JSON.stringify("Some query here"),
		datatype: 'json',
		success: function (data) { }
});
```
OR

Simply go to [truenet.cf](http://truenet.cf) and use it via our website.

*NOTE: The database we have used to analyse queries was last updated on 25th September, 2017. Queries pertaining to events occurring post 25th September will not produce accurate results. The reason for maintaining an offline database of our sources was to increase speed and efficiency. In the future, we plan to update the database periodically.*

# Flow
![image](https://i.imgur.com/E6AR3ZO.png)

# Video demonstration
Click the below image to view the video

[![image](http://img.youtube.com/vi/wRG0eYjrMEc/0.jpg)](https://youtu.be/wRG0eYjrMEc)  

```


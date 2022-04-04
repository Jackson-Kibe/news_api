from flask import Flask,render_template   # imported render-template to be able to render html templates
from newsapi import NewsApiClient

app = Flask(__name__) #Creating an app instance

@app.route("/") #Creating a home route
def bbc(): #Home route definition to bbc
    api_key = '7211d8d601cb4ac0a63c18c28b94010b'
    
    newsapi = NewsApiClient(api_key=api_key)

    #for top headlines of the news, sourse is where it comes from
    top_headlines = newsapi.get_top_headlines(sources = "bbc-news")
    all_articles = newsapi.get_everything(sources = "bbc-news")

    #fetch all articles from the headlines 
    t_articles = top_headlines['articles']
    a_articles = all_articles['articles']

    #a list of content to store value on that list
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    #fetch all content of articles using loop
    for i in range (len(t_articles)):
        main_article = t_articles[i]

    #appendall the content in to each of the list
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []   
    url_all = []

    for j in range(len(a_articles)): 
        main_all_articles = a_articles[j]   

        news_all.append(main_all_articles['title'])
        desc_all.append(main_all_articles['description'])
        img_all.append(main_all_articles['urlToImage'])
        p_date_all.append(main_all_articles['publishedAt'])
        url_all.append(main_article['url'])
        
        all = zip( news_all,desc_all,img_all,p_date_all,url_all)

    return render_template('bbc.html',contents=contents,all = all)


if __name__ == '__main__':
    app.run(debug=True)
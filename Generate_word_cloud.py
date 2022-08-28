import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def get_content(query):
    # get matching title or suggestion for given query
    title = wikipedia.search(query)

    # get wikipedia page for selected title
    page = wikipedia.page(title)

    # get content of that page
    Content = page.content

    return Content


def generate_wc(text):
    # create numpy array for wordcloud mask image
    custom_mask = np.array(Image.open('cloud.png'))

    # create set of stopwords
    stopwords = set(STOPWORDS)

    # create wordcloud object
    word_cloud = WordCloud(background_color='white', max_words=200, mask=custom_mask, stopwords=stopwords,
                           contour_width=3)

    # generate wordcloud
    word_cloud.generate(text)

    # plotting wordcloud
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    print('------------ Generate Wordcloud ------------')

    # get query
    while True:
        Query = input('Enter your query : ')
        print()

        try:
            Text = get_content(Query)
            generate_wc(Text)
            break
        except:
            print("An error occured. Try with something different query!")
            print()

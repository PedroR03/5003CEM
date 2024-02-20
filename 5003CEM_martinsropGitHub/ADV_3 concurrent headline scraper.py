import newspaper
from newspaper import Article
import concurrent.futures

'''get headline non-concurrent'''
def get_headlines():

    #list URLs used
    URLs = ['http://www.foxnews.com/', 
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',
            'http://global.chinadaily.com.cn/',
            'https://www.dailymail.co.uk/',
            'https://www.nbcnews.com/',
            'https://www.nytimes.com/']

    for url in URLs: #this goes through all URLs
        result = newspaper.build(url, memoize_articles=False) #picks the information of all urls
        print('\n''The headlines from %s are' % url, '\n')
        for i in range(1,6): #go through 5 times 
            art = result.articles[i] #get the articles from the result 
            art.download() #download article
            art.parse() #parse the article so can print the title
            print(art.title) 


def result(url):
    result = newspaper.build(url, memoize_articles=False) #pick the information of the url and return it
    return result

'''get headlines concurrent'''
def concurrent_get_headlines():

    #list of URLs used
    URLs = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',
            'http://global.chinadaily.com.cn/',
            'https://www.dailymail.co.uk/',
            'https://www.nbcnews.com/',
            'https://www.nytimes.com/']

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: #initiates the concurrent code with max of 5 
        future_to_url = {executor.submit(result, url ): url for url in URLs} #set the fucntion to run with concurrent code
        for future in concurrent.futures.as_completed(future_to_url): 
            url = future_to_url[future] #gets the resul of url
            print('\n''The headlines from %s are' % url, '\n')
            for i in range(1, 6): #go through the 5 news
                art = future.result().articles[i]  #get the result 
                art.download() #download the article
                art.parse()  #parse the article so can print the title
                print(art.title) 



if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=5)/5 #Run the concurrent code and counts the time at the start and at the end stops the time
    elapsed_time2 = timeit.timeit("concurrent_get_headlines()", setup="from __main__ import concurrent_get_headlines", number=5)/5 #Run the non concurrent code and counts the time at the start and at the end stop the time
    print(elapsed_time, elapsed_time2) 
import urllib.request, urllib.error,sys

def result_txt(name):
    f = open("links.txt", "a")
    f.write(name + "\n")
    f.close()

def main():
    for i in range(len(link)):
        try:
            try:
                name = link[i]+username
                conn = urllib.request.urlopen(name)
            except urllib.error.HTTPError as e:
                    # Return code error (e.g. 404, 501, ...)
                print(name,'not found, reason >> HTTPError: {}'.format(e.code))
            except urllib.error.URLError as e:
                    # Not an HTTP-specific error (e.g. connection refused)
                print(name,'not found, reason >> URLError: {}'.format(e.reason))
            else:
                    # 200 ok
                print(name,'Found !!!')
                result_txt(name)
        except:
            print("Your connection Bad or the website blocked by your country, Plz wait a sec\nskipping this site ........")

if __name__=="__main__":
    while True:
        print("Social Media Checker \nAuthor = github.com/Anasg4\n")
        #U have your own links ? add here
        ask= input("Do u have your own link \n(rename your link list be mylinks.txt in same directory)\n if not u using default links from this program \ny/n ??")
        if ask == 'n':
            link = [
                'https://steamcommunity.com/id/', 'https://www.last.fm/user/', 'https://photobucket.com/u/',
                'https://www.dailymotion.com/', 'https://twitch.tv/', 'https://www.ebay.com/usr/',
                'https://www.reddit.com/user/', 'https://www.tripadvisor.co.uk/Profile/', 'https://www.kongregate.com/', 'https://ask.fm/',
                'https://about.me/', 'https://www.meetme.com/', 'https://myspace.com/', 'http://kik.me/',
                'https://www.instagram.com/', 'https://www.youtube.com/', 'https://www.facebook.com/',
                'https://twitter.com/', 'https://tiktok.com/@', 'https://www.pinterest.com/',
                'https://id.linkedin.com/in/'
            ]
        else:
            linknew = open("mylinks.txt", "r")
            link= linknew.read().split('\n')
        username = input("\nInput Username Target: ")
        main()
        print("\nThe Found Links are saved in links.txt")
        a = input("\nDo u want use this tool again ? y/n >> ")
        if a == 'y':
            continue
        else:
            print ("\nThx u for using this Tools ^^v")
            sys.exit()

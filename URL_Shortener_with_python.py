
import requests


def shorten_link(Full_link, Link_name):
    API_Key = 'c04627c9417fd00f66e357c4a56f32dd83d12'
    Base_URL = 'https://cutt.ly/api/api.php'

    parameter = {'key': API_Key, 'short': Full_link, 'name': Link_name}
    request = requests.get(Base_URL, params=parameter)
    data = request.json()
    # print(data)

    try:
        short_Link = data['url']['shortLink']
        print('Shorten Link : ', short_Link)
        print()
        print("The link has been shortened !")

    except:
        status = data['url']['status']
        if status == 1:
            print(
                'The shortened link comes from the domain that shortens the link, i.e. the link has already been '
                'shortened')

        elif status == 2:
            print('The entered link is not a link')

        elif status == 3:
            print('The preferred link name is already taken')

        elif status == 4:
            print('The Invalid API key')

        elif status == 5:
            print('The link has not passed the validation. Includes invalid characters')

        elif status == 6:
            print('The link provided is from a blocked domain')


if __name__ == '__main__':
    Link = input('Enter a link : ')
    title = input('Give your link a name : ')
    shorten_link(Link, title)

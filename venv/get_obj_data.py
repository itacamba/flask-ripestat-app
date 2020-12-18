import requests


def get_data_for(obj, obj_type):
    print(obj)
    if obj_type == "inetnum":
        r = requests.get(f'https://stat.ripe.net/data/whois/data.json?resource={obj}')
        data = r.json()['data']['records'][0]
        print(data)
        return data
    # elif obj_type == "organisation":

        # return render_template('ripe_object.html', data=data)
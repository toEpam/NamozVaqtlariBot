class Text:
    today = "☪️ Bugungi namoz vaqtlari"


class Regions:
    toshkent = 'Toshkent'
    quqon = 'Qoqon'
    andijon = 'Andijon'
    buxoro = 'Buxoro'
    guliston = 'Guliston'
    samarqand = 'Samarqand'
    namangan = 'Namangan'
    navoiy = 'Navoiy'
    jizzah = 'Jizzax'
    nukus = 'Nukus'
    qarshi = 'Qarshi'
    xiva = 'Xiva'
    fargona = 'Fargona'


def get_regions_names(): 
    # Assuming Regions is defined elsewhere
    return [region for region in
            list(map(str, Regions.__dict__.values())) if not
            region.startswith('__') and not region.startswith('<')]
    # return [
    #     region
    #     for region in Regions.__dict__.values()
    #     if all(x not in region for x in ['_', '<'])
    # ]



if __name__ == '__main__':
    print(get_regions_names())

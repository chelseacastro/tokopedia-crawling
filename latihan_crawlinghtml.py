import requests
import json

url = "https://www.tokopedia.com/p/komputer-laptop/komponen-komputer/vga-card?ob=5&page=1"

payload={}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'cookie': '_UUID_NONLOGIN_=8c27c5579bafa704bf997b909aee509b; _UUID_NONLOGIN_.sig=HneJ1-jcbXr9asekhOAGhB2xlPM; _gcl_au=1.1.573440469.1656828978; DID=ea80dc43850b88ddc33898f0363f38d9adbe45a2efb9aeaf1fb6089f8c299832b2b35872502302a3ed9fcfb6544b2e93; DID_JS=ZWE4MGRjNDM4NTBiODhkZGMzMzg5OGYwMzYzZjM4ZDlhZGJlNDVhMmVmYjlhZWFmMWZiNjA4OWY4YzI5OTgzMmIyYjM1ODcyNTAyMzAyYTNlZDlmY2ZiNjU0NGIyZTkz47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _UUID_CAS_=2d665481-71d7-41da-9d59-b1653633da98; _CASE_=70296f426f293139393c3f27296a426f29313b2729676967293129416a606a797f6a2b5b7e786a7f29272968426f29313a3c3d27296764656c293129292729676a7f2931292927297b48642931292927297c426f29313a39393a3b383c3e272978426f29313a3a3e383b3e3c382729785f727b6e29312939632927297c6378293129507057297c6a796e63647e786e54626f5729313a39393a3b383c3e275729786e797d62686e547f727b6e57293157293963572927572954547f727b6e656a666e57293157295c6a796e63647e786e78572976277057297c6a796e63647e786e54626f5729313b275729786e797d62686e547f727b6e57293157293a3e66572927572954547f727b6e656a666e57293157295c6a796e63647e786e78572976562976; __auc=893da878181c2b3fb999ed8ad51; _gcl_marco=1.1975289966.1656828984; _gcl_dc=GCL.1657036988.CjwKCAjwwo-WBhAMEiwAV4dybdPLkZyMorDmLC8QFIfBQDCl4lwpnveOOITCR8jve-GlWgICQZF3qBoCtnwQAvD_BwE; _gcl_aw=GCL.1660022074.CjwKCAjw6MKXBhA5EiwANWLODNd7KtygHUc-Ib-3_mPxKt8v8l2T-g2O52FKfLZAoh2btiBwf4DemRoCDq8QAvD_BwE; _gac_UA-126956641-6=1.1660022078.CjwKCAjw6MKXBhA5EiwANWLODNd7KtygHUc-Ib-3_mPxKt8v8l2T-g2O52FKfLZAoh2btiBwf4DemRoCDq8QAvD_BwE; _gac_UA-9801603-1=1.1660022128.CjwKCAjw6MKXBhA5EiwANWLODNd7KtygHUc-Ib-3_mPxKt8v8l2T-g2O52FKfLZAoh2btiBwf4DemRoCDq8QAvD_BwE; g_state={"i_p":1660108583840,"i_l":2}; _jxx=8c0e60e0-0a99-11ed-b70c-a1cafb7b0b38; _jxx=8c0e60e0-0a99-11ed-b70c-a1cafb7b0b38; _jx=8c0e60e0-0a99-11ed-b70c-a1cafb7b0b38; _jx=8c0e60e0-0a99-11ed-b70c-a1cafb7b0b38; _abck=F82A9B5645F6A0F3B14163B14D9764FC~0~YAAQlSE1Fywg7YCDAQAAdiegjgh4F5VHjHgRBOX8b6Ygl6KIV6BzULxDEFXaFFxhCfZUF/S7K+Rbt+cbJHA8KJ96eUZai5H7hXY1xzRp7GgOyF+o69urMNOmHWOuUAzQGNTvomHwKkNKc1JkuIiLS5kpkzkcd6NYLgncjGJvxIg20Bjrysb8E4ZcKGplHSiLKXAXAqz0E4a1cDvIoAhr/p4ak+3G/Njes9tFrGHS5V8NyejfIcn/RJ8ujxQRti+7YGGjrRqjrvfQfwDQdzIucswiI5xYjeQYzy1q3jq5V53uqZJ7unEl17flUngWk2S8/gb5OS7plSx/kpMoufo/BRnRPMlf8BdDQyw+mZ+oOY+3buEaB78Npx3EAz9pzz0tGp3590UUaCxRT8PMJuyEFLvdS1q3kleUUKzh~-1~-1~-1; bm_sz=7313EA3D57D3798B87FAF954F76438D5~YAAQlSE1Fy0g7YCDAQAAdiegjhHAiJZ9DbVJVlShnzIWtDASHwLLDUvgKVTk9+UeZe5eCOHBdQ5B0WThJ8ZI8RCXYVzSu0BNF2DsnAW+GvNBIYyEbKIzHsP5iuv0EpogTjWDojsdCpxvjvTw+cp/0IavFUDmio+lpSSmtw8E9NIzMl8IHPr1eiKNdLbeTEbXgvax/nVUaoEiLMuGTPSsKub0GEEzNQT6noQMho3RLDuCAIJh3wVyUE/iRp0kgRBQoikT8wIfJQJBfsEeLqh+wDLypxjIVlcrgkmBU0M4eP3E4eAslDw=~3617346~3684662; _gid=GA1.2.1120234076.1664545207; _SID_Tokopedia_=6tYhkoqDhLJxYUenUWxvob8WGzOI9y5DKht4M4By7lz_44paHLrOKjC2WUu-qHYID3s60902bWBZWAuBaUDq3fUF5nie2yRxNolQ_zdoifvfASK1rtM2afu4sVhc5mAb; AMP_TOKEN=%24NOT_FOUND; __asc=143eb4521838ea04fed05e6c7e6; bm_mi=B22D003D859404E900FB49104582B30E~YAAQjyE1F99ZUliDAQAAGvmxjhEgPAw7rL7O48YQDpV+xBVNny997KwOjQcJvCd2TKriMSK/SC63P4IL+vsiD5I4ORGgySNfFFqR9ksfyuuiPSFfowqzeFuFHga6RvUGEnRshOTV+GROCPT9okt3j4kstK+QzbbesBIP3UUJ3Lm+QDJolA3xHXYsCCq4n1GTP0w+NrEJ8rikJa9IDYlw9nqG/mD/S4sV8YlnTIY26MP2PEC2dJmpNoMnHt1to+LkzrFrRHA/OVGmWEjtPPY7vAGN02T/S6PH48CAzVLW3GtlZPL1//5D9qixJ2HD0frVqTuRXC02Rjj2cxnvVomYoBsuct7bHDEG2l0GFd8ywMehUTZAE8STdXkXgpg=~1; ak_bmsc=326FADF8483E1F7357D0E88D8EA5E2C9~000000000000000000000000000000~YAAQjyE1FxpbUliDAQAALUayjhHGFUWvT6Zz5T/vmFh/HsJ5jMvaXBk+Gvnv3mVDsfPirz0sKJyRYSX+Plz1sCJmmiuHXzu7Xxu1kVkjAlbvnp5Yj7HqfPp87vKAlTD2lF+e4ijFdjL9BR3pofQ5gjukaqUqn191xS9auTPyRfwEl0++7H0SFpl+v4cO9+ONqVR99fjhs5t6O0c4iJdd32AMcvPnR1tM43eWqUGerwp1N1Q48ahtHRVi1roe8/EKwKT0OPYTu8OM1a86cHBl5HYTWoCoBy9g+fYEIfsLmImlSwPotXzLziNWG2F64LCaOIUXaZHacUDZD7WYc4C5Xkf4IEwf8yzI0e2GIaKFPk96w9AXYmTmEDY6rio+tWN75k+n8bQOrtnFkGUPC9UC5u+nUSqcXde2a5hMBLPCOVO0PzJu8g2V/jXtgUeBvA9chrdyxsseLV5VxNfjuFNEzJUMfQ41wq6LrvYE; serverECT=4g; _dc_gtm_UA-126956641-6=1; _gat_UA-9801603-1=1; _ga=GA1.2.1065013003.1656828979; bm_sv=D50EA939464ECDBBF207D8B6D3DD35D7~YAAQjyE1F42ZUliDAQAA4xO/jhF4vOU2aa57ixreiictX3iQwXu11fQqy17Gjng0VRZuKwajNkPNsoc7Q2ItoDkrO/ulNZ49GvNxdWivffBTZnxkmLA+1YRkPeSQnikUyot9XXItqY4Ag4187DyonOHj9DR8qzCcCRS3JmKikRua9BoHZJPP7RAvLKtvHwIGJ6LzS/e5+vYMUyXjYGBQxVY1NjQFcp1PVfOGiV0Pqh8HlAFEVXwrIXwOoiY8ikTFKkxJ~1; _ga_70947XW48P=GS1.1.1664545210.4.1.1664547254.14.0.0; ISID=%7B%22www.tokopedia.com%22%3A%22d3d3LnRva29wZWRpYS5jb20%3D.884102025296e4d88897c8b01d303d96.1664545209375.1660023545007.1664547254887.5%22%7D; _abck=F82A9B5645F6A0F3B14163B14D9764FC~-1~YAAQdcMmF3uEyI6DAQAAuXbTjghcItGgWnoPjRncqK2fA9iMGS77mC/2L3E9dni9PIKOHj0Qs/j4ebsB/RGd2ISOcC6RoPxRVWscH1PYEagUIcseoPaA2HDFTySO496ZfKtOwzwNwWTrXZ5c1QW/IQAiPIdu21I69Sq9V9NAP58J3Ig1HeqoQfWuCoS3K9myo7EwPxlXWox58ahg5TOeznCsZNKXIc5T/wPOeP+DYYMTg9DXnSYhtY2W3pitDsrlN/G7AlrorLyWhdDjSInnTlX6Sb4LgG1Nz2KPvPbVM6wy8JOqXbcyzbw3+pR4o5LGlN7+Z1ToZX6lfYmGtGIiC7yQutl0/LUpkXCRe6PYXMmQAQSueWyOJpBRH56k7xuXywFBdjsx1HOFVGnLwkEwObnaqsunBvF6NFm1~0~-1~-1',
  'dnt': '1',
  'ect': '4g',
  'referer': 'https://www.tokopedia.com/search?navsource=&page=1&q=xiaomi&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product%22)',
  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text.split('window.__cache=')[1].split(';\n    </script>')[0])

y = response.text.split('window.__cache=')[1].split(';\n    </script>')[0]

# print(x)

json_data = json.loads(y)
# json_data = json_data[0]
json_data1 = json_data['$ROOT_QUERY.searchProduct({"params":"ob=5&page=1&ob=5&identifier=komputer-laptop_komponen-komputer_vga-card&sc=3951&user_id=0&rows=60&start=1&source=directory&device=desktop&page=1&related=true&st=product&safe_search=false"})']
json_data2 = json_data1['products']
# json_data = json_data['id']
# json_data = json_data['data']

# print(json.dumps(json_data))
a = []

for x in json_data2:
    # a.append(x['id'])
    b = json_data[str(x['id'])]
    print(b['name'])
    # print(json_data[str(x['id'])])
# print(a)
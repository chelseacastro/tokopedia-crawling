import requests
import json
import psycopg2

for loop_data in range(10):
  url = "https://gql.tokopedia.com/graphql/TopadsProductQuery"

  payload = "[{\"operationName\":\"TopadsProductQuery\",\"variables\":{\"adParams\":\"dep_id=&device=desktop&ep=product&fcity=&item=20&minimum_item=10&navsource=&ob=23&page=1&q=minyak%20goreng%20tropical%202%20liter&shipping=&src=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&user_addressId=&user_cityId=176&user_districtId=2274&user_id=0&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=\"},\"query\":\"query TopadsProductQuery($adParams: String) {\\n  displayAdsV3(displayParams: $adParams) {\\n    data {\\n      clickTrackUrl: product_click_url\\n      product_wishlist_url\\n      product {\\n        id\\n        name\\n        wishlist\\n        image {\\n          imageUrl: s_ecs\\n          trackerImageUrl: s_url\\n          __typename\\n        }\\n        url: uri\\n        relative_uri\\n        price: price_format\\n        wholeSalePrice: wholesale_price {\\n          quantityMin: quantity_min_format\\n          quantityMax: quantity_max_format\\n          price: price_format\\n          __typename\\n        }\\n        count_talk_format\\n        countReviewFormat: count_review_format\\n        category {\\n          id\\n          __typename\\n        }\\n        categoryBreadcrumb: category_breadcrumb\\n        preorder: product_preorder\\n        product_wholesale\\n        free_return\\n        isNewProduct: product_new_label\\n        cashback: product_cashback_rate\\n        rating: product_rating\\n        ratingAverage: product_rating_format\\n        top_label\\n        bottomLabel: bottom_label\\n        labelGroups: label_group {\\n          position\\n          type\\n          title\\n          url\\n          __typename\\n        }\\n        campaign {\\n          discountPercentage: discount_percentage\\n          originalPrice: original_price\\n          __typename\\n        }\\n        customvideo_url\\n        __typename\\n      }\\n      shop {\\n        shopId: id\\n        name\\n        domain\\n        city\\n        tagline\\n        uri\\n        isOfficial: shop_is_official\\n        isPowerBadge: gold_shop\\n        badges {\\n          title\\n          imageURL: image_url\\n          show\\n          __typename\\n        }\\n        __typename\\n      }\\n      tag\\n      __typename\\n    }\\n    header {\\n      meta {\\n        ab_test\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}]"
  headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': '_UUID_NONLOGIN_=7f89975cce558139aa406fd1c71467c6; _UUID_NONLOGIN_.sig=_9lONw_2SzTazdPnicu_mbQshYo; bm_sz=A8865628E9B050793DFA856467044DBD~YAAQEqIAFxN9P4GDAQAAstuejhFj5GUuVIAez+qpsgXfautVN6khwCATpuuPxaDATBS4u8WSEesnfB1AuGmSWXZitme7LM6K/0O5k5dQ8Azgy8Lo+YWAHJBfyrfR3/steOcxpSc4k1uKJ5L6wyD5TxsCNQe9/w2S4x05SCeeTCsloCUzGeKtuRFKuT9ONCot8uDKM6uzNJ0tkh3lLk/afcEjW4PgXyoHUZnqZscfiJECir3RbXWsTmriowgEezVgBVFGkiy6erQJZa2OO0PJURVEvBoE9M91lyPZQ+9vndbbNzJ7/P8=~4604225~3617329; _gcl_au=1.1.1122374823.1664545113; _SID_Tokopedia_=ByxlleOA-_dCyQcPGmLHaid6ZP4afwFiCNGgDhr4QBkKh6qGkPquj47aoZSfIXnY9wH-za_uzAsO76ulOadKGl6EP8g1J9TyUqcbEMZALIlTGNSefSnpyJ8pE8JqT4Ty; DID=5d6cc958e821bb87c41090d4e7ebdb3c2f32ebb5def4af8e437fe76ca55fc56ccc27b76f0fd8d4191fb7d371696c98ba; DID_JS=NWQ2Y2M5NThlODIxYmI4N2M0MTA5MGQ0ZTdlYmRiM2MyZjMyZWJiNWRlZjRhZjhlNDM3ZmU3NmNhNTVmYzU2Y2NjMjdiNzZmMGZkOGQ0MTkxZmI3ZDM3MTY5NmM5OGJh47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _gid=GA1.2.561731760.1664545113; ak_bmsc=6D0D30153CAF3B81FFE930B1EFF4A008~000000000000000000000000000000~YAAQEqIAF159P4GDAQAAzOGejhEclFfJl3+1bSl2GVCUFwDCFTX2doqb655UIrqy93k5B/KJqFMsTSwhFnGLmIXgh7WV9P2F5E9Pd+7YYlcgJ3BWqwwjywhSLvObztJiZp/KI1bkJEIC0TDT2kJ5BIswZJG5iHocbBPYaACQtuD51ZCph3juinXfKESShNSYcJt3HFrMdUBOV2kJYBWLRgzfzvi9TRd/NYs+XHDprNN8HSbd9wgaoTSUM8pfg9Fq781CQBtdGXJ0JK4xbgIcO8jdMv+lYFGmKEXkAFj4t0rVu6cHzIIaqxzUXymB0qDCT5ac/j/MHocHyIN8KzK9jlDhwK5aaIaYHKL3sDMrSgKzzZlF6wXXmeu6cN8Qaj37KoqiZoZPoC4SWY0eWb8xcOFWPjtMopGiepWgPP6/TdSWNNlxrXic+NJ++RRpT3DRLpAAB4yrNkgI5OKzGtuD46Ba2a6bBk+3gCNmYKxz7Wsa4KBUxqiFUbWwVja+1DRl; _UUID_CAS_=c8f0ba46-3347-4a6d-bc6c-6d1b4e1fd46b; _CASE_=247d3b163b7d656d6d686b737d3e163b7d656f737d333d337d657d153e343e2d2b3e7f0f2a2c3e2b7d737d3c163b7d656e6869737d333031387d657d7d737d333e2b7d657d7d737d2f1c307d657d7d737d28163b7d656e6d6d6e6f6c686a737d2c163b7d656e6e6a6c6f6a686c737d2c0b262f3a7d657d6d377d737d28372c7d657d0424037d283e2d3a37302a2c3a00363b037d656e6d6d6e6f6c686a73037d2c3a2d29363c3a002b262f3a037d65037d6d37037d73037d00002b262f3a313e323a037d65037d083e2d3a37302a2c3a2c037d227324037d283e2d3a37302a2c3a00363b037d656f73037d2c3a2d29363c3a002b262f3a037d65037d6e6a32037d73037d00002b262f3a313e323a037d65037d083e2d3a37302a2c3a2c037d22027d737d330a2f3b7d657d6d6f6d6d726f66726c6f0b6d6f656c67656b6e746f68656f6f7d22; __asc=8da0cfa51838e9ed6c5f2148807; __auc=8da0cfa51838e9ed6c5f2148807; _fbp=fb.1.1664545118077.1354695159; _abck=4F2911DC5A0CEA8A6CFEF0A45A10EB17~0~YAAQEqIAF9l+P4GDAQAAIPuejgix6ElKuRHGFB1ObydTswk4sEjI+2jl6HA28hpjvhighdvV6Rd/TlIDIo62rjnIoAVcSB7Z8Wizb0sDU2oHU6yR7XSX3c4a6WPXdYKe/muc/nmFZ2UdJgj4V3SwhnfQi9Vmb7fyf6tpggORRLUtVzJ6VPXIv3czwTy5Ua2fnfv4gberrL3ZEGbaZgeoQ/CiAWypR1O3VqxZb0bk4xQ68x0/QG5h9SM/1vqxlnBhgg695+2tcitsJ0unSWwnBV4CrHVhwgX3NPDBuuO1W5a840S620hugdo9nHrMzfyikMTRUpGCp3kz+QeNi7VzQ493PfPjQa4FEBUyKhlXSk+GmIbTQ+fgiM3VHiovenK2yjv7TRCkj/+w8oY/mm84qDXaCrCA9+mp~-1~-1~-1; _jxx=3610a970-40c5-11ed-8b4f-11d07651358f; _jxxs=1664545127-3610a970-40c5-11ed-8b4f-11d07651358f; _jx=3610a970-40c5-11ed-8b4f-11d07651358f; _jxs=1664545127-3610a970-40c5-11ed-8b4f-11d07651358f; AMP_TOKEN=%24NOT_FOUND; _gat_UA-9801603-1=1; _dc_gtm_UA-126956641-6=1; _ga_70947XW48P=GS1.1.1664545113.1.1.1664545313.59.0.0; _ga=GA1.2.1917867079.1664545113; _dc_gtm_UA-9801603-1=1; _abck=4F2911DC5A0CEA8A6CFEF0A45A10EB17~-1~YAAQEqIAFxHiP4GDAQAAFuunjggOhiAzaYmmpSmBlJF0qJegU6HpJdMaYCbvihkopKqqC1pBhAXJMVAVU0y/Wuo15HaTjd+SnW5EVjUQNC6YjLX3icrCUMNneXlDcnrveK7tOzGp0+XcrRuDBF7UgR5jf9+j9TP+ktfh+jRjuvrnBj/d1DDYO/+QFng3KXz/ifL2QHIs6vpc0ZIXsRDWLJ9+rwYj+Xl7fJG1XPiC2edetRGmik6DnjfavLKFUzuwH4LOx/AEzfDoKVAWgmfsAoFt6C4/vCwFyU1dUXxsSX0p/0zNOirUqN6bt5HKp9XjFQHhrgrd5wVath+S9mOgpKjQmWkhSe+Te0KRXu0y97EZWYNzM9YLw073uvLhatWQqtpsnd86wnsUA48nvzdEqNZcF9wTK0wx~0~-1~-1',
    'iris_session_id': 'd3d3LnRva29wZWRpYS5jb20=.8a73633446d23463681d465bafce53bf.1664545113032',
    'origin': 'https://www.tokopedia.com',
    'referer': 'https://www.tokopedia.com/search?st=product&q=minyak%20goreng%20tropical%202%20liter&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-device': 'desktop-0.0',
    'x-source': 'tokopedia-lite',
    'x-tkpd-lite-service': 'zeus',
    'x-version': 'b5f4372'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  # print(response.text)

  json_data = json.loads(response.text)
  json_data = json_data[0]
  json_data = json_data['data']
  json_data = json_data['displayAdsV3']
  json_data = json_data['data']

  for x in json_data:
    product_name = x['product']
    shop_name = x['shop']
    nama = product_name['name']
    harga = str(product_name['price']).replace('Rp','').replace('.','')
    toko = shop_name['name']

    # print(product_name['name'])
    # print(product_name['price'])
    # print(shop_name['name'])

    try:
      connection = psycopg2.connect(user="postgres",
                                    password="ubuntu",
                                    host="192.168.18.130",
                                    port="5432",
                                    database="crawling")
      cursor = connection.cursor()
      postgres_insert_query = "insert into latihan_crawling values ('" + nama + "','" + harga + "','" + toko + "')"
      cursor.execute(postgres_insert_query)
      connection.commit()
      count = cursor.rowcount
      print(count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
      print("Failed to insert record into mobile table", error)

    finally:
      if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

import requests

url_base = "https://melcosurdistribuciones.e.org.pe/api/items/record"
bearer_token = "RO5uSj0mN9D1yt7MjGdLoEHutnaAcqjHpBSXyGyV52zNCaRsJW"

headers = {"Authorization": f"Bearer {bearer_token}"}


def get_products_info(products_data=[]):
    responses = []
    for product in products_data:
        try:
            response = requests.get(f"{url_base}/{product['id']}", headers=headers)
            if response.status_code == 200:
                # print(f"Solicitud exitosa para {url_base}/{id}")
                json_data = response.json()
                responses.append(
                    {
                        "id": product["id"],
                        "cantidad": product["cantidad"],
                        "tipo_precio": product["tipo_precio"],
                        "data": json_data,
                    }
                )
                print(json_data)
            else:
                print(
                    f"Fallo en la solicitud para {url_base}/{product} - Código de estado: {response.status_code}"
                )
        except Exception as e:
            print(f"Error al realizar la solicitud para {url_base}/{product}: {str(e)}")

    return responses

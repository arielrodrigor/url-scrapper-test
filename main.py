import requests
import xml.etree.ElementTree as ET


def extraer_urls_sitemap(url_sitemap):
    try:
        # Hacer una petición GET al sitemap
        respuesta = requests.get(url_sitemap)

        # Verificar que la petición fue exitosa
        if respuesta.status_code != 200:
            print(f"Error al acceder al sitemap: Estado {respuesta.status_code}")
            return []

        # Intentar analizar el contenido XML
        raiz = ET.fromstring(respuesta.content)

        # Extraer las URLs
        urls = [element.text for element in raiz.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

        return urls

    except ET.ParseError as e:
        print(f"Error al analizar XML: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url_del_sitemap = "www.example.com/sitemap.xml"  # Reemplaza con la URL del sitemap que deseas analizar
    urls = extraer_urls_sitemap(url_del_sitemap)
    print(urls)


from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class ChocolateProductLoader(ItemLoader):

    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x : x.split("£")[-1])
    url_in = MapCompose(lambda x: 'https://www.chocolate.co.uk' + x)

#     Item Loaders:
# Item Loaders, web sayfalarından alınan verileri (örneğin, bir ürünün adı, fiyatı, açıklaması gibi) düzgün bir şekilde işlemek ve düzenlemek için kullanılır.
# Bu verilerin bazen temizlenmesi, biçimlendirilmesi veya dönüştürülmesi gerekebilir. Örneğin, fiyatı bir ondalık sayıya dönüştürmek veya tarih formatını standartlaştırmak gibi.
# Item Loaders, bu veri işleme işlemlerini kolaylaştıran ve kodunuzu düzenli tutmanıza yardımcı olan bir araç seti sağlar.
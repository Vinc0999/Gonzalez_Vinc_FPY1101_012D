productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32],
         'GF75HD': [749990,2], 
         'UWU131HD': [349990,1] 
        }

def stock_marca(marca):
    for clave in productos:
            if marca.upper() == productos[clave][0].upper():
                  print(f"{productos[clave][0]} stock : {stock[clave][1]}")
                  
            else:
                  print("no se encuentra")

def búsqueda_precio(p_min,p_max):
        if p_min>=100000 and p_max<=200000 or p_max<=250000:
               print("no hay stock con esos precios")
               if p_min>=200000 and p_max>=300000:
                      print(f"computador :{stock[clave][0]}")
               for clave in stock[clave][0]:
                      print(f" producto: {productos[clave][0]}precios: {stock[clave][0]}")
        else:
               print("valor no valido")
                     
                        
def actualizar_precio(modelo, p) :
        
        for clave in productos:
               if modelo == productos[clave][0]:
                      print("producto encontrado")
                      print(f"producto {productos[0]}")
                      

                      
                             


                

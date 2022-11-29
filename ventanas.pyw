import webbrowser#Esta libreria nos ayuda a trabajar con navegadores

#En la siguiente variable debemos introducir la o las urls a las que queremos acceder
urls = ['']

aux = 0
for x in urls:
    #Podemos trabajar con varios navegadores, en este caso usamos chrome
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
        #La funcion BackgroundBrowser nos pide un parametro, este es la ruta en donde tenemos guardado el ejecutable del navedor
        "C:\Program Files\Google\Chrome\Application\chrome.exe"))

    webbrowser.get('chrome').open(urls[aux])
    aux += 1
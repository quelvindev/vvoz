import flet as ft
import screeninfo as esif

class HomePage:

    def __init__(self,page:ft.Page= None):
        self.page = page
        monitor = esif.get_monitors()[0]
        screen_width = monitor.width*0.4
        screen_height = monitor.height*0.3
        page.title = 'Donwload de Vídeos'
        page.window.alignment = ft.alignment.center
        page.window.width = screen_width
        page.window.height = screen_height
        #inputs = self.column_one(screen_width,screen_height)
        #page.add(inputs)
        page.update()


def run(page: ft.Page):
    app_instance = HomePage(page)
   
ft.app(target=run)
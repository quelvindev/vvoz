import flet as ft
import screeninfo as esif
from machine.gerador import Gerador

class HomePage:

    def __init__(self,page:ft.Page= None):
        self.page = page
        self.fragment = Gerador()
        monitor = esif.get_monitors()[0]
        screen_width = monitor.width*0.4
        screen_height = monitor.height*0.3
        page.title = 'Donwload de Vídeos'
        page.window.alignment = ft.alignment.center
        page.window.width = screen_width
        page.window.height = screen_height
        inputs = self.column_one(screen_width,screen_height)
        page.add(inputs)
        page.update()
        
    
    def getClear(self,e):
        
        if self.text.value.strip():
            self.text.value = ''
            self.text.focus()
            self.page.update()
        self.text_info.spans = [ft.TextSpan("Aguardando texto",
                    ft.TextStyle(weight=ft.FontWeight.BOLD),)]
    def gettext(self,e):
         
         self.page.update()
         if  self.text.value.strip():
            self.text_info.spans = [ft.TextSpan("Texto coletado",
                    ft.TextStyle(weight=ft.FontWeight.BOLD,color='#445588'),)]
            self.page.update()
            self.text_info.spans = [ft.TextSpan("Gerado Audio Original",
                    ft.TextStyle(weight=ft.FontWeight.BOLD,color="#444E88"),)]
            self.fragment.create_folder_voz()
            self.page.update()
            self.text_info.spans = [ft.TextSpan("Gerado audio Padrão",
                    ft.TextStyle(weight=ft.FontWeight.BOLD,color="#314EA5"),)]
            self.fragment.generate_audio(self.text.value)
            self.text_info.spans = [ft.TextSpan("Audio gerado!",
                    ft.TextStyle(weight=ft.FontWeight.BOLD,color="#6E7DAA"),)]
            self.page.update()

         
    def copy_pix(self):
        ...
    def playaudio(self,e):
        self.fragment.play_audio()  
    def column_one(self,screen_width,screen_height):

        self.text = ft.TextField(   label="Texto",
                                    hint_text='Cole o texto aqui!',
                                    autofill_hints=ft.AutofillHint.NAME,
                                    height = screen_height,
                                    autofocus=True,
                                    multiline=True,
                                    min_lines=10)
        self.text_info = ft.Text(   color="#000000",
                                    selectable=True, 
                                    spans=[ft.TextSpan("Aguardando texto",
                                                        ft.TextStyle(weight=ft.FontWeight.BOLD),
                                                        ),])
        self.btn_clear = ft.IconButton(
                                    icon=ft.Icons.CLEAR,
                                    icon_color="#F7513B",
                                    icon_size=30,
                                    tooltip='Limpar',
                                    alignment=ft.alignment.center,
                                    on_click=self.getClear)
        self.btn_convert =  ft.FilledButton(
                                            text="Gerar",
                                            width=screen_width*0.2,
                                            height=50,
                                            on_click= self.gettext)
        self.btnplay =  ft.FilledButton(
                                            text="Play",
                                            width=screen_width*0.2,
                                            height=42,
                                            icon=ft.Icons.PLAY_ARROW_SHARP,
                                            color="#FFFFFF",
                                            style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(radius=0),  
                                                    padding=0 ,bgcolor="#562FC0"                                
                                                ),
                                            
                                            on_click=self.playaudio,
                                        )
        self.btn_stop = ft.IconButton(
                                    icon=ft.Icons.CLEAR,
                                    icon_color="#FFFFFF",
                                    #bgcolor="#562FC0",
                                     style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=0),  
                                                padding=10, 
                                                bgcolor="#562FC0"),
                                   # icon_size=60,
                                    tooltip='Parar',
                                    alignment=ft.alignment.center,
                                    
                                    on_click=self.getClear)
        self.column_left =  ft.Column(  expand=True,
                                        spacing=2,
                                        width= screen_width*0.7,
                                        height = screen_height,
                                        alignment=ft.MainAxisAlignment.START,
                                        controls=[ 
                                            ft.Container(content= 
                                                        self.text,
                                                        alignment=ft.alignment.top_left,
                                                        width=screen_width*0.7,
                                                        height = screen_height*0.68,
                                                        padding=0.5,
                                                        margin=0.5),
                                            ft.Divider( color="#FFFFFF"),
                                            ft.Container(content= 
                                                        self.text_info ,
                                                        bgcolor= "#D3D3D3",
                                                        alignment=ft.alignment.center_left,
                                                        width=screen_width,
                                                        height = screen_height*0.1,
                                                        padding=0.5,
                                                        margin=0.5,),
                                        ])
            
        self.column_right = ft.Column(  expand=True,
                                        spacing=2,
                                        width= screen_width*0.2,
                                        height = screen_height,
                                        
                                        alignment=ft.MainAxisAlignment.START,
                                        controls=[ 
                                                ft.Row([     
                                                        ft.Container(content=  
                                                                        self.btn_clear,
                                                                        alignment=ft.alignment.top_left,
                                                                        width=screen_width*0.05,
                                                                        height = screen_height*0.30,
                                                                        padding=0.005,
                                                                        margin=0.005),

                                                        ft.Container(content=
                                                                        self.btn_convert,
                                                                        alignment=ft.alignment.top_right,
                                                                        height = screen_height*0.30,
                                                                        padding=0.5,
                                                                        margin=0.5,
                                                                        width=screen_width*0.18) 
                                                        ]),
                                                    ft.Row([     
                                                        ft.Container(content=  
                                                                        self.btn_stop,
                                                                        alignment=ft.alignment.top_left,
                                                                        #width=screen_width*0.05,
                                                                        height = screen_height*0.42,
                                                                        padding=0.005,
                                                                        margin=0.005),

                                                        ft.Container(content=
                                                                        self.btnplay,
                                                                        alignment=ft.alignment.top_right,
                                                                        height = screen_height*0.42,
                                                                        padding=0.5,
                                                                        margin=0.5,
                                                                        width=screen_width*0.18) 
                                                        ],alignment=ft.alignment.center),

                                                ft.Row([
                                                        ft.Container(
                                                           bgcolor= "#9E9D9D",
                                                            height=screen_height,
                                                            #padding=ft.padding.all(0),
                                                            alignment=ft.alignment.bottom_right,
                                                            padding=0.5,
                                                            margin=0.5
                                                            ,
                                                        content= 
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.END,  
                                                                expand=True,
                                                                controls=[   
                                                                    ft.IconButton(
                                                                        padding = ft.padding.only(2,5,2,5),
                                                                        #mouse_cursor = ft.MouseCursor.ZOOM_IN,
                                                                        tooltip="Linkedin",
                                                                        on_click=lambda e: self.page.launch_url("https://www.linkedin.com/in/quelvincarvalho/"),
                                                                        content=ft.Image(src='img/linkedin.png')
                                                                    ),
                                                                    ft.IconButton(
                                                                        padding = ft.padding.only(2,5,2,5),
                                                                        tooltip="Github",
                                                                        on_click=lambda e: self.page.launch_url("https://github.com/quelvindev"),
                                                                        content=ft.Image(src='img/github.png')
                                                                    ),
                                                                    ft.IconButton(
                                                                        padding = ft.padding.only(2,5,2,5),
                                                                        tooltip="Site",
                                                                        on_click=lambda e: self.page.launch_url("https://quelvindev.github.io/meusite/"),
                                                                        content=ft.Image(src='img/site.png')
                                                                    ),
                                                                    ft.IconButton(
                                                                        padding = ft.padding.only(2,5,2,5),
                                                                        tooltip="Doe - Colabore",
                                                                        #on_click=lambda e: self.page.set_clipboard("https://github.com/quelvindev"),
                                                                        on_click= self.copy_pix,
                                                                        content=ft.Image(src='img/doe.png')
                                                                    )
                                                                ],
                                                            ),
                                                        ),
                                                    ]
                                                )])
        


        column = ft.Row(
                    expand=True,
                    controls=[
                       ft.Column([self.column_left]), 
                       ft.Column([self.column_right]) 
                       
   
                       # ft.Divider( color="#FFFFFF"),
                       # footer()
                ]
        )

      
        return column


def run(page: ft.Page):
    app_instance = HomePage(page)

    
   
ft.app(target=run)
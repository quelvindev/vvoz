import flet as ft
import screeninfo as esif
from machine.gerador import Gerador

class HomePage:

    def __init__(self,page:ft.Page= None):
        self.page = page
        self.fragment = Gerador()
        self.btn_time = 1.0
        monitor = esif.get_monitors()[0]
        screen_width = monitor.width*0.4
        screen_height = monitor.height*0.3
        page.title = 'Gerador de audio -Vvoz'
        page.window.alignment = ft.alignment.center
        page.window.width = screen_width
        page.window.height = screen_height
        inputs = self.column_one(screen_width,screen_height)
        page.add(inputs)
        page.update()
        
    
    def clear_text(self,e):
        
        if self.text.value.strip():
            self.text.value = ''
            self.text.focus()
            self.page.update()
        self.text_info.spans = [ft.TextSpan("Aguardando texto",
                    ft.TextStyle(weight=ft.FontWeight.BOLD),)]
    def get_text(self,e):
         
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
            self.fragment.generate_audio(self.text.value,self.btn_time.label)
            self.text_info.spans = [ft.TextSpan("Audio gerado!",
                    ft.TextStyle(weight=ft.FontWeight.BOLD,color="#6E7DAA"),)]
            self.btn_play.disabled = False
            self.btn_stop.disabled = False
            self.page.update()

         
    def copy_pix(self,e):
        key = 'b39a79bd-3de3-4f36-8fbe-5dda50038de9'
        self.page.set_clipboard(key)
        self.text_info.spans = [
                ft.TextSpan(
                    "Chave Pix copiada com sucesso!",
                    ft.TextStyle(weight=ft.FontWeight.BOLD, color="#463AEE"),
                )
            ]
        
        self.page.update()
    def unpause_audio(self,e):
        self.fragment.unpause_audio()
        self.btn_play.icon=ft.Icons.PAUSE
        self.btn_play.on_click = self.pause_audio
        self.page.update()

    def pause_audio(self,e):
        self.fragment.pause_audio()
        self.btn_play.icon=ft.Icons.PLAY_ARROW_SHARP
        self.btn_play.on_click = self.unpause_audio
        self.page.update()

    def play_audio(self,e):
        self.fragment.play_audio() 
        self.btn_play.icon=ft.Icons.PAUSE
        self.btn_play.on_click = self.pause_audio
        self.page.update()

    def stop_audio(self,e):
        self.fragment.stop_audio()
        self.btn_play.icon=ft.Icons.PLAY_ARROW_SHARP
        self.btn_play.on_click= self.play_audio
        self.page.update()

    def on_slider_change(self, e):
        self.btn_time.label  = f"{e.control.value:.1f}"
        self.page.update()

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
                                    icon_color="#FFFFFF",                                    
                                    height=50,
                                    tooltip='Limpar',
                                    alignment=ft.alignment.center,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=0),  
                                                padding=0, 
                                                bgcolor={"": "#000000", 
                                                         "disabled": "#999999"},),
                                    on_click=self.clear_text)
        self.btn_convert =  ft.FilledButton(
                                            text="Gerar",
                                            width=screen_width*0.2,
                                            height=50,
                                            #alignment=ft.alignment.center,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),  
                                                padding=0, 
                                                bgcolor={"": "#84A3E6", "disabled": "#999999"}
                                            ),
                                            on_click= self.get_text)
        self.btn_play =  ft.FilledButton(
                                            text="Play",
                                            width=screen_width*0.2,
                                            height=50,
                                            icon=ft.Icons.PLAY_ARROW_SHARP,
                                            disabled=True,
                                            style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(radius=0),  
                                                    padding=0 , 
                                                    bgcolor={"": "#562FC0", "disabled": "#999999"},                               
                                                ),
                                            
                                            on_click=self.play_audio,
                                        )
        self.btn_stop = ft.IconButton(
                                    icon=ft.Icons.STOP,
                                    icon_color="#FFFFFF",
                                    height=50,
                                    disabled=True,
                                    tooltip='Parar',
                                    alignment=ft.alignment.center,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=0),  
                                                padding=0, 
                                                bgcolor={"": "#562FC0", 
                                                         "disabled": "#999999"},),
                                    on_click=self.stop_audio)
        
        self.btn_time = ft.Slider( min=1.0, 
                                  max=2.0, 
                                  divisions=10, 
                                  label=self.btn_time,
                                  width=screen_width,
                                  on_change=self.on_slider_change
                                  )
        

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
                                        width= screen_width*0.3,
                                        height = screen_height,
                                        
                                        alignment=ft.MainAxisAlignment.START,
                                        controls=[ 
                                                ft.Row([     
                                                        ft.Container(content=  
                                                                        self.btn_clear,
                                                                        alignment=ft.alignment.top_left,
                                                                        width=screen_width*0.05,
                                                                        height = screen_height*0.20,
                                                                        padding=0.005,
                                                                       # margin=0.005
                                                                       ),

                                                        ft.Container(content=
                                                                        self.btn_convert,
                                                                        alignment=ft.alignment.top_right,
                                                                        height = screen_height*0.20,
                                                                        padding=0.5,
                                                                        #margin=0.5,
                                                                        width=screen_width*0.18) 
                                                        ]),
                                                ft.Row([ 
                                                        ft.Container(content=
                                                                        self.btn_time,
                                                                        width=screen_width*0.25,
                                                                        padding=0.5,
                                                                        margin=ft.margin.only(bottom =40),
                                                                        alignment=ft.alignment.top_left,
                                                                         ) ]),
                                                ft.Row([     
                                                        ft.Container(content=  
                                                                        self.btn_stop,
                                                                        alignment=ft.alignment.top_left,
                                                                        width=screen_width*0.05,
                                                                        height = screen_height*0.25,
                                                                        padding=0.005,
                                                                        margin=0.005),

                                                        ft.Container(content=
                                                                        self.btn_play,
                                                                        alignment=ft.alignment.top_right,
                                                                        height = screen_height*0.25,
                                                                        padding=0.5,
                                                                        margin=0.5,
                                                                        width=screen_width*0.18) 
                                                        ],alignment=ft.alignment.center),

                                                ft.Row([
                                                        ft.Container(
                                                           bgcolor= "#9E9D9D",
                                                            height=screen_height*0.10,
                                                            alignment=ft.alignment.bottom_center,
                                                           # padding=0.5,
                                                            margin=ft.margin.only(top =0,bottom=20)
                                                            ,
                                                        content= 
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.CENTER,  
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
                                                                        
                                                                        on_click=self.copy_pix,
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
                ]
        )

      
        return column


def run(page: ft.Page):
    app_instance = HomePage(page)

    
   
ft.app(target=run)
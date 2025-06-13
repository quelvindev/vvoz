# Gere audio a partir Textos com Python :rocket:

## Necessário instalar o FFmpeg
1. Baixe o FFmpeg Acesse: [Aqui](https://ffmpeg.org/download.html). Para Windows o caminho mais fácil é [Aqui](https://www.gyan.dev/ffmpeg/builds/)

    - Baixe a versão "release full build"  

    - Extraia em um local como C:\ffmpeg

2.  Adicione o FFmpeg ao PATH
    - Copie o caminho da pasta bin, por exemplo:
    ```
    C:\ffmpeg\bin
    ```

    - Vá em: Iniciar > Digite “Variáveis de ambiente”

    - Em “Variáveis do sistema”, encontre a variável chamada Path, clique em Editar

    - Clique em Novo e cole o caminho C:\ffmpeg\bin

    - Clique em OK em todas as janelas

    - Reinicie o terminal ou IDE (VS Code, etc) para aplicar as mudanças.
3. Teste se o FFmpeg está funcionando
    - Abra o terminal (cmd ou PowerShell) e digite:
    ```
    ffmpeg -version
    ```


    ### Para gerar o executável 
    1- Instale pyinstaller

    ```
    pip install pyinstaller
    ```
    2 - Gere o exe

    ```
    pyinstaller --onefile --add-data "img;img" --icon=icone.ico .\app.py
    ```
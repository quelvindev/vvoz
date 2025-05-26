from gtts import gTTS
from playsound import playsound



linguage = 'pt-br'
fala = '''
Polícia Federal abre inscrições para concurso. São mil vagas e salários de até R$ 26,8 mil.

Os interessados devem acessar o site do Cebraspe (Centro Brasileiro de Pesquisa em Avaliação e Seleção e de Promoção de Eventos ), a banca organizadora do concurso. Do total de vagas a serem preenchidas, 20% são reservadas para negros e indígenas, e 5% para pessoas com deficiência. A jornada de trabalho dos aprovados é de 40 horas semanais.
Para os cargos de escrivão, agente e papiloscopista, podem se inscrever graduados em qualquer curso de nível superior. Já as funções de delegado de Polícia Federal e perito criminal exigem formação específica.
As provas objetivas e discursivas serão aplicadas em todas as capitais e no Distrito Federal. A prova oral, exclusiva para o cargo de delegado, será realizada apenas em Brasília.
Candidatos doadores de medula óssea em entidades reconhecidas pelo Ministério da Saúde e inscritos no CadÚnico podem solicitar isenção da taxa.
Siga nosso canal girodenoticias55 para receber notícias relevantes do Brasil e do mundo!
'''

audio = gTTS(
    text=fala,
    lang = linguage
)


audio.save('audio.mp3')
playsound('audio.mp3')
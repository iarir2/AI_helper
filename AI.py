import tkinter as tk
import webbrowser as wb
import keyboard as kb
from pyperclip import copy
from time import sleep

bg = 'lightyellow'
fg = 'black'

root = tk.Tk()
root.title('AI #1 assistant')
root['bg'] = bg

cou = 0
second_line = 29
class Zagolovok:
    def __init__(self, t):
        global cou
        cou += 1
        col = 0 if cou <= second_line else 3
        row = cou if col == 0 else cou-second_line
        tk.Label(root, text=t, fg=fg, bg=bg, font='Arial 10 bold').grid(row=row, column=col, columnspan=2)
class Pachka:
    def __init__(self, t):
        global cou
        cou += 1
        tk.Label(root, text=t, fg=fg, bg=bg).grid(row=cou, column=0, sticky=tk.E)
        self.entry = tk.Entry(root, width=50, fg=fg, bg=bg)
        self.entry.grid(row=cou, column=1)
    def getter(self):
        return self.entry.get()

Zagolovok('Роль')
you = Pachka('Ты - ')
style = Pachka('Стиль общения:  ')
audience = Pachka('Твоя аудитория:  ')
refer = Pachka('Референсы:  ')
debat = Pachka('Смоделируй дебаты между:  ')

Zagolovok('Контекст')
situation = Pachka('Ситуация:  ')
add_info = Pachka('Дополнительная информация: ')

Zagolovok('Температура')
temp = Pachka('Температура:  ')

Zagolovok('Повторы')
fr_pen = Pachka('Частота повторов:  ')

Zagolovok('Метод')
method = Pachka('Используй следующий подход:  ')

Zagolovok('Материалы')
knowlage = Pachka('Используй следующие материалы:  ')

Zagolovok('Задача')
task = Pachka('Основная задача:  ')
add_task = Pachka('Подзадачи:  ')

Zagolovok('Примеры')
example = Pachka('Примеры:  ')

Zagolovok('Структура')
structure = Pachka('Структура ответа:  ')
leng = Pachka('Длина:  ')

Zagolovok('Обязательства')
dont_do = Pachka('Что НЕ делать:  ')
do_do = Pachka('Что ОБЯЗАТЕЛЬНО делать:  ')
Zagolovok(' ')

tk.Label(root, bg=bg, width=10).grid(column=2, row=0)

class PachkaDaGalochka:
    def __init__(self, t):
        global cou
        cou += 1
        self.state = tk.BooleanVar()
        col = 0 if cou <= second_line else 3
        row = cou if col == 0 else cou-second_line
        tk.Label(root, text=t, fg=fg, bg=bg).grid(row=row, column=col, sticky=tk.E)
        tk.Checkbutton(root, fg=fg, bg=bg, height=1, onvalue=1, offvalue=0, variable=self.state).grid(row=row, column=col+1, sticky=tk.W)
    def getter(self):
        return self.state.get()

Zagolovok('Проверки')
quality = PachkaDaGalochka('Проверка качества:  ')
secur = PachkaDaGalochka('Проверка надежности:  ')

Zagolovok('Техники')
step_by_step = PachkaDaGalochka('Шаг за шагом')
three_ways = PachkaDaGalochka('3 Разных подхода')
notes = PachkaDaGalochka('Заметки')
sigurnost = PachkaDaGalochka('Оценка уверенности')
parallel = PachkaDaGalochka('3 Решения')
mini_tasks = PachkaDaGalochka('Подзадачи')
self_check = PachkaDaGalochka('Самооценка')

Zagolovok('ИИ')
gpt = PachkaDaGalochka('GPT')
gemini = PachkaDaGalochka('GEMINI')
perplexity = PachkaDaGalochka('PERPLEXITY')
claude = PachkaDaGalochka('CLAUDE')

def promt():
    role = 1 if you.getter() or style.getter() or audience.getter() or refer.getter() or debat.getter() else 0
    task_check = 1 if task.getter() or add_task.getter() else 0
    tech = 1 if step_by_step.getter() or three_ways.getter() or notes.getter() or sigurnost.getter() or parallel.getter() or mini_tasks.getter() or self_check.getter() else 0
    context = 1 if situation.getter() or add_info.getter() else 0
    temperature = 1 if temp.getter() else 0
    freq = 1 if fr_pen.getter() else 0
    meth = 1 if method.getter() else 0
    know = 1 if knowlage.getter() else 0
    ex = 1 if example.getter() else 0
    out = 1 if structure.getter() or leng.getter() else 0
    cons = 1 if do_do.getter() or dont_do.getter() else 0
    qua = 1 if quality.getter() else 0
    add = 1 if secur.getter() else 0

    def h(text, obj):
        tempo = 1 if obj.getter() else 0
        return ('\n' + text + obj.getter()) * tempo
    def g(text, obj):
        tempi = 1 if obj.getter() else 0
        return ('\n' + text) * tempi

    result = f"""{'\n<role>' * role}{h('Ты - ', you)}{h('Твой стиль общения:  ', style)}{h('Твоя аудитория:  ', audience)}{h('Референсы:  ', refer)}{h('Смоделируй дебаты между:  ', debat)}{'\n</role>' * role}{'\n<task>' * task_check}{h('Основная задача:  ', task)}{h('Подзадачи:  ', add_task)}{'\n</task> ' * task_check}{'\n<techniques>\nИспользуй следующие техники:  ' * tech}{g('Рассуждай шаг за шагом, после каждого шага проверяй правильность рассуждений.', step_by_step)}{g('Рассмотри задачу с 3 разных подходов, после этого проанализируй все решения и выбери наиболее часто встречающийся ответ.', three_ways)}{g('Делай заметки после анализа каждого факта и опирайся на них когда будешь делать окончательный вывод.', notes)}{g('''Используй только известные тебе законы и факты, ничего не выдумывай. Для каждого утверждения в своём ответе: 
1. Оцени уверенность (высокая/средняя/низкая) 
2. Если уверенность низкая, пометь как [ТРЕБУЕТ ПРОВЕРКИ] 
3. Укажи источник знания (источник данных / логический вывод) ''', sigurnost)}{g('Исследуй несколько вариантов решения параллельно - представь, что три разных эксперта отвечают на этот вопрос. Каждый эксперт опишет один шаг своего размышления, затем поделится им с группой. После этого все эксперты перейдут к следующему шагу. Если какой-то эксперт поймёт, что ошибся, он выбывает из дискуссии.', parallel)}{g('Разбей задачу на простые подзадачи, реши каждую подзадачу по отдельности, затем объедини в итоговый ответ.', mini_tasks)}{g('''После того, как подготовишь окончательный ответ, проведи самооценку: 
1. Проверь все утверждения на логичность, 
2. Найди противоречия или неточности, 
3. Оцени сбалансированность (учтены ли разные точки зрения?), 
4. Предложи улучшения, 
Затем перепиши статью с учётом самооценки.''', self_check)}{'\n</techniques>' * tech}{'\n<context>' * context}{h('Ситуация:  ', situation)}{h('Дополнительная информация:  ',add_info)}{'\n</context>' * context}{'\n<temperature>' * temperature}{h('Температура:  ', temp)}{'\n</temperature>' * temperature}{'\n<frequency penalty>' * freq}{h('Частота повторов:  ', fr_pen)}{'\n</frequency penalty>' * freq}{'\n<methodology>' * meth}{h('Используй следующий подход:  ', method)}{'\n</methodology>'*meth}{'knowledge_base' * know}{h('Используй следующие материалы как основу знаний:  ', knowlage)}{'\n</knowledge_base>' * know}{'examples' * ex}{h('Примеры:  ', example)}{'\n</examples>' * ex}{'\n<output_format>' * out}{h('Структура ответа:  ', structure)}{h('Длина:  ', leng)}{'\n</output_format>' * out}{'\n<constraints>' * cons}{h('Что НЕ делать:  ', dont_do)}{h('Что ОБЯЗАТЕЛЬНО делать:  ', do_do)}{'\nОтвечай на том же языке, на котором задан вопрос. Если в вопросе используется английская терминология, сохрани её в ответе на русском.' * cons}{'\n</constraints>' * cons}{'\n<quality_check>' * qua}{g('''После выполнения проверь:  
Все ли данные обработаны?  
Соответствует ли формат требованиям?  
Есть ли противоречия в выводах?''', quality)}{'\n</quality_check>' * qua}{'\n<additional_instructions>' * add}{g('''Дополнительные инструкции:
Делай пометки в частях ответов, в которых не уверен. 
Сначала объясни свои рассуждения, затем дай ответ. 
Покажи свою работу: 
1. Покажи все формулы (если есть) 
2. Объясни каждый шаг 
3. Укажи допущения''', secur)}{'\n</additional_instructions>' * add}"""
    return result

links = {'GPT':'https://chatgpt.com/',
         'GEMINI':'https://gemini.google.com/app',
         'PERPLEXITY':'https://www.perplexity.ai/',
         'CLAUDE':'https://claude.ai/new'}

def main():
    copy(promt())
    if gpt.getter():
        wb.open(links['GPT'])
        sleep(2)
        kb.press_and_release('ctrl+v')
        sleep(1)
        kb.press_and_release('enter')
        sleep(2)
    if gemini.getter():
        wb.open(links['GEMINI'])
        sleep(2)
        kb.press_and_release('ctrl+v')
        sleep(1)
        kb.press_and_release('enter')
        sleep(2)
    if perplexity.getter():
        wb.open(links['PERPLEXITY'])
        sleep(2)
        kb.press_and_release('ctrl+v')
        sleep(1)
        kb.press_and_release('enter')
        sleep(2)
    if claude.getter():
        wb.open(links['CLAUDE'])
        sleep(2)
        kb.press_and_release('ctrl+v')
        sleep(1)
        kb.press_and_release('enter')
        sleep(2)



Zagolovok(' \n ')
tk.Button(root, text='CTAPT', command=main, fg=fg, bg=bg).grid(column=2, columnspan=3, row=cou-second_line)

root.mainloop()

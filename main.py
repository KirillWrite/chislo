import tkinter
import tkinter.messagebox
import random


# рандомное число
number = random.randint(1, 100)
print(number)

# количество попыток
pop = 10


def check_number():
    """
    Логика игры
    """
    #print(number)
    global pop
    guess = text_guess.get()
    guess = int(guess)
    while guess != number:
        if pop == 0:
            tkinter.messagebox.showinfo("Проигрыш", "Ты истратил все попытки")
            break
        elif guess > number:
            pop -= 1
            tkinter.messagebox.showinfo("", f"Загаданное число меньше, попыток осталось: {pop}")
            break
        elif guess < number:
            pop -= 1
            tkinter.messagebox.showinfo("", f"Загаданное число больше, попыток осталось: {pop}")
            break
    else:
        tkinter.messagebox.showinfo("Победа", "Ты угадал!")


def btn_confirm():
    """
    Приветствие
    """
    myName = text_name.get()
    tkinter.messagebox.showinfo("name", myName + ', я загадаю тебе число от 1 до 100, а ты угадай!')

root = tkinter.Tk()
root.minsize(360, 250)
root.maxsize(360, 250)
root.title('Игра угадай число')

# поле имя
label_name = tkinter.Label(root, text="Как тебя зовут?")
label_name.place(x=120, y=20)
text_name = tkinter.Entry(root, width=20)
text_name.place(x=100, y=50)
btnOK = tkinter.Button(root, text="Подтвердить", command=btn_confirm)
btnOK.place(x=120, y=80, height=30)

# поле ввода
label_guess = tkinter.Label(root, text='Введи  загаданное число')
label_guess.place(x=90, y=120)
text_guess = tkinter.Entry(root, width=10)
text_guess.place(x=130, y=150)
btnCheck = tkinter.Button(root, text='Мне повезёт!', command=check_number)
btnCheck.place(x=120, y=180, height=30)

# перезапуск инфо
restartBtn = tkinter.Label(root, text='Чтобы начать игру заново ,перезапусти приложение')
restartBtn.place(x=30, y=220, height=30)


root.mainloop()
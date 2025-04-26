import tkinter as tk

# Добавляем задачу в список всех задач из поля ввода
def add_task():
    task = entry.get()
    if task:
        all_task_list.insert(tk.END, task)
        entry.delete(0, tk.END)


# Переносим задачу в список "в работе"
def in_progress_task():
    selected_task_all = all_task_list.curselection()
    selected_task_finished = finished_task_list.curselection()

    if selected_task_all:
        in_progress_task_list.insert(tk.END, all_task_list.get(selected_task_all))
        all_task_list.delete(selected_task_all)
    if selected_task_finished:
        in_progress_task_list.insert(tk.END, finished_task_list.get(selected_task_finished))
        finished_task_list.delete(selected_task_finished)


# Переносим задачу в список "Завершено"
def finish_task():
    selected_task_all = all_task_list.curselection()
    selected_task_in_progress = in_progress_task_list.curselection()

    if selected_task_all:
        finished_task_list.insert(tk.END, all_task_list.get(selected_task_all))
        all_task_list.delete(selected_task_all)
    if selected_task_in_progress:
        finished_task_list.insert(tk.END, in_progress_task_list.get(selected_task_in_progress))
        in_progress_task_list.delete(selected_task_in_progress)


# Удаляем задачу
def delete_task():
    selected_task_all = all_task_list.curselection()
    selected_task_in_progress = in_progress_task_list.curselection()
    selected_task_finished = finished_task_list.curselection()

    if selected_task_all:
        all_task_list.delete(selected_task_all)
    if selected_task_in_progress:
        in_progress_task_list.delete(selected_task_in_progress)
    if selected_task_finished:
        finished_task_list.delete(selected_task_finished)


# Удаляем все выполненные задачи
def clear_finished_task():
    finished_task_list.delete(0, tk.END)


root = tk.Tk()
root.title("Task tracker")
root.configure(background="grey20")

label_1 = tk.Label(root, text="Добавить новую задачу:", bg="grey20")
label_1.grid(row=0, column=0)

entry = tk.Entry(root, bg="grey10")
entry.grid(row=0, column=1)

add_button = tk.Button(root, text="Добавить", command=add_task, bg="grey20")
in_progress_button = tk.Button(root, text="В работу", command=in_progress_task, bg="grey20")
finish_button = tk.Button(root, text="Выполнено", command=finish_task, bg="grey20")
delete_button = tk.Button(root, text="Удалить", command=delete_task, bg="grey20")
clear_button = tk.Button(root, text="Очистить", command=clear_finished_task, bg="grey20")

add_button.grid(row=0, column=2)
in_progress_button.grid(row=3, column=0)
finish_button.grid(row=3, column=1)
delete_button.grid(row=3, column=2)

label_2 = tk.Label(root, text="Ваш список задач:", bg="grey20")
label_2.grid(row=5, column=0)
label_3 = tk.Label(root, text="Задачи в работе:", bg="grey20")
label_3.grid(row=5, column=1)
label_4 = tk.Label(root, text="Завершенные задачи:", bg="grey20")
label_4.grid(row=5, column=2)
label_4 = tk.Label(root, text="", bg="grey20")
label_4.grid(row=1, column=0)  # Пустая строка для отступа в окне программы

all_task_list = tk.Listbox(root, bg="grey10")
in_progress_task_list = tk.Listbox(root, bg="grey10")
finished_task_list = tk.Listbox(root, bg="grey10")
all_task_list.grid(row=6, column=0)
in_progress_task_list.grid(row=6, column=1)
finished_task_list.grid(row=6, column=2)

clear_button.grid(row=7, column=2, pady=2)


root.mainloop()
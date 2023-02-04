#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from os import system
import os
import json
from tkinter import filedialog as fd 


with open("data.json", "r") as fh:
    dict_param = json.load(fh) # загружаем структуру из файла
    
#print(dict_param)

#===============================\
# Выводить messagebox?         #|
res_mb = dict_param['resultat']#|
#Показыть кнопку help?         #|
res_help = dict_param['help']  #|
#===============================/

def start():
    try:
        new_rep(name_choose_dir, cmt_entry.get())
        rep_connect(name_choose_dir, rep_entry.get())
    except:
        error()
    else:
        if res_mb == True:
            ready()
    root.destroy()
    
def new_rep(name_dir, commit):
    
    """Создание локального репозитория.
    
    В локальный репозиторий будут добавленны все файлы входящие в указанную директорию."""
    
    os.chdir(name_dir)

    commit_command = 'git commit -m "' +  commit + '"'

    system('git init')
    system('git add -A')
    system(str(commit_command))
    
    
def rep_connect(name_dir, rep):
    """Подключение у удаленному репозитоию.
    
    """
    
    os.chdir('/Users/mab1b0/Desktop/git control')
    log = open('log.txt', 'a')
    log.write(rep + '\n')
    log.close()
    
    os.chdir(name_dir)
    
    connect_command = 'git remote add origin ' + rep # по умолчанию стоит имя origin
    
    system(connect_command)
    system('git push origin master') # по умолчанию ветка master
    
    system('rm -rf .git')
    
def ready():
    messagebox.showinfo('result', 'successfully')
    
def help():
    #help = Toplevel(root)
    messagebox.showinfo('', 'dir: Указать полный путь до директории(включая имя директории)')#.place(x=5,y=5)
    messagebox.showinfo('', 'cmt: Указать commit')#.place(x=5,y=35)
    messagebox.showinfo('', 'rep: Указать ссылку (формата https) на удаленный репозиторий(github)')#.place(x=5, y=65)

def error():
    messagebox.showinfo('', 'error') 
def setting():
    settings_dict = {
        'resultat' : 'True',
        'help' : 'True'
    }
    # with open("data.json", "w") as fh:
    #  json.dump([1, 2, 3, 4, 5], fh) # записываем структуру в файл
    
    setting = Toplevel(root)
    setting.title('settings')
    setting.geometry('250x150')
    setting.resizable(width=False, height=False)
    
    def setting_save():
        print_res = var_res.get()
        settings_dict['resultat'] = print_res
        print_help = var_help.get()
        settings_dict['help'] = print_help
        
        with open("data.json", "w") as fh:
         json.dump(settings_dict, fh) # записываем структуру в файл
        
            
    var_res = BooleanVar()
    var_res.set(dict_param['resultat'])
    res_cb = Checkbutton(setting, text="Показывать результат",
                variable=var_res,
                onvalue=True, offvalue=False,
                command=setting_save)
    res_cb.place(x=5, y=5)
    
    var_help = BooleanVar()
    var_help.set(dict_param['help'])
    res_bt = Checkbutton(setting, text="Отображать кнопку help",
                variable=var_help,
                onvalue=True, offvalue=False,
                command=setting_save)
    res_bt.place(x=5, y=25)
    
    def save():
        root.destroy()
    
    save_btn = Button(setting, text='save', command=save)
    save_btn.place(x=5, y=45)
    
def callback():
    global name_choose_dir
    name_choose_dir = None
    name_choose_dir = fd.askopenfilename() 
    name_choose_dir = name_choose_dir.split('/')
    name_choose_dir.pop(len(name_choose_dir)-1)
    name_choose_dir = '/'.join(name_choose_dir)
    #print(name_choose_dir)
    
def clone_window():
    
    def start_clone():
        try:
            name_clone_file = rep_clone_ent.get()
            os.chdir(name_choose_dir)
            system(f'git clone {name_clone_file}')
            
        except:
            error()
        else:
            if res_mb == True:
                ready()
        clone_window.destroy()
    
    clone_window = Toplevel(root)
    clone_window.geometry('400x300')
    clone_window.resizable(width=False, height=False)
    
    Label(clone_window, text='git control (clone)', font='Type 30').place(x=75, y=5, width=250, height=36)
    
    Label(clone_window, text='rep', font='Type 20').place(x=5, y=50, width=30)
    Label(clone_window, text='dir', font='Type 20').place(x=5, y=80, width=25)  
    
    rep_clone_ent = Entry(clone_window)
    rep_clone_ent.place(x=50, y=50, width=300) 
    
    dir_clone_rep = Button(clone_window, text='choose', command=callback)
    dir_clone_rep.place(x=50, y=80, width=300)
    
    apply_clone_btn = Button(clone_window, text='apply', command=start_clone)
    apply_clone_btn.place(x=275, y=110, width=75, height=40)
    
      
        
    
# new_rep('/Users/mab1b0/Desktop/gitTest', 'test')
# rep_connect('/Users/mab1b0/Desktop/gitTest','https://github.com/kiebe/test.git')

root = Tk()
root.resizable(width=False, height=False)

#root['bg'] = ''
root.geometry('400x300')
root.title('git control')

Label(root, text='git control', font='Type 30').place(x=135, y=5, width=130, height=36)

dir_lbl = Label(root, text='dir', font='Type 20')
dir_lbl.place(x=5, y=50, width=25)
cmt_lbl = Label(root, text='cmt', font='Type 20')
cmt_lbl.place(x=5, y=80, width=35)
rep_lbl = Label(root, text='rep', font='Type 20')
rep_lbl.place(x=5, y=110, width=30)

dir_ent = Button(text='choose', command=callback)
dir_ent.place(x=50, y=50, width=300)

cmt_entry = Entry(root)
cmt_entry.place(x=50, y=80, width=300)

rep_entry = Entry(root)
rep_entry.place(x=50, y=110, width=300)

apply_btn = Button(root, text='apply', command=start)
apply_btn.place(x=275, y=150, width=75, height=40)

if res_help == True:
    help_btn = Button(root, text='help', command=help)
    help_btn.place(x=330, y=5)
    
setting_btn = Button(root, text='settings', command=setting)
setting_btn.place(x=5, y=5)


clone_btn_root = Button(root, text='clone', command=clone_window)

clone_btn_root.place(x=50, y=150, width=75)



root.mainloop()
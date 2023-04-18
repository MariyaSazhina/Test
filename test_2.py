import json
import csv
import datetime

# Функция для чтения списка заметок из файла
def read_notes_file(filename):
 with open(filename, 'r') as f:
  notes = json.load(f)
 return notes

# Функция для сохранения списка заметок в json формате
def save_notes_json(notes, filename):
 with open(filename, 'w', encoding='utf8') as f:
  json.dump(notes, f)

# Функция для сохранения списка заметок в csv формате
def save_notes_csv(notes, filename):
 with open(filename, 'w', encoding='utf8') as f:
  writer = csv.writer(f, delimiter=';')
  for note in notes:
   writer.writerow([note['id'], note['title'], note['body'], note['timestamp']])

# Функция для фильтра, проверка на дату
def filterByDate(pair, date):
  key, value = pair
  if value.date.date() == date:
    return True
  else: 
    return False

# Функция для фильтрации заметок по дате
def filter_notes_by_date(notes, date):
  newDict = {}
  for (key, value) in notes.items():
    if datetime.datetime.strptime(value['timestamp'], '%Y-%m-%d %H:%M:%S.%f').date() == date:
      newDict[key] = value

  return newDict

# Функция для вывода на экран выбранной записи или всего списка заметок
def print_notes(notes):
 if not notes:
  print('Заметок не найдено')
 else:
  for note in notes:
   currNote = notes[note]
   print(f'ID: {currNote["id"]}')
   print(f'Заголовок: {currNote["title"]}')
   print(f'Тело заметки: {currNote["body"]}')
   print(f'Дата/время: {currNote["timestamp"]}')
   print('---')

# Функция для добавления новой записки
def add_note(notes):
 if len(notes) == 0:
  id = 1
 else:
  id = notes[list(notes.keys())[-1]]['id'] + 1
 title = input('Введите заголовок: ')
 body = input('Введите тело заметки: ')
 timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
 new_note = {'id':id, 'title': title, 'body': body, 'timestamp': timestamp}
 notes[id] = new_note
 return notes

# Функция для редактирования записки
def edit_note(notes, id):
 for note in notes:
  if note == str(id):
   currNote = notes[note]
   new_title = input(f'Введите новый заголовок (было: {currNote["title"]}): ')
   new_body = input(f'Введите новое тело заметки (было: {currNote["body"]}): ')
   currNote['title'] = new_title
   currNote['body'] = new_body
   currNote['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
  break
 return notes

# Функция для удаления записки
def delete_note(notes, id):
 notes.pop(str(id))
 return notes

# Главная функция, которая выполняет все действия
def main():

  while True:
    
    filename = 'notes.json'
    notes = read_notes_file(filename)

    print('Выберите действие:')
    print('1. Вывести все заметки')
    print('2. Вывести заметки за определенную дату')
    print('3. Вывести конкретную заметку')
    print('4. Добавить новую заметку')
    print('5. Редактировать заметку')
    print('6. Удалить заметку')
    print('7. Выход')

    choice = input('Ваш выбор: ')

    if choice == '1':
      print_notes(notes)
    elif choice == '2':
      date_str = input('Введите дату в формате ГГГГ-ММ-ДД: ')
      date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
      filtered_notes = filter_notes_by_date(notes, date)
      print_notes(filtered_notes)
    elif choice == '3':
      id = int(input('Введите ID заметки: '))
      print_notes({str(id): notes[str(id)]})
    elif choice == '4':
      notes = add_note(notes)
      save_notes_json(notes, filename)
    elif choice == '5':
      id = int(input('Введите ID заметки для редактирования: '))
      notes = edit_note(notes, id)
      save_notes_json(notes, filename)
    elif choice == '6':
      id = int(input('Введите ID заметки для удаления: '))
      notes = delete_note(notes, id)
      save_notes_json(notes, filename)
    elif choice == '7':
      break
    else:
      print('Недопустимый выбор')

if __name__ == '__main__':
        main()
Git -  распределенная система контроля версий 
Это система для отслеживания и ведения историй изменений ваших файлов проекта.

Репозиторий - хранилище ваших файлов, которые вы отслеживаете при помощи гита и их изменений

Команды Git:
git init - создание локального репозитория, создается в той директории где вы запускаете команду

git add - после создания и изменения файла, то при помощи данной команды мы загружаем все изменения в промежуточное место хранения
 git add <file_name>
 git add . -> сохраняет все в текущей директории
 
 git commit - как только мы достигаем определенного момента в разработке, то мы сохраняем вместе с комментариями все наши изменения в репозитории
 (фиксация изменений в репозитории) Save progress
 git commit -m '<comment>' 
 
 git remote add - команда для связывания локального репозитория с удаленным в github 
  git remote add <название подключения> <ссылка на репозиторий>
  git remote add origin <URL>
  
 git push - команда для отправки изменений в файлах в репозиторий в гитхаб
  git push <origin> <название ветки (main)>
  git push origin main

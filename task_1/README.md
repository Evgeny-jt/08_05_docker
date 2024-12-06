Выполнить команды:

docker image build . --tag=task1:1.0    

docker run -d -p 9009:80 -v .:/usr/share/nginx/html task1:1.0

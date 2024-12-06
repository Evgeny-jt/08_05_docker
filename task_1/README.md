Выполнить команды:

docker image build . --tag=test:1.0    

docker run -d -p 9009:80 -v .:/usr/share/nginx/html test:1.0

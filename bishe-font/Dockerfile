FROM nginx:1.15-alpine 
#从dockerHub上拉取nginx
COPY dist /usr/share/nginx/html
#把vue项目打包后的 dist文件夹放在服务器的/usr/share/nginx/html 路径下
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
#把项目里的nginx.conf 退换掉nginx里的nginx.conf
EXPOSE 8080
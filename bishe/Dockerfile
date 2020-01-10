FROM openjdk:8-jdk-alpine
#从dcokerhub上拉取openjdk8
VOLUME /tmp
#在宿主机的/var/lib/docker目录下创建一个临时文件并把它链接到容器中的/tmp目录
ADD target/*.jar app.jar
#拷贝打包后的jar包并且重命名
EXPOSE 8088
#容器外露到服务器的端口
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom", "-Dserver.port=8088","-jar","/app.jar"]
# 为了缩短 Tomcat 的启动时间，添加java.security.egd的系统属性指向/dev/urandom作为 ENTRYPOINT
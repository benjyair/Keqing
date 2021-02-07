# Keqing

### 初始化环境

```shell
docker pull benjyair/keqing:latest
```

### 重新构建镜像

```shell
cd docker
# 1、导出当前 conda 环境
conda env export --from-history > environment.yml

# 2、open 'environment.yml' and insert 'mysqlclient' 
#  - mysqlclient

# 3、根据当前环境构建 docker 镜像
docker build -t benjyair/keqing .
#docker build --no-cache -t benjyair/keqing .

# 4、推送镜像到 docker hub
docker push benjyair/keqing
```

# Keqing

### 初始化环境

```shell
# 1、获取最近的 docker 镜像
docker pull benjyair/keqing:latest
# 2、激活镜像、进入命令行
# 3、检查当前 环境是否激活，如未激活手动激活
conda evn info -e
conda activate keqing
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

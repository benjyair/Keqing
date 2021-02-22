# Keqing

### 初始化环境

```shell
# 获取最近的 docker 镜像
docker pull benjyair/keqing:latest
```

### 重新构建镜像

```shell
# 1、进入 docker 目录
cd docker

# 2、导出当前 conda 环境
conda env export --from-history > environment.yml

# 3、根据当前环境构建 docker 镜像
docker build -t benjyair/keqing .
#docker build --no-cache -t benjyair/keqing .

# 4、推送镜像到 docker hub
docker push benjyair/keqing
```

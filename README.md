# Keqing

### 简介  
项目主要分为两个部分，Docker 镜像和 Python 代码  

其中 Python 部分完成了这样一个功能：
1、每天定时获取配置的基金涨跌信息，通过一个公式（周涨幅 * 4 - 月涨幅）算出基金一个类似于 MACD 的指标。  
2、将数据收集存入数据库中。  

Docker 部分则主要是我本地 Conda 镜像的副本，内部自动 Clone 项目，并启动定时任务。  

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

FROM continuumio/anaconda3
LABEL author=benjyair site=https://www.benjyair.com/

WORKDIR /home/work
# Create the environment
COPY environment.yml .
RUN conda env create -f ./environment.yml

# Pull repository
ENV GITHUB_URL=https://github.com/benjyair/Keqing.git
RUN git clone $GITHUB_URL
WORKDIR /home/work/Keqing
RUN git pull

CMD ["/bin/bash"]

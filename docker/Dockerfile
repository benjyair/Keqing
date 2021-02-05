FROM continuumio/anaconda3
LABEL author=benjyair site=https://www.benjyair.com/

WORKDIR /home/workdir
# Create the environment:
COPY environment.yml .
RUN conda env create -f ./environment.yml

CMD ["/bin/bash"]

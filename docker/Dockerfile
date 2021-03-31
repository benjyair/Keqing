FROM continuumio/anaconda3
LABEL author=benjyair site=https://www.benjyair.com/

WORKDIR /home/work
# Create the environment
COPY environment.yml .
RUN conda env create -f ./environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "keqing", "/bin/bash", "-c"]

# Pull repository
ENV GITHUB_URL=https://github.com/benjyair/Keqing.git
RUN git clone $GITHUB_URL
WORKDIR /home/work/Keqing

# Run the code
WORKDIR /home/work/Keqing/src
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "keqing", "python", "Main.py"]

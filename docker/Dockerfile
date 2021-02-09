FROM continuumio/anaconda3
LABEL author=benjyair site=https://www.benjyair.com/

WORKDIR /home/work
# Create the environment
COPY environment.yml .
RUN conda env create -f ./environment.yml
RUN echo "Docker Build: Environment is created"

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "keqing", "/bin/bash", "-c"]
RUN echo "Docker Build: Environment is activated"

# Pull repository
ENV GITHUB_URL=https://github.com/benjyair/Keqing.git
RUN git clone $GITHUB_URL
WORKDIR /home/work/Keqing
RUN git pull
RUN echo "Docker Build: Repository initialization completed"

# Run codes
WORKDIR /home/work/Keqing/src
RUN echo "Docker Build: The code to run when container is started"
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "keqing", "python", "Main.py"]

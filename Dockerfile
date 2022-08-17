FROM python:3.9-slim-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    xvfb xserver-xephyr xauth python3-tk python3-dev \
    ca-certificates scrot \
    xz-utils \
    sshpass
    
#RUN chromium chromium-driver
RUN apt-get -y install unzip wget gpg && \
    wget -P /root/ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get -y install -f /root/google-chrome*.deb && \
    wget -P /root/ https://chromedriver.storage.googleapis.com/104.0.5112.29/chromedriver_linux64.zip && \
    unzip /root/chromedriver_linux64.zip -d /root/ && \
    mv /root/chromedriver /usr/bin/

RUN rm -rf /var/lib/apt/lists/*

COPY /botSpotifyV1/requerimientosNeverinstall.txt ./requerimientosNeverinstall.txt
RUN pip3 install -r requerimientosNeverinstall.txt

#RUN sed -i 's%exec $LIBDIR/$APPNAME $CHROMIUM_FLAGS "$@"%exec $LIBDIR/$APPNAME $CHROMIUM_FLAGS "$@" --no-sandbox%g' "/usr/bin/chromium"

COPY /botSpotifyV1 .

CMD ["bash", "-c", "Xvfb :5 -ac & export DISPLAY=:5 ; python3 mainNeverInstall.py"]

# docker build -t display .
# docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display

# docker build -t display . && docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display
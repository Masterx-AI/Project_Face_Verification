FROM python:3.8-slim
ARG port
USER root

WORKDIR /face-verification-1/
COPY requirements.txt /face-verification-1

RUN apt-get update && apt-get install python3-opencv -y

#chgrp -R 0 /face-verification-1 \
    # && chmod -R g=u /face-verification-1 \
    # &&

RUN pip install -r requirements.txt

COPY . /face-verification-1

RUN sed -i 's/keras.engine.topology/keras.utils/' /usr/local/lib/python3.8/site-packages/keras_vggface/models.py

ENV PORT=$port
EXPOSE $PORT

ENTRYPOINT ["python","z.py"]
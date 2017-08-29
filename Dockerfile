FROM jupyter/datascience-notebook

MAINTAINER https://github.com/qiicr

USER root

USER $NB_USER

RUN mkdir -p ${HOME}/data
RUN cd ${HOME}/data && wget https://github.com/fedorov/dicom4miccai-handson/releases/download/QIN-HEADNECK_tables/QIN-HEADNECK-tables.zip && unzip QIN-HEADNECK-tables.zip

#RUN mkdir /src
#RUN ln -s /data /home/jovyan/work/src
#RUN cd /src && git clone https://github.com/fedorov/dicom4miccai-handson

#VOLUME /data
#VOLUME /src

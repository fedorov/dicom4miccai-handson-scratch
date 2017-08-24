FROM radiomics/pyradiomics

MAINTAINER https://github.com/qiicr

#LABEL dicom4miccai-handson-notebooks


RUN mkdir -p /data && mkdir -p /src
RUN cd /data && wget https://github.com/fedorov/dicom4miccai-handson/releases/download/QIN-HEADNECK_tables/QIN-HEADNECK-tables-no_clinical.zip && unzip QIN-HEADNECK-tables-no_clinical.zip

RUN mkdir /src
RUN ln -s /data /home/jovyan/work/src
RUN cd /src && git clone https://github.com/fedorov/dicom4miccai-handson

VOLUME /data
VOLUME /src

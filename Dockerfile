# Build Pyradiomics inside the Jupyter Datascience Notebook

FROM jupyter/datascience-notebook

MAINTAINER https://github.com/qiicr

# Build information
ARG BUILD_DATE
ARG GIT_REF

#LABEL dicom4miccai-handson-notebooks

USER root
ADD . /root/pyradiomics

# Make a global directory and link it to the work directory
RUN mkdir /data
RUN cd /data && wget https://github.com/fedorov/dicom4miccai-handson/releases/download/QIN-HEADNECK_tables/QIN-HEADNECK-tables-no_clinical.zip && unzip QIN-HEADNECK-tables-no_clinical.zip 

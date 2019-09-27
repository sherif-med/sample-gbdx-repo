FROM continuumio/miniconda3

RUN conda install -c conda-forge -c digitalglobe gbdxtools

COPY . ./app

RUN pip install --no-cache-dir scipy==1.2.0
RUN pip install dask==1.0.0

ENTRYPOINT [ "python" ] 

CMD ["./app/task/start.py"]

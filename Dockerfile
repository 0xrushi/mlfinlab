# FROM python:3.6
FROM python:3.8-slim-buster

RUN apt update && apt install git -y
# Install backend dependencies necessary to compile SCS and other solvers
RUN apt install -y build-essential g++ libgl1-mesa-glx libx11-6 cmake protobuf-compiler -y
RUN python -m pip install jupyter cvxpy
RUN git clone https://github.com/rushic24/mlfinlab.git && cd mlfinlab && python setup.py install
RUN pip install pandas==1.5.2 tqdm statsmodels==0.13.5 numpy==1.23.5

EXPOSE 8890
ENTRYPOINT [ "jupyter", "notebook", "--no-browser", "--port=8890", "--ip=0.0.0.0", "--allow-root" ]

FROM svizor/zoomcamp-model:3.11.5-slim
# add your stuff here

WORKDIR /app

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

# RUN pipenv install: This will create a new virtual env.
# Since we are dealing with dokcer container no need for that.
# Thus

RUN pipenv install --system --deploy

COPY ["predict_HW5.py", "model1.bin", "dv.bin", "./"]

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--host=0.0.0.0", "--port=9696", "predict_HW5:app" ]

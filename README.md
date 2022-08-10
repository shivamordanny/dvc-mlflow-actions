create env 

```bash
conda create -n wineq python=3.7 -y
```

activate env
```bash
conda activate wineq
```

created a req file

install the req
```bash
pip install -r requirements.txt
```
download the data from 

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

```bash
git init
```
```bash
dvc init 
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```

oneliner updates  for readme

```bash
git add . && git commit -m "update Readme.md"
```
```bash
git remote add origin https://github.com/shivamordanny/dvc-mlflow-actions.git
git branch -M main
git push origin main
```

tox command -
```bash
tox
```
for rebuilding -
```bash
tox -r 
```
pytest command
```bash
pytest -v
```

setup commands -
```bash
pip install -e . 
```

Hyperparameter tuning:

Change the hyperparameter for the elasticnet model from params.yaml

Run the mlflow server:
```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 -p 1234
```
Perform steps to start training:
```bash
dvc repro
```
Commit the changes to trigger the CI/CD pipeline:
```bash
git add . && git commit -m "version-8 ElasticNet" && git push origin main
```
Check the Deployment status under Github actions on the git repository.
Check the mlflow server to compare different models.

Webapp:

https://shivamordanny-wineq.herokuapp.com/
from fastapi import FastAPI
from fastapi.responses import FileResponse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


app = FastAPI()
data_file_path = 'data.csv'
image_file_path = 'image.png'


@app.get('/')
def get_root():
    return {'it': "works!"}


@app.get('/fit')
def get_fit():
    samples = 100
    x = np.random.rand(samples)
    m = 3
    b = 1

    y = m * x + b + np.random.normal(0.0, 0.2, size=samples)
    X = x.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)
    y_fit = model.predict(X)
    slope = model.coef_[0]
    intercept = model.intercept_

    data = pd.DataFrame({'x': x, 'y': y})
    data.to_csv(data_file_path, index=False)

    plt.figure()
    plt.scatter(x, y, label='data')
    plt.plot(x, y_fit, c='r', label=f'y = {slope:.2f} x + {intercept:.2f}')
    plt.title('scatter plot of random data points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.savefig(image_file_path)
    plt.close()

    return {
        'message': 'data generated and fitted successfully',
        'data_file': data_file_path,
        'image_file': image_file_path
    }


@app.get('/image')
def get_image():
    return FileResponse(image_file_path, media_type='image/png')


@app.get('/data')
def get_data():
    return FileResponse(data_file_path, media_type='text/csv')


def run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0")


if __name__ == '__main__':
    run()


# uvicorn dev2il_devops_app.main:app --host 0.0.0.0

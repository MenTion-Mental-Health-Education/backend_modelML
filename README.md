# backend_modelML
## Cloud Architecture
![Screenshot_66](https://github.com/MenTion-Mental-Health-Education/backend_modelML/assets/125712423/832ee56e-d74c-4bdb-a79d-7b528801799e)

## Getting Started
1. git clone https://github.com/MenTion-Mental-Health-Education/backend_modelML.git in Google Console editor
2. add ProjectID
``PROJECT_ID=replaceyourProjectID``
4. Build using
``docker build -t gcr.io/$PROJECT_ID/app:0.1 .``
5. Push to registry
``docker push gcr.io/$PROJECT_ID/app:0.1``
6. Go to Cloud Run and Create Service
7. Select **Deploy one revision from an existing container image** and Click **Container Registry** and Click **gcr.io/$PROJECT_ID/app** and select the image version
8. configure the service name and AutoScalling
9. in **Authentication** select **Allow unauthenticated invocations**
10. Configure the Capacity **Memory and CPU**
11. Click Create

## How to Access Our API
### 1. Predict ==>method `post`

`{{yourcloudrunlink}}/predict`

JSON Body
```
{
    "text": "i didnt feel humiliated"
}
```

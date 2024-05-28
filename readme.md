# Taichung Py 2024 Meetup05, 企業級 Flask Web App 開發實踐

> 本分支為 `deploy-docker` 分支，目標為演示以下：
> 
>  1. 使用 Dockerfile 建立 Docker Image
>  2. 使用 Docker Compose 啟動多個 Docker Container
>  3. 使用 Nginx 作為 Reverse Proxy Server
>  4. 使用不同的 Python Docker Base Image 進行打包

## 提醒事項

### 錯誤示範
本專案有以下問題：
1. sentry DSN 寫死在程式碼中，並上傳至 GitHub
2. 存有 `ZeroDivisionError` 問題的程式碼

### 啟動
1. 打包
    ``` bash
    docker-compose build
    ```
2. 啟動
    ``` bash
    docker compose up
    ```
3. 測試
    ``` bash
    curl --location 'http://127.0.0.1:8080/api/calculate' \
    --header 'Content-Type: application/json' \
    --data '{
        "x": 10,
        "y": 10,
        "operation": "divide"
    }'
    ```

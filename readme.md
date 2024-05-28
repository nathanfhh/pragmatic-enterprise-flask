# Taichung Py 2024 Meetup05, 企業級 Flask Web App 開發實踐

> 本分支為 `sentry-integration` 分支，目標為演示以下：
> 
>  1. 如何整合 Sentry 與 Flask

## 提醒事項

### 錯誤示範
本專案有以下問題：
1. sentry DSN 寫死在程式碼中，並上傳至 GitHub
2. 存有 `ZeroDivisionError` 問題的程式碼

### 測試
1. 觸發 `ZeroDivisionError` 錯誤
    ``` bash
    curl --location 'http://127.0.0.1:8080/api/calculate' \
    --header 'Content-Type: application/json' \
    --data '{
        "x": 10,
        "y": 0,
        "operation": "divide"
    }'
    ```
2. 登入 Sentry 查看錯誤訊息

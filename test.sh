curl -v -X POST https://api.line.me/v2/bot/message/push \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer {k1RCgmPzvmfqt20j1QBMKMZcBRzLMlfrURxw6i4ZDmWu8YU9f3ZENfd3vedWUmhXELb4jDHo378TIEAfpcd4yh0b5ms3I1mGQnXeO5WKypPJle/RitYUWt3qDxVhzMqMX3tEgw9S2Yt0vrFYZ3G5CQdB04t89/1O/w1cDnyilFU=}' \
    -d '{
        "to": "C50fd0c0f472fd29861f879619da076d0",
        "messages":[
            {
                "type":"text",
                "text":"あかちほ！！！"
            }
        ]
    }'

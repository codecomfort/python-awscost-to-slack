## 参考

### 元ネタ

- [Lambda で AWS の料金を毎日 Slack に通知する（Python3） - Qiita](https://qiita.com/isobecky74/items/88e8e0dcb0ee224a31e4)

### 請求情報について

- 一次情報、公式
  - [AWS Billing and Cost Management とは - AWS 請求情報とコスト管理](https://docs.aws.amazon.com/ja_jp/awsaccountbilling/latest/aboutv2/billing-what-is.html)

### boto3, get_metric_statictics について

- 一次情報、公式
  - [CloudWatch — Boto 3 Docs 1.9.33 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_statistics)
  - [GetMetricStatistics - Amazon CloudWatch](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html)

### CloudWatch メトリクス＝(指標、測定基準)について

- 一次情報、公式
  - [Amazon CloudWatch の概念 - Amazon CloudWatch](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
  - [Amazon CloudWatch メトリクスとディメンションのリファレンス - Amazon CloudWatch](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)

### lambda-uploader について

- 一次情報、公式
  - [rackerlabs/lambda-uploader: Helps package and upload Python lambda functions to AWS](https://github.com/rackerlabs/lambda-uploader)
- その他
  - コンソールで lambda-uploader と打つだけでアップロード完了するので便利

### タイムゾーンについて

- [AWS の Lambda のタイムゾーンを UTC から JST(東京)に変更 - Qiita](https://qiita.com/seisyu1985/items/2f3af4188a61dccf44b2)
- [Python の UTC ⇔ JST、文字列(UTC) ⇒ JST の変換とかのメモ - Qiita](https://qiita.com/yoppe/items/4260cf4ddde69287a632)

### Slack Webhooks について

- [Incoming Webhooks | Slack](
  https://api.slack.com/incoming-webhooks)

### Discord Webhooks について

- [Intro to Webhooks – Discord](
  https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
- [Discord - Developer Documentation](
  https://discordapp.com/developers/docs/resources/webhook#execute-webhook)
- [DiscordにWebhookでいろいろ投稿する - Qiita](
  https://qiita.com/Eai/items/1165d08dce9f183eac74)

### Python の Requests について

discord への POST を試している際、エラーは起こっていないのにメッセージが届かない現象あり

→[DiscordにWebhookでいろいろ投稿する - Qiita](
https://qiita.com/Eai/items/1165d08dce9f183eac74) で言及されているように、header にて Content-Type: application/json を指定する必要があるのだが、指定してないと 400 エラーが帰ってくるものの例外にならないため気付かなかった(正常終了したように見えた)

→400系/500系の場合のみ例外を発生させる方法があった

- [PythonモジュールRequestsのHTTPステータスコードについて ｜ DevelopersIO](
  https://dev.classmethod.jp/cloud/python-requests-status-code/)
- [Quickstart — Requests 2.20.1 documentation](
  http://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes)


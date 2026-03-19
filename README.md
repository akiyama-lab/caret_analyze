# caret_analyze

`caret_analyze` は Autoware システムから収集されたトレースデータを分析するためのPythonライブラリです。

このブランチでは、Autowareにおける停止イベントをもとに分析箇所を絞り込むための時間窓のカスタマイズ機能を提供しています。これにより、特定のイベントやトリガーに注目して、以下の分析を行うことができます。

- Message Flow: UNIX時間（ナノ秒）を使用して特定の時間窓内のメッセージフローを可視化
- Response Time: 上記の時間窓から Response Time メトリクスを抽出して可視化
- ヒストグラム: 上記の時間窓から抽出された Response Time データのヒストグラムを可視化

[ALB-Framework(Autoware Latency–Behavior Integrated Evaluation Framework)](https://github.com/akiyama-lab/alb-framework) でパフォーマンスを分析する際に使用しています。

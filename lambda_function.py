#!/usr/bin/env python
# encoding: utf-8
import json
from datetime import datetime, timedelta
import requests
import boto3
import os
import logging
from tzlocal import get_localzone

date_format = "%Y/%m/%d %H:%M"
local_zone = get_localzone()

# ログ関連
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Slack の設定
slack_post_url = os.environ["SLACK_POST_URL"]
slack_channel = os.environ["SLACK_CHANNEL"]


def get_cost(date):
    # CloudWatch の Billing メトリクスのリージョンは us-east-1 固定
    # (AWS コンソールで CloudWatch の請求を選ぶと、
    # 「US East(バージニア北部)にすべての請求データとアラームを表示します」
    # とポップアップが出る)
    cw_client = boto3.client("cloudwatch", region_name="us-east-1")
    # [CloudWatch — Boto 3 Docs 1.9.33 documentation]
    # (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_statistics)
    response = cw_client.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[
          {
            'Name': 'Currency',
            'Value': 'USD'
          }
        ],
        StartTime=date - timedelta(days=1),
        EndTime=date,
        Period=86400,
        Statistics=['Maximum']
    )
    cost = response["Datapoints"][0]["Maximum"]
    timestamp = response["Datapoints"][0]["Timestamp"]
    return cost, timestamp


def get_color_str(cost):
    float_cost = float(cost)
    if float_cost >= 50.0:
        return "#ff0000"
    elif float_cost > 30.0:
        return "warning"
    else:
        return "good"


def post_to_slack(message):
    try:
        requests.post(slack_post_url, data=json.dumps(message))
        # aws の python では 3.6 なのに f 文字列は怒られる
        # logger.info(f'Message posted to {message["channel"]}')
        logger.info('Message posted to {}'.format(message["channel"]))
    except requests.exceptions.RequestException as e:
        # logger.error(f'Request failed: {e}')
        logger.info('Request failed: {}'.format(e))


# 名前は Lambda の設定名に合わせる
def lambda_handler(event, context):
    utc_now = datetime.utcnow()
    cost, res_utc_now = get_cost(utc_now)
    jst_now = res_utc_now.astimezone(local_zone)
    color = get_color_str(cost)
    message = '{}までのAWS料金は ＄{}です'.format(jst_now.strftime(date_format), cost)

    slack_message = {
        "channel": slack_channel,
        "attachments": [
          {
            "text": message,
            "color": color
          }
        ]
    }

    post_to_slack(slack_message)

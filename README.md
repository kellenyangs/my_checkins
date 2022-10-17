# GitHub Actions

## 配置参数

依次点击【Setting】->【Security】->【Secrets】->【Actions】->【New repository secrets】 添加对应的设置，以 Key: Value 的形式，有多个配置参数就添加多次。

## WorkFlow

workflows 下可以有多个 .yml 文件会自动执行

```
# workflow 名称
name: Checkins

# 什麼情況下触发 workflow
on:
  # 对于 main branch 建立 Branch 与 Pull Request 时触发 workflow
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  # 允许你从 Action 页面上手动执行 workflow
  workflow_dispatch:
  #  在指定的时间(周期)触发 workflow。
  # 第一位代表 minute
  # 第二位代表 hour
  # 第三位代表 day
  # 第四位代表 month
  # 第五位代表 day of week
  schedule:
    # 每日7点执行一次
    - cron: '0 9 * * *'

# 使用该字段，可以限制 GITHUB_TOKEN 赋予的权限。这是一个全局的权限设置，会运用在工作流的所有任务中。也可以为某个单独的任务添加 premissions 字段单独设置权限.
# 当你为某些字段设定了权限后，所有未设定权限的字段值为None
permissions:
  actions: write
  checks: write
  contents: write
  deployments: write
  issues: write
  packages: write
  pull-requests: write
  repository-projects: write
  security-events: write
  statuses: write

# 这些job的执行默认是并行的，如果需要串行执行job，需要设定job.<job_id>.needs关键字
# 每一个job运行的环境由runs-on指定
jobs:
  check-in:
    # 指定运行所需要的虚拟机环境。它是必填字段。目前可用的虚拟机如下。
    # ubuntu-latest，ubuntu-18.04或ubuntu-16.04
    # windows-latest，windows-2019或windows-2016
    # macOS-latest或macOS-10.14
    runs-on: ubuntu-latest

    # 指定每个 Job 的运行步骤，可以包含一个或多个步骤。每个步骤都可以指定以下三个字段。
    # jobs.<job_id>.steps.name：步骤名称
    # jobs.<job_id>.steps.run：该步骤运行的命令或者 action。
    # jobs.<job_id>.steps.env：该步骤所需的环境变量。
    steps:
    # 1. 构建源码
    - uses: actions/checkout@v2

    # 2. 安装环境
    - name: Install Python
      run: |
        sudo apt update && \
        sudo apt install python3

    # 3. 安装依赖
    - name: requirements
      run: |
        pip3 install -r requirements.txt

    # 执行脚本文件
    - name: Checkin
      run: |
        user='${{ secrets.USER }}'
        pwd='${{ secrets.PWD }}'

        user_list=()
        pwd_list=()

        IFS=","

        for u in ${user[*]}
        do
        user_list[${#user_list[*]}]=${u}
        done

        for p in ${pwd[*]}
        do
        pwd_list[${#pwd_list[*]}]=${p}
        done

        user_num=${#user_list[*]}
        pwd_num=${#pwd_list[*]}

        if [ $user_num != $pwd_num ];then
        echo "账号和密码个数不对应"
        exit 1
        else
        echo "共有 $user_num 个账号，即将开始签到"
        fi

        for ((i=0;i<$user_num;i++))
        do
        python3 checkin.py --username ${user_list[$i]} --password ${pwd_list[$i]}
        done
    # 4. 提交日志
    - name: Commit
      run: |
        git config --global user.email founder.yu@foxmail.com
        git config --global user.name founder-yu
        git add .
        git commit -m "Update flow.log" -a
    - name: Push changes
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
```

## 说明

- 支持多账号，账号之间与密码之间用半角逗号分隔，账号与密码的个数要对应。

- 脚本会在北京时间00:07执行一次(Github定时任务会有20min左右延迟)，或者自己点击Star亦可手动执行一次(无延迟)。

- 运行结束后，会在flow.log中生成日志信息，您可以在此查看运行结果信息(flow.log文件中的时间以协调世界时显示)。
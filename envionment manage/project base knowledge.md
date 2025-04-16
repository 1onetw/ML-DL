# project base knowledge

## 创建环境

1. anaconda创建环境 (可任意指定版本)

    开始任何一个项目，开始一个新环境，是一个好习惯
    ```bash
    $ conda create -n myenv python=3.10
        -n：指明环境名称，环境路径默认保存在Anaconda3\envs\环境名
    $ conda create -p venv python=3.10
        -p：指明环境路径，将环境与项目绑定
    ```

2. python 创建环境 (根据当前path的python版本创建环境)
    ```bash
    $ python -m venv venv1
    ```
    venv1/scripts目录下有activate.bat和deactivate.bat

3. virtualenv创建环境(根据当前path的python版本创建环境)
    ```bash
    $ pip install virtualenv
    $ virtualenv -p python3 virtual_env
    ```
    virtualenv/scripts目录下有activate.bat和deactivate.bat

## 激活环境

```bash
$ conda activate venv
```

## 退出环境
```bash
$ conda deactivate
```

## 包管理

requirements.txt，可进行依赖安装

```bash
$ pip install -r requirements.txt
```

## 项目文件类型

1. ipynb：jupyter notebook文件
    - 需pip install ipykernel：才可运行python代码
2. py：python文件


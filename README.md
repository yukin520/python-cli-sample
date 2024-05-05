
# python-cli-sample

Pythonのパッケージングと、cli用のライブラリ`click`の使い方に関する個人の備忘を兼ねたサンプルリポジトリです。
`democli`というシンプルなCLIツールをパッケージとして配布することを想定しています。

```shell
$ democli color-echo --word OK --color red
OK
```

```shell
$ democli show-progress --total-seconds 5 --between-seconds 1
  [------------------------------------]    0%  sleep(1/5)...
  [#########---------------------------]   25%  00:00:03  sleep(2/5)...
  [##################------------------]   50%  00:00:02  sleep(3/5)...
  [###########################---------]   75%  00:00:01  sleep(4/5)...
  [####################################]  100%          

 Finished command!!
```

```shell
democli edit-file --file-path README.md 
```

## install

```shell
$ git clone https://github.com/Yuki0520-ba/python-cli-sample.git
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install ./python-cli-sample
```

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install git+https://github.com/Yuki0520-ba/python-cli-sample.git
```
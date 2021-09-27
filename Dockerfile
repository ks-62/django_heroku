FROM python:3            
    # 元となるdockerイメージを指定
ENV PYTHONUNBUFFERED 1   
    # この環境変数に値を入れることでバッファを無効化する('1'じゃなくてもいい)
RUN mkdir /code          
    # codeディレクトリを作成
WORKDIR /code            
    # codeディレクトリに移動
COPY requirements.txt /code/   
    # txtファイルをcodeディレクトリに配置
RUN pip install --upgrade pip && pip install -r requirements.txt
    # pipコマンドを最新にし、txtファイル内のパッケージ（後述）をpipインストール
COPY . /code/            
    # sample-pj/配下のファイルをcodeディレクトリにコピー